## Round Robin Algorithm

This directory contains a Python implementation of the Round Robin (RR) algorithm for CPU scheduling. The `RR.py` file
contains the implementation of the algorithm, and the `cpu_time_unit.py` file contains a utility function for
calculating the CPU time unit.

### Running the Algorithm

To run the RR algorithm, you can import the `simulate_rr_algorithm()` function from the `RR.py` file and pass in a
pandas DataFrame containing the process ID and burst time for each process, as well as the time quantum. The function
will return a dictionary containing various performance metrics for the algorithm.

```python
import pandas as pd
from RR import simulate_rr_algorithm

# create a pandas DataFrame with process ID and burst time
data = pd.DataFrame({
    'process_id': [1, 2, 3, 4],
    'burst_time': [5, 4, 3, 2]
})

# run the RR algorithm on the data with a time quantum of 2
results = simulate_rr_algorithm(data, 2)

# print the results
print(results)
```

The output will be a dictionary containing the following performance metrics:

- `n`: the number of processes
- `throughput`: the throughput of the system
- `cpu_util`: the CPU utilization of the system
- `awt`: the average waiting time of the processes
- `att`: the average turnaround time of the processes
- `art`:the average response time of the processes

### CPU Time Unit

The `cpu_time_unit.py` file contains a utility function for calculating the CPU time unit. The `get_cpu_time_unit()`
function uses the `timeit.default_timer()` function to measure the time it takes to perform a simple calculation. This
time is used as the CPU time unit for the RR algorithm.

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

The RR algorithm implementation requires the `pandas` library to be installed. You can install it using pip:

```
pip install pandas
```

### Preemptive SJF Algorithm

The Preemptive SJF algorithm is a CPU scheduling algorithm that selects the process with the shortest burst time from
the ready queue and executes it. If a new process arrives with a shorter burst time than the currently executing
process, the currently executing process is preempted and added back to the ready queue. This process continues until
all processes have been completed.

The `simulate_sjf_p_algorithm()` function in `SJF.py` implements the preemptive SJF algorithm using a `PriorityQueue` to
manage the ready queue. The function calculates the completion time, turnaround time, and waiting time for each process
and returns various performance metrics for the algorithm.

### Non-Preemptive SJF Algorithm

The Non-Preemptive SJF algorithm is a CPU scheduling algorithm that selects the process with the shortest burst time
from the ready queue and executes it until completion. This process continues until all processes have been completed.

The `simulate_sjf_np_algorithm()` function in `SJF_np.py` implements the non-preemptive SJF algorithm using
a `PriorityQueue` to manage the ready queue. The function calculates the completion time, turnaround time, and waiting
time for each process and returns various performance metrics for the algorithm.

Both algorithms are designed to minimize the average waiting time of the processes, making them useful in
situationswhere minimizing the turnaround time and improving the response time is crucial. However, these algorithms can
suffer from starvation, where a process with a long burst time may be stuck waiting indefinitely behind other shorter
tasks. Nonetheless, SJF algorithms are commonly used in real-time systems and applications where response time is
critical.

### Note

This implementation of the RR algorithm assumes that the processes are preemptive and that the burst times are sorted in
ascending order. If the burst times are not sorted, you should sort them before running the algorithm.