
import csv
from datetime import datetime

filename = "air_quality_readings.csv"

print("AIR QUALITY MONITORING SYSTEM")
print("--------------------------------")

with open(filename, "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["Time", "Gas_Value", "Status"])

    while True:

        try:
            value = input("\nEnter sensor value (0-1023) or exit: ")

            if value.lower() == "exit":
                break

            gas_value = int(value)

            if gas_value < 0 or gas_value > 1023:
                print("Enter a value between 0 and 1023.")
                continue

            if gas_value < 500:
                status = "NORMAL"
            elif gas_value < 750:
                status = "MODERATE"
            else:
                status = "HIGH"

            current_time = datetime.now().strftime("%H:%M:%S")

            writer.writerow([current_time, gas_value, status])
            file.flush()

            print("Gas Input:", gas_value)
            print("Air Quality Status:", status)
            print("Reading saved!")

        except ValueError:
            print("Invalid input. Enter a number.")

print("\nMonitoring completed.")
print("File saved:", filename)


