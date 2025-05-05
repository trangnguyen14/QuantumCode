import os
from pathlib import Path

# Parameters to vary
q_values = [2,3,4,5]                   # Field size (GF(q^2))
n_values = [i for i in range (10,80,10)]                # Code lengths

base_dir = "/home/nguyen7/QuantumCode/QECC_FromQT/auto_run_theorem_3"
template_file = os.path.join(base_dir, "hermitian_template.m")
input_dir = os.path.join(base_dir, "Input")
log_dir = os.path.join(base_dir, "Logs")
utilities_dir = os.path.join(base_dir, "Utilities")
run_all_script = os.path.join(utilities_dir, "run_all.sh")
pids_file = os.path.join(utilities_dir, "PIDS")

# Create necessary directories
Path(input_dir).mkdir(parents=True, exist_ok=True)
Path(log_dir).mkdir(parents=True, exist_ok=True)
Path(utilities_dir).mkdir(parents=True, exist_ok=True)

# Read the Magma template
with open(template_file, 'r') as f:
    template = f.read()

# Generate Magma input files
jobs = []
for q in q_values:
    for n in n_values:
        script_name = f"q{q}_n{n}.m"
        script_path = os.path.join(input_dir, script_name)
        script_content = template.replace("{Q}", str(q)).replace("{N}", str(n))
        with open(script_path, 'w') as f:
            f.write(script_content)
        jobs.append((script_path, os.path.join(log_dir, f"q{q}_n{n}.log")))

# Generate run_all.sh
with open(run_all_script, 'w') as f:
    f.write("#!/bin/bash\n\n")
    f.write(f"echo '' > {pids_file}\n\n")
    for script_path, log_path in jobs:
        f.write(f"(nohup /usr/bin/time -v magma {script_path} > {log_path} 2>&1 & echo $! >> {pids_file}) &\n")
    f.write("wait\n")

# Make the run_all.sh script executable
os.chmod(run_all_script, 0o755)

print("Hermitian code search scripts and runner created.")
