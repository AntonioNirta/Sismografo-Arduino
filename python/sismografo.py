# Code written by Antonio Nirta

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Import csv file. "LOG(5).csv" is the name of file
    db = pd.read_csv("LOG(5).csv")

    # Variables with accelerations
    AcX = db.iloc[:, 0]
    AcY = db.iloc[:, 1]
    AcZ = db.iloc[:, 2]

    # Time settings
    arduino_time = db.iloc[:, 3]  # time in milliseconds, give by arduino

    converted_time = [i/1000 for i in arduino_time]  # time in seconds

    # Create plots with pre-defined labels.
    fig, ax = plt.subplots()

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
    plt.show()


if __name__ == '__main__':
    main()
