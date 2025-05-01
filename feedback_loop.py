from verigpt import generate_hdl
from verify import simulate

prompt_file = "prompts/adder_prompt.txt"
hdl_file = "verilog/generated_adder.v"
testbench_file = "testbenches/tb_adder.v"

MAX_ATTEMPTS = 3
for attempt in range(MAX_ATTEMPTS):
    print(f"\nAttempt {attempt+1}")
    generate_hdl(prompt_file, hdl_file)
    if simulate(hdl_file, testbench_file):
        print("HDL PASSED Verification!")
        break
    else:
        print("HDL FAILED. Retrying with refined prompt...")
        # Optional: Modify the prompt or regenerate from a fallback
