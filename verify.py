import subprocess

def simulate(verilog_file: str, testbench_file: str):
    try:
        subprocess.run(["iverilog", "-o", "sim.out", testbench_file, verilog_file], check=True)
        result = subprocess.run(["vvp", "sim.out"], capture_output=True, text=True)
        print("Simulation Output:\n", result.stdout)
        return "PASS" in result.stdout
    except subprocess.CalledProcessError as e:
        print("Error during simulation:", e)
        return False
