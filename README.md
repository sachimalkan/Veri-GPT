# VeriGPT-HDL: Trustworthy LLM-Driven Hardware Design Automation

VeriGPT-HDL is a prototype framework that integrates Large Language Models (LLMs) like GPT-4 with simulation-based feedback loops to automatically generate, validate, and refine Verilog HDL code. It targets the automation of hardware design by incorporating formal verification principles and iterative correction mechanisms in a closed-loop system.

## Core Features
- LLM-driven code synthesis for complex digital modules (ALUs, FIFOs, pipelines, DSP cores)
- Testbench co-generation and output waveform validation
- Multi-round refinement using simulation outputs and structured re-prompting
- Integration with Icarus Verilog and Verilator backends
- Error classification and response strategy engine (e.g., syntax error, race condition, logic bug)
- Modular prompt injection and constraint templates

## Directory Structure
```
verigpt-hdl/
├── prompts/                     # Dynamic prompt templates
│   ├── alu_pipeline.txt
│   └── fft_accelerator.txt
├── verilog/                    # LLM-generated Verilog files
│   └── alu_pipeline.v
├── testbenches/                # Co-generated or templated testbenches
│   └── tb_alu_pipeline.v
├── logs/                       # Simulation logs, compile errors
│   └── sim_trace_round2.log
├── feedback_strategies/        # Refinement logic for different failure types
│   └── retry_fix_logic_bug.py
├── verigpt.py                  # Code generation wrapper
├── verify.py                   # Compile + simulate + parse
├── feedback_loop.py            # Loop orchestrator
└── README.md
```

## Sample Usage
### 1. Generate HDL from LLM
```python
from verigpt import generate_hdl

generate_hdl("prompts/alu_pipeline.txt", "verilog/alu_pipeline.v")
```

### 2. Simulate and Capture Output
```python
from verify import simulate

simulate("verilog/alu_pipeline.v", "testbenches/tb_alu_pipeline.v")
```

### 3. Run Feedback-Driven Correction Loop
```python
from feedback_loop import run_feedback_loop

run_feedback_loop(
    prompt_path="prompts/alu_pipeline.txt",
    verilog_path="verilog/alu_pipeline.v",
    testbench_path="testbenches/tb_alu_pipeline.v",
    log_output="logs/sim_trace_round2.log"
)
```

## Feedback Strategies
- **Syntax Error** → Regenerate with cleaned formatting
- **Simulation Failure** → Add waveform diffing and assertion-based localization
- **Functional Mismatch** → Re-prompt with previous inputs and expected output patterns
- **Unstable Output** → Inject clock domain crossing templates and metastability constraints

## Example Prompt (for `fft_accelerator.txt`)
```
Generate a Verilog module for a parameterized 8-point FFT accelerator using Radix-2 architecture. It should pipeline stages using `generate` loops and include latency-balancing registers. Do not include the testbench.
```

## Requirements
- Python 3.8+
- openai >= 0.28
- iverilog or verilator

## Output Example (Simulation Pass)
```
> Simulation complete.
> All test vectors passed.
> Peak memory usage: 18MB
> Logic coverage: 100%
> Cycle latency: 22
```
