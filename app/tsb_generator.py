# tsb_generator.py

import ollama

def generate_tsb_with_ollama(repair_log: str, prompt_template: str) -> str:
    """
    Generate a Technical Service Bulletin (TSB) from a repair log using Ollama.
    
    Args:
        repair_log (str): The raw repair log text.
        prompt_template (str): The TSB prompt template with a {log} placeholder.
    
    Returns:
        str: The generated TSB content.
    """
    prompt = prompt_template.replace("{log}", repair_log)

    messages = [
        {"role": "system", "content": "You are a technical writer generating official Technical Service Bulletins (TSBs)."},
        {"role": "user", "content": prompt}
    ]

    # 👇 Choose a lightweight, fast model like "mistral" or "llama2"
    response = ollama.chat(model="mistral", messages=messages)

    return response["message"]["content"]
