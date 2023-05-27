# Priority Scheduling Algorithms

This directory contains two different CPU scheduling algorithms implemented in Python: Priority Non-Preemptive and
Priority Preemptive. These algorithms are designed to schedule processes based on their priority levels, where
higher-priority processes are executed first. These algorithms are useful in real-time systems and applications where
response time is critical.

## Getting Started

The algorithms are implemented in three different Python files:

* `cpu_time_unit.py`: A utility file for calculating the CPU time unit used in the algorithms.
* `priority_np.py`: The Priority Non-Preemptive algorithm implementation.
* `priority_p.py`: The Priority Preemptive algorithm implementation.

The algorithms require Python version 3.x and the following libraries:

* `queue`
* `pandas`
* `cpu_time_unit`

To run the algorithms, clone this repository and execute the following command:

```
python priority_np.py
```

Or

```
python priority_p.py
```

## CPU Time Unit

The `cpu_time_unit.py` file contains a function for calculating the CPU time unit used in both algorithms. The CPU time
unit is a measure of how long one unit of CPU time takes to execute. The `get_cpu_time_unit()` function calculates the
CPU time unit by running a loop that performs a simple mathematical operation 10,000times and measures the time it takes
to complete. This value is then used to calculate the execution time of the algorithms.

## Priority Non-Preemptive Algorithm

The Priority Non-Preemptive algorithm is a CPU scheduling algorithm that selects the process with the highest priority
level from the ready queue and executes it until completion. This process continues until all processes have been
completed. If two processes have the same priority level, the algorithm uses the First-Come-First-Serve (FCFS)
scheduling policy.

The `priority_np.py` file contains the implementation of the Priority Non-Preemptive algorithm. The algorithm sorts
processes based on their arrival time and uses a priority queue to manage the ready queue. The algorithm then selects
the process with the highest priority level from the ready queue and executes it until completion. The algorithm
calculates the completion time, turnaround time, waiting time, and response time for each process and returns various
performance metrics for the algorithm.

## Priority Preemptive Algorithm

The Priority Preemptive algorithm is a CPU scheduling algorithm that selects the process with the highest priority level
from the ready queue and executes it. If a new process arrives with a higher priority level than the currently executing
process, the currently executing process is preempted and added back to the ready queue. This process continues until
all processes have been completed.

The `priority_p.py` file contains the implementation of the Priority Preemptive algorithm. The algorithm sorts processes
based on their arrival time and uses a priority queue to manage the ready queue. The algorithm then selects the process
with the highest priority level from the ready queue and executes it. If a new process arrives with a higher priority
level than the currently executing process, the currently executing process is preempted and added back to the ready
queue. The algorithm calculates the completion time, turnaround time, waiting time, and response time for each process
and returns various performance metrics for the algorithm.

## Performance Metrics

Both algorithms calculate the following performance metrics:

* Throughput: the number of processes completed per unit of time.
* CPU utilization: the percentage of time the CPU was busy executing processes.
* Average Turnaround Time: the amount of time it takes for a process to complete from the moment it enters the system
  until its completion.
* Average Waiting Time: the amount of time a process waits in the ready queue before being executed.
* Average Response Time: the amount of time a process waits in the ready queue before being executed for the first time.

## Conclusion

Both Priority Non-Preemptive and Priority Preemptive algorithms are useful in situations where minimizing the turnaround
time and improving the response time is crucial. However, these algorithms can suffer from starvation, where a process
with a low priority level may be stuck waiting indefinitely behind other higher-priority tasks. The selection of the
appropriate scheduling algorithm depends on the specific requirements of the system or application.