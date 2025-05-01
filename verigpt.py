import openai
import argparse
import sys
import os

def print_help():
    """Print detailed help information about the script."""
    print("""
VeriGPT: HDL Code Generator
==========================

This tool generates HDL (Hardware Description Language) code using OpenAI's GPT models
based on a text prompt file.

Usage:
  python verigpt.py --prompt <prompt_file> --output <output_file> [--model <model_name>]
  python verigpt.py -p <prompt_file> -o <output_file> [-m <model_name>]
  python verigpt.py --help

Arguments:
  --prompt, -p     Path to the prompt file containing HDL requirements
  --output, -o     Path where the generated HDL code will be saved
  --model, -m      OpenAI model to use (default: gpt-4)
  --help, -h       Show this help message and exit

Examples:
  python verigpt.py -p prompts/counter.txt -o generated/counter.v
  python verigpt.py -p prompts/alu.txt -o generated/alu.v -m gpt-3.5-turbo

Requirements:
  - OpenAI API key must be set as an environment variable (OPENAI_API_KEY)
  - Prompt file should contain clear specifications for the HDL code

Note:
  If arguments are not provided, the script will prompt for them interactively.
""")

def generate_hdl(prompt_path: str, output_path: str, model: str = "gpt-4"):
    """Generate HDL code from a prompt file and save to the output path"""
    
    # Check if prompt file exists
    if not os.path.isfile(prompt_path):
        print(f"Error: Prompt file '{prompt_path}' does not exist")
        return False
    
    try:
        # Read the prompt
        with open(prompt_path, "r") as f:
            prompt = f.read()
        
        print(f"Generating HDL code using {model}...")
        
        # Generate the HDL code
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )

        code = response['choices'][0]['message']['content']
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Write the generated code to the output file
        with open(output_path, "w") as f:
            f.write(code)
        
        print(f"✅ HDL code successfully generated and written to {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error generating HDL code: {str(e)}")
        return False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate HDL code using GPT-4")
    parser.add_argument("--prompt", "-p", required=False, help="Path to the prompt file")
    parser.add_argument("--output", "-o", required=False, help="Path to save the generated HDL code")
    parser.add_argument("--model", "-m", default="gpt-4", help="OpenAI model to use (default: gpt-4)")
    args = parser.parse_args()
    
    prompt_path = args.prompt
    output_path = args.output
    
    # If arguments weren't provided, prompt the user
    if not prompt_path:
        prompt_path = input("Enter path to prompt file: ")
    
    if not output_path:
        output_path = input("Enter path for output HDL file: ")
    
    # Validate inputs
    if not prompt_path or not output_path:
        print("Both prompt and output paths are required.")
        return
    
    # Generate the HDL code
    generate_hdl(prompt_path, output_path, args.model)

if __name__ == "__main__":
    main()
