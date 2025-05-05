import os
from pathlib import Path

# Parameters to vary
q_values = [2, 3,5,7,9]
n_values = [i for i in range (10,40,5)]

# Paths
base_dir = "/home/nguyen7/QuantumCode/CC_CodesAxiom2014"
template_file = os.path.join(base_dir, "run.m")
input_dir = os.path.join(base_dir, "Input")
log_dir = os.path.join(base_dir, "Logs")
utilities_dir = os.path.join(base_dir, "Utilities")
run_script = os.path.join(utilities_dir, "run_all.sh")
pids_file = os.path.join(utilities_dir, "PIDS")

# Ensure directory structure
Path(input_dir).mkdir(parents=True, exist_ok=True)
Path(log_dir).mkdir(parents=True, exist_ok=True)
Path(utilities_dir).mkdir(parents=True, exist_ok=True)

# Read Magma template
with open(template_file, 'r') as f:
    template = f.read()

jobs = []

# Generate input files
for q in q_values:
    for n in n_values:
        script_name = f"q{q}_n{n}.m"
        script_path = os.path.join(input_dir, script_name)
        log_path = os.path.join(log_dir, f"q{q}_n{n}.log")
        content = template.replace("{Q}", str(q)).replace("{N}", str(n))
        with open(script_path, 'w') as f:
            f.write(content)
        jobs.append((script_path, log_path))

# Write run_all.sh
with open(run_script, 'w') as f:
    f.write("#!/bin/bash\n\n")
    f.write(f"echo '' > \"{pids_file}\"\n\n")
    for script, log in jobs:
        f.write(f"(nohup /usr/bin/time -v magma \"{script}\" > \"{log}\" 2>&1 & echo $! >> \"{pids_file}\") &\n")
    f.write("wait\n")

os.chmod(run_script, 0o755)

print("Theorem 6 CSS quantum code search scripts and runner created.")
