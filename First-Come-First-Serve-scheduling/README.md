## FCFS Algorithm

This directory contains a Python implementation of the First Come First Serve (FCFS) algorithm for CPU scheduling. The `FCFS.py` file contains the implementation of the algorithm, and the `cpu_time_unit.py` file contains a utility function for calculating the CPU time unit.

### Running the Algorithm

To run the FCFS algorithm, you can import the `simulate_fcfs_algorithm()` function from the `FCFS.py` file and pass in a pandas DataFrame containing the process ID, arrival time, and burst time for each process. The function will return a dictionary containing various performance metrics for the algorithm.

```python
import pandas as pd
from FCFS import simulate_fcfs_algorithm

# create a pandas DataFrame with process ID, arrival time, and burst time
data = pd.DataFrame({
    'process_id': [1, 2, 3, 4],
    'arrival_time': [0, 1, 2, 3],
    'burst_time': [5, 4, 3, 2]
})

# run the FCFS algorithm on the data
results = simulate_fcfs_algorithm(data)

# print the results
print(results)
```

The output will be a dictionary containing the following performance metrics:

- `n`: the number of processes
- `throughput`: the throughput of the system
- `cpu_util`: the CPU utilization of the system
- `awt`: the average waiting time of the processes
- `att`: the average turnaround time of the processes
- `art`: the average response time of the processes

### CPU Time Unit

The `cpu_time_unit.py` file contains a utility function for calculating the CPU time unit. The `get_cpu_time_unit()` function uses the `timeit.default_timer()` function to measure the time it takes to perform a simple calculation. This time is used as the CPU time unit for the FCFS algorithm.

```python
from cpu_time_unit import get_cpu_time_unit

# get the CPU time unit
cpu_time_unit = get_cpu_time_unit()

# print the CPU time unit
print(cpu_time_unit)
```

The output will be the CPU time unit, which represents the amount of time it takes for the CPU to perform a single unit of work.

### Dependencies

The FCFS algorithm implementation requires the `pandas` library to be installed. You can install it using pip:

```
pip install pandas
```

### Note

This implementation of the FCFS algorithm assumes that the arrival times of the processes are sorted in ascending order. If the arrival times are not sorted, you should sort them before running the algorithm.