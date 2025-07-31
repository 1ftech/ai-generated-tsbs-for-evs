import os
#import sys
#from tsb_generator import generate_tsb_with_ollama

# ====== CONFIGURATION ======
MAX_LOGS = 1  # Change this to a higher number when ready (e.g., 5 or None for all)

# ====== MOCK FUNCTION INSTEAD OF OLLAMA ======
def generate_mock_tsb(log, prompt_template):
    return f"""## Technical Service Bulletin (Mocked)

**Issue Description:**  
{log}

**Root Cause:** Simulated analysis of the issue.

**Solution:** Suggested fix using standard procedures.

**Parts Required:** Placeholder parts.

**Notes:** This is a simulated output for demo purposes only.
"""


# ====== LOAD INPUT FILES ======
# Load repair logs (separated by two newlines)
with open("repair_logs_sample.txt", "r") as file:
    repair_logs = [log.strip() for log in file.read().split("\n\n") if log.strip()]

# Load prompt template
with open("tsb_prompt.txt", "r") as file:
    prompt_template = file.read()

# Create output folder
output_folder = "Tsbs"
os.makedirs(output_folder, exist_ok=True)

# ====== GENERATE MOCK TSBs ======
for i, log in enumerate(repair_logs, start=1):
    if MAX_LOGS is not None and i > MAX_LOGS:
        print("✅ Reached log processing limit. Exiting.")
        break

    print(f"🔧 Repair Log #{i}:\n{log}\n")

    try:
        tsb = generate_mock_tsb(log, prompt_template)
    except Exception as e:
        print(f"❌ Error generating TSB for Log #{i}: {e}")
        continue

    tsb_path = os.path.join(output_folder, f"tsb_{i}.md")
    with open(tsb_path, "w") as file:
        file.write(tsb)

    print(f"✅ Saved: {tsb_path}\n")

print("🎉 Mocked TSB generation complete.")

# ====== GENERATE TSBs ======
#for i, log in enumerate(repair_logs, start=1):
   # if MAX_LOGS is not None and i > MAX_LOGS:
      #  print("✅ Reached log processing limit. Exiting.")
      #  break

 #   print(f"🔧 Repair Log #{i}:\n{log}\n")

  #  try:
     #   tsb = generate_tsb_with_ollama(log, prompt_template)
  #  except Exception as e:
      #  print(f"❌ Error generating TSB for Log #{i}: {e}")
     #   continue

  #  tsb_path = os.path.join(output_folder, f"tsb_{i}.md")
  #  with open(tsb_path, "w") as file:
       # file.write(tsb)

  #  print(f"✅ Saved: {tsb_path}\n")

#print("🎉 TSB generation complete.")
