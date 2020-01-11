# Code written by Antonio Nirta

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from tkinter import Tk, ttk, Menu, TOP as TKTOP, BOTH as TKBOTH
from tkinter.filedialog import askopenfilename


class Gui(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.title("Sismografo")
        self.master.minsize(640, 400)
        self.create_widgets()
        self.maximize()

    def quit(self):
        self.master.quit()
        self.master.destroy()

    def maximize(self):
        w = self.master.winfo_screenwidth()
        h = self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (w, h))

    def create_widgets(self):
        menubar = Menu(self.master)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Show CSV", command=self.fileDialog)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=menubar)

    def fileDialog(self):
        csv_file = askopenfilename(
            initialdir=Path.home(),
            title="Select A File",
            filetypes=(("csv", "*.csv"), )
            )
        if csv_file:
            self.show_graph(csv_file)

    def show_graph(self, csv_file):
        db = pd.read_csv(csv_file)

        # Variables with accelerations
        AcX = db.iloc[:, 0]
        AcY = db.iloc[:, 1]
        AcZ = db.iloc[:, 2]

        # Time settings
        arduino_time = db.iloc[:, 3]  # time in milliseconds, give by arduino

        converted_time = [i/1000 for i in arduino_time]  # time in seconds

        # Create plots with pre-defined labels.
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=self.master)

        ax.plot(converted_time, AcX, '-',
                color="red", linewidth=0.8, label='AcX')
        ax.plot(converted_time, AcY, '-',
                color="blue", linewidth=0.8, label='AcY')
        ax.plot(converted_time, AcZ, '-',
                color="green", linewidth=0.8, label='AcZ')

        legend = fig.legend(loc='upper right', shadow=True, fontsize='medium')

        # Axis' name
        plt.xlabel('Tempo (s)')
        plt.ylabel('Accelerazione')

        # Put a nicer background color on the legend.
        legend.get_frame().set_facecolor('white')

        # Show graph
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TKTOP, fill=TKBOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self.master)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TKTOP, fill=TKBOTH, expand=1)


def main():
    root = Tk()
    app = Gui(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
