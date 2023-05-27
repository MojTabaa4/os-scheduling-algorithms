# CPU scheduling algorithms simulator
## Introduction

The CPU scheduling algorithms simulator is a project that simulates different CPU scheduling algorithms using Python.
The project includes a Graphical User Interface (GUI) that allows the user to select the algorithm, view the results on
the screen, and visualize the results in a chart. The project uses four different algorithms: First Come, First Served (
FCFS), Shortest Job First (SJF), Round Robin (RR), and Priority.

## Directory Structure

The project has four directories, each containing a Python file that implements a specific algorithm. The directories
are:

- [First-Come-First-Serve-scheduling](https://github.com/MojTabaa4/os-scheduling-algorithms/tree/main/First-Come-First-Serve-scheduling)
- [Priority-Scheduling](https://github.com/MojTabaa4/os-scheduling-algorithms/tree/main/Priority-Scheduling)
- [Round-Robin-scheduling](https://github.com/MojTabaa4/os-scheduling-algorithms/tree/main/Round-Robin-scheduling)
- [Shortest-Job-First-scheduling](https://github.com/MojTabaa4/os-scheduling-algorithms/tree/main/Shortest-Job-First-scheduling)

Each of these directories contains a README file that explains the algorithm and how it is implemented.

## Files

The project has three main Python files:

### `main.py`

This file is the entry point to the simulation. It imports the algorithms from the corresponding directories and reads
the process data from a CSV file. Then, it calls the simulation function for each algorithm and prints the results on
the screen.

### `main_ui.py`

This file contains the implementation of the GUI interface using the tkinter library. The user can select the algorithm
to simulate from the buttons on the home page. The GUI then displays the results on the screen, and the user can
visualize the results in a chart.

### `process_generator.py`

This file contains a function to generate a CSV file containing the process data for the simulation. The user can specify
the number of processes to generate, and the function will generate random values for the arrival time, priority, and
burst time of each process.

## Algorithms

### First Come, First Served (FCFS)

The FCFS algorithm is a non-preemptive algorithm where the processes are executed in the order they arrive in the ready
queue. The process with the lowest arrival time is executed first, and the CPU is not released until the process
completes. This algorithm is simple and easy to implement, but it suffers from the problem of convoy effect, where a
long process can hold the CPU, causing other short processes to wait.

### Shortest Job First (SJF)

The SJF algorithm is a non-preemptive algorithm where the processes are executed in order of their burst time. The
process with the shortest burst time is executed first, and the CPU is not released until the process completes. This
algorithm reduces the waiting time and turnaround time of the processes, but it suffers from the problem of starvation,
where a long process can keep waiting for the CPU if shorter processes keep arriving.

### Round Robin (RR)

The RR algorithm is a preemptive algorithm where each process is executed for a fixed time slice. When the time slice
expires, the CPU is released, and the next process in the ready queue is executed. This algorithm ensures that every
process gets a fair share of the CPU, but it suffers from the problem of high context switching overhead, which can
reduce the overall performance of the system.

### Priority Scheduling

The priority scheduling algorithm is a non-preemptive algorithm where each process is assigned a priority, and the
process with the highest priority is executed first. If two processes have the same priority, then the FCFS algorithm is
used to break the tie. This algorithm ensures that high-priority processes are executed first, but it suffers from the
problem of starvation, where low-priority processes may have to wait indefinitely if high-priority processes keep
arriving.

## GUI Interface

The GUI interface is implemented in the `main_ui.py` file using the tkinter library. The interface has two main pages:
the home page and the results page.

### Home Page

The home page contains buttons for each algorithm, and the user can select the algorithm to simulate by clicking the
corresponding button. The home page also has a button to exit the application.

### Results Page

The results page displays the results of the simulation on the screen. The page shows the average waiting time, average
turnaround time, and average response time for the selected algorithm. The results page also has a button to visualize
the results in a chart and a back button to return to the home page.

### Chart Page

The chart page displays a chart that visualizes the results of the simulation. The chart shows the waiting time,
turnaround time, and response time for each process. The chart page has a back button to return to the results page.

## How to use

To use the project, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the `process_generator.py` file to generate the process data CSV file. Specify the number of processes to
   generate when prompted.
4. Run the `main_ui.py` file to open the GUI interface.
5. Select the algorithm to simulate from the buttons on the home page.
6. View the results on the screen. The results page displays the average waiting time, average turnaround time, and
   average response time for the selected algorithm.
7. Click the "Chart" button to visualize the results in a chart. The chart page displays a chart that shows the waiting
   time, turnaround time, and response time for each process.
8. Click the "Back" button to return to the results page and view the results for another algorithm.
9. Click the "Exit" button on the home page to exit the application.

Note: Make sure you have the required Python packages installed, such as pandas and matplotlib. You can install them
using pip. Also, the project assumes that the process data is stored in a CSV file with the following columns: "Process
ID", "Arrival Time", "Priority", and "Burst Time". If your data is stored in a different format, you will need to modify
the code accordingly.