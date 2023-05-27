import numpy as np
import pandas as pd


def generate_process():
    print('---Process Generator---')
    n = int(input('Please insert the number of precesses: '))

    burst_time = np.random.randint(low=1, high=10, size=n)
    burst_time = np.ceil(burst_time).astype(int)
    arrival_time = np.arange(0, 2*n, 2)
    process_id = np.arange(1, n + 1)
    priority = process_id.copy()
    np.random.shuffle(priority)

    csv_data = np.stack(
        (process_id, arrival_time, priority, burst_time), axis=0)

    data_csv = pd.DataFrame(csv_data).T.set_axis(
        ["process_id", "arrival_time", "priority", "burst_time"], axis="columns"
    )
    data_csv.to_csv("db/data_set.csv", index=False)
    print(f'{n} process generated in csv file successfully!')


if __name__ == '__main__':
    generate_process()
