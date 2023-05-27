from cpu_time_unit import get_cpu_time_unit

idle_time = 0


def calculate_waiting_time(processes, n, burst_t, waiting_t, quantum):
    global idle_time
    # Copy the burst time into remaining burst
    remain_bt = burst_t.copy()

    t = 0

    while True:
        done = True
        for i in range(n):
            if remain_bt[i] > 0:
                done = False
                if remain_bt[i] > quantum:
                    t += quantum
                    remain_bt[i] -= quantum

                else:
                    t += remain_bt[i]
                    waiting_t[i] = t - burst_t[i]
                    remain_bt[i] = 0

            if waiting_t[i] < 0:
                idle_time += abs(waiting_t[i])
                waiting_t[i] = 0

        # If all processes are done
        if done:
            break


def calculate_turnaround_time(processes, n, burst_t, waiting_t, turn_around_t):
    for i in range(n):
        turn_around_t[i] = burst_t[i] + waiting_t[i]


def calculate_response_time(n, burst_t, quantum):
    response_t = 0
    response_t_arr = []
    for i in range(n):
        if i == 0:
            response_t = 0
        else:
            if quantum >= burst_t[i - 1]:
                response_t += burst_t[i - 1]
                response_t_arr.append(response_t)
            else:
                response_t += quantum
                response_t_arr.append(response_t)
    return (sum(response_t_arr) * get_cpu_time_unit()) / n


def simulate_rr_algorithm(data, quantum):
    processes = data['process_id']
    n = len(processes)
    burst_time = data['burst_time']
    waiting_t = [0] * n
    turn_around_t = [0] * n

    calculate_waiting_time(processes, n, burst_time, waiting_t, quantum)
    calculate_turnaround_time(processes, n, burst_time, waiting_t, turn_around_t)

    total_waiting_t = sum(waiting_t)
    total_turn_around_t = sum(turn_around_t)
    total_burst_t = sum(burst_time)
    cpu_utilization = total_burst_t / (total_burst_t + idle_time)
    throughput = n / ((total_burst_t + idle_time) * get_cpu_time_unit())
    average_waiting_time = (total_waiting_t * get_cpu_time_unit()) / n
    average_turnaround_time = (total_turn_around_t * get_cpu_time_unit()) / n
    avg_response_t = calculate_response_time(n, burst_time, quantum)

    print('RR preemptive algorithm results: ')
    print("Throughput = %.4f" % throughput)
    print(f"CPU utilization = {'%.2f' % cpu_utilization}")
    print("Average waiting time = %.4f " % average_waiting_time)
    print("Average turn around time = %.4f " % average_turnaround_time)
    print("Average response time = %.4f \n" % avg_response_t)

    return {
        'n': str(n),
        'throughput': "%.4f" % throughput,
        'cpu_util': "%.2f" % cpu_utilization,
        'awt': "%.4f" % average_waiting_time,
        'att': "%.4f" % average_turnaround_time,
        'art': "%.4f" % avg_response_t
    }
