# Air Quality Monitoring System

## Project Description
This project demonstrates an Air Quality Monitoring System using Arduino UNO and Python. A 1 kΩ potentiometer is used to simulate the analog output of a gas sensor. Arduino reads the changing input values and indicates different input levels using green and red LEDs.
Python is used to collect and store the simulated readings in a CSV file. Matplotlib is used to generate line and bar graphs for data visualization and analysis.

## Features
- Analog input simulation using a potentiometer.
- Arduino-based input monitoring.
- LED indication for different input levels.
- Python-based data logging.
- CSV file generation.
- Real-time manual data entry and graphical visualization.
- Line graph and bar graph generation using Matplotlib.

## Technologies Used
- Arduino UNO
- SimulIDE
- Arduino IDE
- Python 3.11
- CSV module
- Matplotlib

## Project Workflow
1. The potentiometer generates variable analog input values.
2. Arduino reads the input through analog pin A0.
3. The program classifies readings into normal, moderate and high input categories.
4. LEDs indicate the corresponding status.
5. Python stores readings and status information in a CSV file.
6. Matplotlib generates graphs to visualize the recorded data.

## Applications
- Smart-city monitoring system demonstrations.
- Embedded systems learning.
- Analog input monitoring.
- Sensor-data logging and visualization.

## Project Outcome
This project provides practical experience in Arduino programming, analog input processing, embedded-system simulation, Python data logging and graphical data visualization.
