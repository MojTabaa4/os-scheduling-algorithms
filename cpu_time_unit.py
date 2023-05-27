from timeit import default_timer as timer

CPU_TIME_UNIT = None


def calculate():
    start = timer()
    for i in range(1, 10_000):
        if i % 2 == 0:
            temp = i / 2
        else:
            temp = 2 * i
    end = timer()
    return end - start


def get_cpu_time_unit():
    global CPU_TIME_UNIT
    if not CPU_TIME_UNIT:
        CPU_TIME_UNIT = calculate()
    return CPU_TIME_UNIT
