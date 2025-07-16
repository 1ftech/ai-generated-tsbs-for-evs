# generate_cluster_tsbs.py

import os
from tsb_generator import generate_tsb_with_ollama

# Paths
cluster_dir = "clustered_logs"
output_dir = "Tsbs"
prompt_path = "tsb_prompt.txt"

os.makedirs(output_dir, exist_ok=True)

# Load prompt template
with open(prompt_path, "r") as file:
    prompt_template = file.read()

# Process each cluster file
for filename in os.listdir(cluster_dir):
    if not filename.endswith(".txt"):
        continue

    cluster_path = os.path.join(cluster_dir, filename)

    with open(cluster_path, "r") as file:
        cluster_logs = file.read().strip()

    print(f"🔧 Generating TSB for {filename}...")

    try:
        tsb = generate_tsb_with_ollama(cluster_logs, prompt_template)
    except Exception as e:
        print(f"❌ Error generating TSB for {filename}: {e}")
        continue

    tsb_filename = filename.replace(".txt", ".md")
    tsb_path = os.path.join(output_dir, tsb_filename)

    with open(tsb_path, "w") as file:
        file.write(tsb)

    print(f"✅ Saved: {tsb_path}\n")
