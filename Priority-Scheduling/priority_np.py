from queue import PriorityQueue
from cpu_time_unit import get_cpu_time_unit

n: int
idle_time = 0


def insert_ready_queue(ready_queue, normal_queue, s_time, e_time):
    if normal_queue:
        for value in normal_queue.values():
            if e_time < value['arrival_time'] <= s_time:
                ready_queue.put((value['priority'],
                                 value['burst_time'],
                                 value['arrival_time'],
                                 value['process_id']))
    return ready_queue


def simulate_priority_np_algorithm(process_data):
    global n
    global idle_time
    s_time = 0
    e_time = -1

    process_data['et'] = 0
    process_data['tat'] = 0
    # Sort processes according to the Arrival Time
    process_data = process_data.sort_values('arrival_time')
    normal_queue = process_data.to_dict(orient="index")
    n = len(normal_queue)
    ready_queue = PriorityQueue()
    while True:

        ready_queue = insert_ready_queue(ready_queue, normal_queue, s_time, e_time)

        if not ready_queue.empty():
            process = ready_queue.get()

            e_time = s_time
            s_time += process[1]
            k = process[3] - 1
            del normal_queue[k]
            process_data.at[k, 'et'] = s_time

        elif len(normal_queue) != 0:
            first_index = next(iter(normal_queue))
            if s_time < normal_queue[first_index]['arrival_time']:
                idle_time += normal_queue[first_index]['arrival_time'] - s_time
                s_time = normal_queue[first_index]['arrival_time']
            e_time = s_time
            s_time += normal_queue[first_index]['burst_time']
            k = normal_queue[first_index]['process_id'] - 1
            del normal_queue[k]
            process_data.at[k, 'et'] = s_time

        elif not normal_queue and ready_queue.empty():
            break

    t_time = calculate_turnaround_time(process_data)
    w_time = calculate_waiting_time(process_data)

    return printData(process_data, t_time, w_time)


def calculate_turnaround_time(process_data):
    total_turnaround_time = 0
    for i in range(n):
        # turnaround_time = completion_time - arrival_time
        turnaround_time = process_data.at[i, 'et'] - process_data.at[i, 'arrival_time']
        total_turnaround_time += turnaround_time
        process_data.at[i, 'tat'] = turnaround_time
    average_turnaround_time = (total_turnaround_time * get_cpu_time_unit()) / n

    return average_turnaround_time


def calculate_waiting_time(process_data):
    total_waiting_time = 0
    for i in range(n):
        # waiting_time = turnaround_time - burst_time
        waiting_time = process_data.at[i, 'tat'] - process_data.at[i, 'burst_time']
        total_waiting_time += waiting_time
    average_waiting_time = (total_waiting_time * get_cpu_time_unit()) / n

    return average_waiting_time


def printData(process_data, average_turnaround_time, average_waiting_time):
    total_burst_t = process_data['burst_time'].sum(axis=0)
    cpu_utilization = total_burst_t / (total_burst_t + idle_time)
    throughput = n / ((total_burst_t + idle_time) * get_cpu_time_unit())

    print('Priority non preemptive algorithm results: ')
    print("Throughput = %.4f" % throughput)
    print(f"CPU utilization = {cpu_utilization}")
    print(f'Average waiting time = {"%.2f" % average_waiting_time}')
    print(f'Average turn around time = {"%.2f" % average_turnaround_time}')
    print(f'Average response time = {"%.2f" % average_waiting_time}\n')

    return {
        'n': str(n),
        'throughput': "%.4f" % throughput,
        'cpu_util': "%.2f" % cpu_utilization,
        'awt': "%.4f" % average_waiting_time,
        'att': "%.4f" % average_turnaround_time,
        'art': "%.4f" % average_waiting_time
    }
