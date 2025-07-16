import os
from tsb_generator import generate_tsb_with_ollama

# Load all repair logs from a file (one or multiple logs separated by blank lines)
with open("repair_logs_sample.txt", "r") as file:
    repair_logs = [log.strip() for log in file.read().split("\n\n") if log.strip()]

# Load prompt template
with open("tsb_prompt.txt", "r") as file:
    prompt_template = file.read()

output_folder = "Tsbs"
os.makedirs(output_folder, exist_ok=True)

for i, log in enumerate(repair_logs, start=1):
    print(f"Processing repair log #{i}...")

    try:
        tsb = generate_tsb_with_ollama(log, prompt_template)
    except Exception as e:
        print(f"Failed to generate TSB for log #{i}: {e}")
        continue

    output_path = os.path.join(output_folder, f"tsb_batch_{i}.md")
    with open(output_path, "w") as out_file:
        out_file.write(tsb)

    print(f"Saved TSB #{i} to {output_path}\n")

