import os
from pathlib import Path

# Parameter sweep: prime field q and length n
q_values = [2, 3, 4,5,7,8,9]             # Change these as needed
n_values = [i for i in range (40,80,2)]          # Code lengths

# Base directory
base_dir = "/home/nguyen7/QuantumCode/CyclicCode"
template_file = os.path.join(base_dir, "cyclic.m")
input_dir = os.path.join(base_dir, "Input")
log_dir = os.path.join(base_dir, "Logs")
utilities_dir = os.path.join(base_dir, "Utilities")
run_all_script = os.path.join(utilities_dir, "run_all.sh")
pids_file = os.path.join(utilities_dir, "PIDS")

# Create directories
Path(input_dir).mkdir(parents=True, exist_ok=True)
Path(log_dir).mkdir(parents=True, exist_ok=True)
Path(utilities_dir).mkdir(parents=True, exist_ok=True)

# Read Magma template
with open(template_file, 'r') as f:
    template = f.read()

# Generate Magma scripts
jobs = []
for q in q_values:
    for n in n_values:
        filename = f"q{q}_n{n}.m"
        filepath = os.path.join(input_dir, filename)
        content = template.replace("{Q}", str(q)).replace("{N}", str(n))
        with open(filepath, 'w') as f:
            f.write(content)
        jobs.append((filepath, os.path.join(log_dir, f"q{q}_n{n}.log")))

# Write run_all.sh script
with open(run_all_script, 'w') as f:
    f.write("#!/bin/bash\n\n")
    f.write(f"echo '' > \"{pids_file}\"\n\n")
    for script_path, log_path in jobs:
        f.write(f"(nohup /usr/bin/time -v magma \"{script_path}\" > \"{log_path}\" 2>&1 & echo $! >> \"{pids_file}\") &\n")
    f.write("wait\n")

os.chmod(run_all_script, 0o755)
print("CSS dual code search scripts and runner created.")
