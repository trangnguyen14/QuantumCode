#!/bin/bash

echo '' > "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Utilities/PIDS"

(nohup /usr/bin/time -v magma "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Input/q2_n6_k6.m" > "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Logs/q2_n6_k6.log" 2>&1 & echo $! >> "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Utilities/PIDS") &
(nohup /usr/bin/time -v magma "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Input/q3_n6_k6.m" > "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Logs/q3_n6_k6.log" 2>&1 & echo $! >> "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Utilities/PIDS") &
(nohup /usr/bin/time -v magma "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Input/q5_n6_k6.m" > "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Logs/q5_n6_k6.log" 2>&1 & echo $! >> "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Utilities/PIDS") &
(nohup /usr/bin/time -v magma "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Input/q7_n6_k6.m" > "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Logs/q7_n6_k6.log" 2>&1 & echo $! >> "/home/nguyen7/QuantumCode/NonBinFromQC/mass_search_t5_2/Utilities/PIDS") &
wait
