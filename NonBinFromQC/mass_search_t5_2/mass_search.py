import os
from pathlib import Path

# Parameters to vary
q_values = [2, 3,5,7]        # Field sizes GF(q)
n_values = [i for i in range (6,20,2)]     # Half the classical code length (total length = 2n)
k_values = [2,3, 4, 5,6]      # Code dimension

# Directories
base_dir = "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2"
template_file = os.path.join(base_dir, "symp.m")
input_dir = os.path.join(base_dir, "Input")
log_dir = os.path.join(base_dir, "Logs")
utilities_dir = os.path.join(base_dir, "Utilities")
run_script = os.path.join(utilities_dir, "run_all.sh")
pids_file = os.path.join(utilities_dir, "PIDS")

# Create folders
Path(input_dir).mkdir(parents=True, exist_ok=True)
Path(log_dir).mkdir(parents=True, exist_ok=True)
Path(utilities_dir).mkdir(parents=True, exist_ok=True)

# Read template
with open(template_file, 'r') as f:
    template = f.read()

jobs = []

# Generate Magma files
for q in q_values:
    for n in n_values:
        for k in k_values:
            if k < n:
                continue  # Skip invalid dimensions
            script_name = f"q{q}_n{n}_k{k}.m"
            script_path = os.path.join(input_dir, script_name)
            log_path = os.path.join(log_dir, f"q{q}_n{n}_k{k}.log")
            content = template.replace("{Q}", str(q)).replace("{N}", str(n)).replace("{K}", str(k))
            with open(script_path, 'w') as f:
                f.write(content)
            jobs.append((script_path, log_path))

# Generate run_all.sh
with open(run_script, 'w') as f:
    f.write("#!/bin/bash\n\n")
    f.write(f"echo '' > \"{pids_file}\"\n\n")
    for script_path, log_path in jobs:
        f.write(f"(nohup /usr/bin/time -v magma \"{script_path}\" > \"{log_path}\" 2>&1 & echo $! >> \"{pids_file}\") &\n")
    f.write("wait\n")

os.chmod(run_script, 0o755)

print("Symplectic Theorem 5.2 search scripts and run_all.sh created.")
