## Shortest Job First (SJF) Algorithm

This directory contains two Python implementations of the SJF algorithm for CPU scheduling: `SJF.py` for preemptive SJF
and `SJF_np.py` for non-preemptive SJF. Both implementations use the `PriorityQueue` data structure from the `queue`
module to manage the ready queue.

The `cpu_time_unit.py` file contains a utility function for calculating the CPU time unit, which is used in both
implementations.

### Running the Algorithm

To run the SJF algorithm, you can import the `simulate_sjf_p_algorithm()` function from `SJF.py` for preemptive SJF or
the `simulate_sjf_np_algorithm()` function from `SJF_np.py` for non-preemptive SJF and pass in a pandas DataFrame
containing the process ID, arrival time, and burst time for each process. The function will return a dictionary
containing various performance metrics for the algorithm.

```python
import pandas as pd
from SJF import simulate_sjf_p_algorithm
from SJF_np import simulate_sjf_np_algorithm

# create a pandas DataFrame with process ID, arrival time, and burst time
data = pd.DataFrame({
    'process_id': [1, 2, 3, 4],
    'arrival_time': [0, 1, 2, 3],
    'burst_time': [5, 4, 3, 2]
})

# run theSJF algorithm with preemptive or non-preemptive mode on the data
results_p = simulate_sjf_p_algorithm(data)
results_np = simulate_sjf_np_algorithm(data)

# print the results
print(results_p)
print(results_np)
```

The output will be a dictionary containing the following performance metrics:

- `n`: the number of processes
- `throughput`: the throughput of the system
- `cpu_util`: the CPU utilization of the system
- `awt`: the average waiting time of the processes
- `att`: the average turnaround time of the processes
- `art`: the average response time of the processes

### CPU Time Unit

The `cpu_time_unit.py` file contains a utility function for calculating the CPU time unit. The `get_cpu_time_unit()`
function uses the `timeit.default_timer()` function to measure the time it takes to perform a simple calculation. This
time is used as the CPU time unit for the SJF algorithm.

```python
from cpu_time_unit import get_cpu_time_unit

# get the CPU time unit
cpu_time_unit = get_cpu_time_unit()

# print the CPU time unit
print(cpu_time_unit)
```

The output will be the CPU time unit, which represents the amount of time it takes for the CPU to perform a single unit
of work.

### Dependencies

The SJF algorithm implementations require the `pandas` library to be installed. You can install it using pip:

```
pip install pandas
```

### References

- [Shortest Job First (SJF) Scheduling Algorithm](https://www.geeksforgeeks.org/shortest-job-first-scheduling-algorithm/)
  by Geeks for Geeks
- [Priority Queue in Python](https://www.geeksforgeeks.org/priority-queue-in-python/) by Geeks for Geeks