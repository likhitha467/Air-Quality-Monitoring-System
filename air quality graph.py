

import csv
import matplotlib.pyplot as plt

times = []
values = []
statuses = []

# Read stored readings
with open("air_quality_readings.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        times.append(row["Time"])
        values.append(int(row["Gas_Value"]))
        statuses.append(row["Status"])

if len(values) == 0:
    print("No readings available.")
else:

    # Graph 1: Gas input readings
    plt.figure(figsize=(10, 5))

    plt.plot(
        range(1, len(values) + 1),
        values,
        marker="o",
        label="Gas Input"
    )

    plt.axhline(
        y=500,
        linestyle="--",
        label="Normal/Moderate boundary"
    )

    plt.axhline(
        y=750,
        linestyle="--",
        label="Moderate/High boundary"
    )

    plt.xlabel("Reading Number")
    plt.ylabel("Analog Input (0-1023)")
    plt.title("Air Quality Monitoring Simulation")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Graph 2: Status of readings
    plt.figure(figsize=(10, 5))

    plt.bar(
        range(1, len(values) + 1),
        values
    )

    plt.xlabel("Reading Number")
    plt.ylabel("Analog Input")
    plt.title("Recorded Air Quality Input Levels")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()
