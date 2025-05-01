import subprocess
import sys

def print_help():
    """Print help information about the script."""
    print("""
Verilog Simulator using Icarus Verilog
======================================

This script compiles and simulates Verilog designs using Icarus Verilog.

Usage:
  python verify.py [verilog_file] [testbench_file]
  python verify.py --help

Arguments:
  verilog_file    Path to the Verilog design file (.v)
  testbench_file  Path to the testbench file (.v)

Examples:
  python verify.py my_design.v my_testbench.v

Requirements:
  - Icarus Verilog (iverilog) must be installed on your system
  - Your testbench should output "PASS" when tests pass successfully

Note:
  If no arguments are provided, the script will prompt for file paths.
""")

def simulate(verilog_file: str, testbench_file: str):
    try:
        print(f"Compiling {verilog_file} with testbench {testbench_file}...")
        subprocess.run(["iverilog", "-o", "sim.out", testbench_file, verilog_file], check=True)
        
        print("Running simulation...")
        result = subprocess.run(["vvp", "sim.out"], capture_output=True, text=True)
        
        print("\nSimulation Output:\n" + "-"*50)
        print(result.stdout)
        print("-"*50)
        
        if "PASS" in result.stdout:
            print("\n✅ Simulation PASSED")
            return True
        else:
            print("\n❌ Simulation did not indicate PASS")
            return False
    except subprocess.CalledProcessError as e:
        print("❌ Error during simulation:", e)
        return False
    except FileNotFoundError as e:
        print("❌ Error: iverilog or vvp not found. Make sure Icarus Verilog is installed.")
        return False

def main():
    print("Verilog Simulator using Icarus Verilog")
    print("======================================")
    
    verilog_file = input("Enter path to Verilog design file: ")
    testbench_file = input("Enter path to testbench file: ")
    
    if not verilog_file or not testbench_file:
        print("❌ Error: Both design and testbench files are required")
        return
        
    simulate(verilog_file, testbench_file)

if __name__ == "__main__":
    main()
