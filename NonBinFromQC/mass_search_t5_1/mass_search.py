import os
from pathlib import Path

# Parameters to vary
q_values = [2, 3,5,7]        # Field sizes GF(q)
n_values = [i for i in range (6,20,2)]     # Half the classical code length (total length = 2n)
k_values = [2,3, 4, 5,6]      # Code dimension

# Base directory
base_dir = "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_1"
template_file = os.path.join(base_dir, "symp.m")
input_dir = os.path.join(base_dir, "Input")
log_dir = os.path.join(base_dir, "Logs")
utilities_dir = os.path.join(base_dir, "Utilities")
run_script = os.path.join(utilities_dir, "run_all.sh")
pids_file = os.path.join(utilities_dir, "PIDS")

# Ensure all directories exist
Path(input_dir).mkdir(parents=True, exist_ok=True)
Path(log_dir).mkdir(parents=True, exist_ok=True)
Path(utilities_dir).mkdir(parents=True, exist_ok=True)

# Load the Magma template
with open(template_file, 'r') as f:
    template = f.read()

jobs = []

# Generate Magma files
for q in q_values:
    for n in n_values:
        for k in k_values:
            name = f"q{q}_n{n}_k{k}.m"
            path = os.path.join(input_dir, name)
            log = os.path.join(log_dir, f"q{q}_n{n}_k{k}.log")
            filled = template.replace("{Q}", str(q)).replace("{N}", str(n)).replace("{K}", str(k))
            with open(path, 'w') as f:
                f.write(filled)
            jobs.append((path, log))

# Generate run_all.sh
with open(run_script, 'w') as f:
    f.write("#!/bin/bash\n\n")
    f.write(f"echo '' > \"{pids_file}\"\n\n")
    for script, log in jobs:
        f.write(f"(nohup /usr/bin/time -v magma \"{script}\" > \"{log}\" 2>&1 & echo $! >> \"{pids_file}\") &\n")
    f.write("wait\n")

os.chmod(run_script, 0o755)
print("Symplectic quantum code search scripts and run_all.sh created.")
