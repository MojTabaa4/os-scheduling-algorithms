from cpu_time_unit import get_cpu_time_unit

idle_time = 0


def calculate_waiting_time(n, burst_t, waiting_t, arrival_t):
    global idle_time
    service_time = [0] * n

    for i in range(1, n):
        service_time[i] = (service_time[i - 1] + burst_t[i - 1])
        waiting_t[i] = service_time[i] - arrival_t[i]

        # If waiting time for a process is in
        # negative that means it is already
        # in the ready queue before CPU becomes
        # idle so its waiting time is 0
        if waiting_t[i] < 0:
            idle_time += abs(waiting_t[i])
            waiting_t[i] = 0


def calculate_turnaround_time(n, burst_t, waiting_t, turn_around_t):
    for i in range(n):
        turn_around_t[i] = burst_t[i] + waiting_t[i]


def simulate_fcfs_algorithm(data):
    data = data.sort_values('arrival_time')
    processes = data['process_id']
    n = len(processes)
    burst_time = data['burst_time']
    arrival_time = data['arrival_time']
    waiting_t = [0] * n
    turn_around_t = [0] * n

    calculate_waiting_time(n, burst_time, waiting_t, arrival_time)

    calculate_turnaround_time(n, burst_time, waiting_t, turn_around_t)

    total_waiting_t = sum(waiting_t)
    total_turn_around_t = sum(turn_around_t)
    total_burst_t = sum(burst_time)
    cpu_utilization = total_burst_t / (total_burst_t + idle_time)
    throughput = n / ((total_burst_t + idle_time) * get_cpu_time_unit())
    average_waiting_time = (total_waiting_t * get_cpu_time_unit()) / n
    average_turnaround_time = (total_turn_around_t * get_cpu_time_unit()) / n

    print('FCFS algorithm results:')
    print("Throughput = %.4f" % throughput)
    print(f"CPU utilization = {'%.2f' % cpu_utilization}")
    print("Average waiting time = %.4f" % (average_waiting_time))
    print("Average turn around time = %.4f" % (average_turnaround_time))
    print("Average response time = %.4f \n" % (average_waiting_time))

    return {
        'n': str(n),
        'throughput': "%.4f" % throughput,
        'cpu_util': "%.2f" % cpu_utilization,
        'awt': "%.4f" % (average_waiting_time),
        'att': "%.4f" % (average_turnaround_time),
        'art': "%.4f" % (average_waiting_time)
    }
