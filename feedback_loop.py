import os
import re
import subprocess
import argparse
from verigpt import generate_hdl
from verify import simulate

def get_syntax_errors(hdl_file):
    """Get syntax errors from iverilog compilation"""
    try:
        # Run iverilog in check-only mode 
        result = subprocess.run(["iverilog", "-t", "null", "-y", ".", hdl_file], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            return result.stderr
        return None
    except Exception as e:
        return str(e)

def fix_syntax_errors(prompt_file, error_message):
    """Create an improved prompt based on syntax errors"""
    with open(prompt_file, 'r') as f:
        original_prompt = f.read()
    
    # Create a new prompt focusing on syntax issues
    new_prompt = f"""
{original_prompt}

The previous code had the following syntax errors:
{error_message}

Please fix these issues and ensure the code follows proper Verilog syntax.
Pay special attention to:
- Missing semicolons
- Unmatched begin/end blocks
- Proper module port declarations
- Signal width declarations
- Case statement completeness
"""
    
    # Write to a temporary prompt file
    temp_prompt = prompt_file.replace('.txt', '_syntax_fixed.txt')
    with open(temp_prompt, 'w') as f:
        f.write(new_prompt)
    
    return temp_prompt

def capture_waveform(hdl_file, testbench_file, output_vcd):
    """Capture VCD waveform for debugging"""
    try:
        # First compile with VCD output enabled
        subprocess.run(["iverilog", "-o", "wave_sim.out", 
                      "-DVCD_OUTPUT", testbench_file, hdl_file], check=True)
        
        # Then run simulation to generate VCD
        subprocess.run(["vvp", "wave_sim.out"], check=True)
        
        return os.path.exists(output_vcd)
    except Exception as e:
        print(f"Error capturing waveform: {e}")
        return False

def locate_failure_points(testbench_file, simulation_output):
    """Extract assertion failures and problematic test cases"""
    # Look for assertion failures
    assertion_pattern = r'Assertion failed:.*at\s+(\w+\.v:\d+)'
    assertions = re.findall(assertion_pattern, simulation_output)
    
    # Look for failed test patterns
    test_pattern = r'TEST CASE (\d+).*FAILED'
    test_cases = re.findall(test_pattern, simulation_output)
    
    return assertions, test_cases

def improve_functional_prompt(prompt_file, testbench_file, simulation_output, assertions, test_cases):
    """Create improved prompt based on functional issues"""
    with open(prompt_file, 'r') as f:
        original_prompt = f.read()
    
    # Extract expected behavior from testbench
    testbench_content = ""
    if os.path.exists(testbench_file):
        with open(testbench_file, 'r') as f:
            testbench_content = f.read()
    
    # Create a new prompt with functional requirements
    new_prompt = f"""
{original_prompt}

The code fails to meet the following functional requirements:

Simulation output showing failures:
{simulation_output[:500]}...

Failed assertions: {assertions}
Failed test cases: {test_cases}

Here's the testbench that the code needs to pass:
```verilog
{testbench_content}"""

def add_stability_constraints(prompt_file):
    """Add stability constraints to the prompt"""
    with open(prompt_file, 'r') as f:
        original_prompt = f.read()
    
    # Create a new prompt with stability requirements
    new_prompt = f"""
{original_prompt}

Please improve the design with the following stability considerations:
- Add proper clock domain crossing logic where needed
- Ensure all inputs are properly synchronized to prevent metastability
- Add reset synchronization if needed
- Consider using double-flop synchronizers for external inputs
- Verify that all state machines have well-defined reset states
"""
    
    # Write to a temporary prompt file
    temp_prompt = prompt_file.replace('.txt', '_stability_fixed.txt')
    with open(temp_prompt, 'w') as f:
        f.write(new_prompt)
    
    return temp_prompt

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='HDL Feedback Loop Generator')
    parser.add_argument('--prompt', help='Path to prompt file')
    parser.add_argument('--hdl', help='Path for HDL output file')
    parser.add_argument('--testbench', help='Path to testbench file')
    parser.add_argument('--attempts', type=int, default=5, help='Maximum attempts')
    args = parser.parse_args()
    
    # Get file paths from user if not provided
    prompt_file = args.prompt or input("Enter path to prompt file: ")
    hdl_file = args.hdl or input("Enter path for HDL output file: ")
    testbench_file = args.testbench or input("Enter path to testbench file: ")

    # Validate inputs
    if not prompt_file or not hdl_file or not testbench_file:
        print("All file paths are required.")
        return

    MAX_ATTEMPTS = args.attempts
    vcd_file = "waveform.vcd"  # Default VCD output file

    for attempt in range(MAX_ATTEMPTS):
        print(f"\n======= Attempt {attempt+1} =======")
        
        # Generate HDL from prompt
        success = generate_hdl(prompt_file, hdl_file)
        if not success:
            print("Failed to generate HDL. Aborting.")
            break
        
        # Check for syntax errors
        syntax_errors = get_syntax_errors(hdl_file)
        if syntax_errors:
            print("❌ Syntax errors detected:")
            print(syntax_errors[:500] + "..." if len(syntax_errors) > 500 else syntax_errors)
            print("Regenerating with improved syntax prompt...")
            prompt_file = fix_syntax_errors(prompt_file, syntax_errors)
            continue
        
        # Simulate the design
        simulation_result = simulate(hdl_file, testbench_file)
        if simulation_result:
            print("✅ HDL PASSED Verification!")
            break
        
        # Capture waveform for debugging
        print("Capturing waveform for debugging...")
        waveform_captured = capture_waveform(hdl_file, testbench_file, vcd_file)
        
        # Get the simulation output
        with open("sim_output.log", "r") if os.path.exists("sim_output.log") else open(os.devnull, "r") as f:
            simulation_output = f.read()
        
        # Locate failure points
        assertions, test_cases = locate_failure_points(testbench_file, simulation_output)
        
        if assertions or test_cases:
            print(f"❌ Functional mismatch detected. Found {len(assertions)} assertion failures and {len(test_cases)} failed test cases.")
            print("Regenerating with improved functional requirements...")
            prompt_file = improve_functional_prompt(prompt_file, testbench_file, simulation_output, assertions, test_cases)
        else:
            print("❌ Unstable output or timing issues detected.")
            print("Adding clock domain crossing and metastability constraints...")
            prompt_file = add_stability_constraints(prompt_file)

    if attempt == MAX_ATTEMPTS - 1:
        print(f"\n❌ Failed to generate working HDL after {MAX_ATTEMPTS} attempts.")
        print("Please review the modified prompts and simulation outputs for further debugging.")

    print("\nGenerated files:")
    print(f"  HDL: {hdl_file}")
    if os.path.exists(vcd_file):
        print(f"  Waveform: {vcd_file}")

    # List all prompt variations that were created
    print("\nPrompt variations:")
    prompt_dir = os.path.dirname(prompt_file)
    prompt_base = os.path.basename(prompt_file).split('.')[0]
    for file in os.listdir(prompt_dir or '.'):
        if file.startswith(prompt_base) and file.endswith('.txt'):
            print(f"  {os.path.join(prompt_dir, file)}")

if __name__ == "__main__":
    main()
