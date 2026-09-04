Micro:bit V2 Ambient Monitor & Audio Event Logger

A MicroPython script for the BBC micro:bit V2 that functions as an ambient data logger and conversational noise tracker. It records regular hourly environmental snapshots alongside triggered audio events (such as loud conversations or sudden noises) using the built-in microphone, temperature sensor, and light sensor.

Features

Automatic Hourly Logging (type_event: 0): Captures ambient sound averages, temperature, and light levels every hour using @run_every.

Event-Driven Logging (type_event: 1): Detects when sound crosses a specific threshold (seuil_bruit = 85), tracks the duration of the event, and logs averaged sensor data once the noise subsides.

Built-in Flash Logging: Utilizes the MicroPython log module to save data directly onto the micro:bit for easy retrieval.

Hardware Requirements

BBC micro:bit V2 (required for the built-in microphone).

Code Structure

Initialization: Sets up CSV-like headers (type_event, duree_conv, son_moy, temp_moy, lum_moy) and gives a 10-second startup buffer indicated by the center LED.

Hourly Routine: A background task running every 3600 seconds to record baseline ambient conditions.

Main Loop: Continuously samples sensors every 10ms to monitor noise spikes, manage event durations, and write logs to internal memory.

Usage & Installation

Flash the Python script onto your micro:bit V2 using the Mu Editor or the Online Python Editor.

Disconnect and place the device in your target location (ensure it stays powered via battery pack or USB).

Retrieve the LOG.CSV file from the micro:bit drive once recording is complete
