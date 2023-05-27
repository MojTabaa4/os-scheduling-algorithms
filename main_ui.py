import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style

import pandas as pd
import matplotlib.pyplot as plt

sys.path.append(os.path.relpath("First-Come-First-Serve-scheduling"))
sys.path.append(os.path.relpath("Priority-Scheduling"))
sys.path.append(os.path.relpath("Round-Robin-scheduling"))
sys.path.append(os.path.relpath("Shortest-Job-First-scheduling"))

from FCFS import simulate_fcfs_algorithm
from RR import simulate_rr_algorithm
from SJF_np import simulate_sjf_np_algorithm
from SJF_p import simulate_sjf_p_algorithm
from priority_np import simulate_priority_np_algorithm
from priority_p import simulate_priority_p_algorithm


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        style = Style()
        style.configure('TButton',
                        background='blue',
                        foreground='white',
                        font=('Arial', 20, 'bold'),
                        borderwidth='4')

        style.configure('TLabel',
                        background='#081547',
                        foreground='white',
                        font=('Arial', 20, 'bold'),
                        borderwidth='4')

        style.map('TButton',
                  foreground=[('active', '!disabled', 'black')],
                  background=[('active', 'yellow')])
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, FCFS, SJF_np, SJF_p, RR, PriorityNP, PriorityP, Chart):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='#081547')

        label = ttk.Label(self, text="CPU Scheduling algorithms simulator", font=LARGE_FONT)
        label.place(x=0, y=0)

        button1 = ttk.Button(self, text="FCFS", command=lambda: controller.show_frame(FCFS))
        button1.place(x=50, y=100)

        button2 = ttk.Button(self, text="SJF NP", command=lambda: controller.show_frame(SJF_np))
        button2.place(x=300, y=100)

        button3 = ttk.Button(self, text="SJF P", command=lambda: controller.show_frame(SJF_p))
        button3.place(x=50, y=200)

        button4 = ttk.Button(self, text="RR", command=lambda: controller.show_frame(RR))
        button4.place(x=300, y=200)

        button5 = ttk.Button(self, text="Priority NP", command=lambda: controller.show_frame(PriorityNP))
        button5.place(x=50, y=300)

        button6 = ttk.Button(self, text="Priority P", command=lambda: controller.show_frame(PriorityP))
        button6.place(x=300, y=300)

        button7 = ttk.Button(self, text="Chart", command=lambda: controller.show_frame(Chart))
        button7.place(x=180, y=400)


def print_result(root, result):
    label = ttk.Label(root, text=f"Number of processes = {result['n']}", font=LARGE_FONT, foreground='yellow')
    label.place(x=20, y=100)
    label = ttk.Label(root, text=f"Throughput = {result['throughput']}", font=LARGE_FONT, foreground='yellow')
    label.place(x=20, y=150)
    label = ttk.Label(root, text=f"CPU utilization = {result['cpu_util']}", font=LARGE_FONT, foreground='yellow')
    label.place(x=20, y=200)
    label = ttk.Label(root, text=f"Average waiting time = {result['awt']}", font=LARGE_FONT, foreground='yellow')
    label.place(x=20, y=250)
    label = ttk.Label(root, text=f"Average turn around time = {result['att']}", font=LARGE_FONT, foreground='yellow')
    label.place(x=20, y=300)
    label = ttk.Label(root, text=f"Average response time = {result['art']}", font=LARGE_FONT, foreground='yellow')
    label.place(x=20, y=350)


def set_data_for_chart(result):
    awt_arr.append(float(result['awt']))
    att_arr.append(float(result['att']))
    art_arr.append(float(result['art']))


class FCFS(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='#081547')
        label = ttk.Label(self, text="First Come First Served algorithm:", font=LARGE_FONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        result = simulate_fcfs_algorithm(data)
        set_data_for_chart(result)
        print_result(self, result)

        button1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.place(x=20, y=450)


class SJF_np(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='#081547')
        label = ttk.Label(self, text="SJF non-preemptive algorithm:", font=LARGE_FONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        result = simulate_sjf_np_algorithm(data)
        set_data_for_chart(result)
        print_result(self, result)

        button1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.place(x=20, y=450)


class SJF_p(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='#081547')
        label = ttk.Label(self, text="SJF preemptive algorithm:", font=LARGE_FONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        result = simulate_sjf_p_algorithm(data)
        set_data_for_chart(result)
        print_result(self, result)

        button1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.place(x=20, y=450)


class RR(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='#081547')
        label = ttk.Label(self, text="Round-Robin algorithm:", font=LARGE_FONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        result = simulate_rr_algorithm(data, 1)
        set_data_for_chart(result)
        print_result(self, result)

        button1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.place(x=20, y=450)


class PriorityNP(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='#081547')
        label = ttk.Label(self, text="Priority non-preemptive algorithm:", font=LARGE_FONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        result = simulate_priority_np_algorithm(data)
        set_data_for_chart(result)
        print_result(self, result)

        button1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.place(x=20, y=450)


class PriorityP(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='#081547')
        label = ttk.Label(self, text="Priority preemptive algorithm:", font=LARGE_FONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        result = simulate_priority_p_algorithm(data)
        set_data_for_chart(result)
        print_result(self, result)

        button1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.place(x=20, y=450)


class Chart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='#081547')
        label = ttk.Label(self, text="Chart:", font=LARGE_FONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        df = pd.DataFrame(
            {
                'avg_waiting_time': awt_arr,
                'avg_turnaround_time': att_arr,
                'avg_response_time': art_arr
            },
            index=['fcfs', 'sjf_np', 'sjf_p', 'rr', 'priority_np', 'priority_p']
        )
        print(df)

        def bar_plot():
            df.plot.bar(rot=0)
            plt.title('scheduling algorithms chart')
            plt.xlabel('algorithms')
            plt.ylabel('time(second)')
            plt.grid()
            plt.show()

        button = ttk.Button(self, text="show chart", command=bar_plot)
        button.place(x=190, y=240)

        button1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.place(x=20, y=450)


if __name__ == "__main__":
    data = pd.read_csv("db/data_set.csv")
    LARGE_FONT = ("Arial", 25)

    awt_arr = []
    att_arr = []
    art_arr = []

    app = tkinterApp()
    app.wm_geometry("600x500")
    app.title('CPU Scheduling Algorithms Simulator')
    app.resizable(False, False)
    app.mainloop()
