import os
import sys

import pandas as pd

sys.path.append(os.path.relpath("First-Come-First-Serve-scheduling"))
sys.path.append(os.path.relpath("Priority-Scheduling"))
sys.path.append(os.path.relpath("Round-Robin-scheduling"))
sys.path.append(os.path.relpath("Shortest-Job-First-scheduling"))

from FCFS import simulate_fcfs_algorithm
from SJF_np import simulate_sjf_np_algorithm
from SJF_p import simulate_sjf_p_algorithm
from RR import simulate_rr_algorithm
from priority_p import simulate_priority_p_algorithm
from priority_np import simulate_priority_np_algorithm

if __name__ == "__main__":
    # read data
    data = pd.read_csv("db/data_set.csv")

    # fcfs algorithm
    simulate_fcfs_algorithm(data)

    # sjf non preemptive algorithm
    simulate_sjf_np_algorithm(data)

    # sjf preemptive algorithm
    simulate_sjf_p_algorithm(data)

    # round robin preemptive algorithm
    quantum = 1
    simulate_rr_algorithm(data, quantum)

    # priority non preemptive algorithm
    simulate_priority_np_algorithm(data)

    # priority preemptive algorithm
    simulate_priority_p_algorithm(data)
