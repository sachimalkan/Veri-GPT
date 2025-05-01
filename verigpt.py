import openai

def generate_hdl(prompt_path: str, output_path: str):
    with open(prompt_path, "r") as f:
        prompt = f.read()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    code = response['choices'][0]['message']['content']
    
    with open(output_path, "w") as f:
        f.write(code)
    
    print(f"HDL written to {output_path}")
