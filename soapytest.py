import simplesoapy
import numpy
import serial
import time
import SoapySDR
import os

# List all connected SoapySDR devices
devices = simplesoapy.detect_devices(as_string=True)
print('Detected devices:', devices)

if not devices:
    raise RuntimeError("No SDR devices found!")

# Use the first detected device string
sdr = simplesoapy.SoapyDevice(devices[0])

# Set sample rate
sdr.sample_rate = 2.56e6

# Set center frequency
sdr.freq = 88e6

# Setup base buffer and start receiving samples
sdr.start_stream()

# Create numpy array for received samples
samples = numpy.empty(len(sdr.buffer) * 100, numpy.complex64)

# Receive all samples
sdr.read_stream_into_buffer(samples)
sdr.stop_stream()

print("Sample max amplitude:", numpy.max(numpy.abs(samples)))
print("First 10 samples:", samples[:10])

# Simple signal detection (example: amplitude threshold)
if numpy.max(numpy.abs(samples)) > 0.5:
    detected = True
else:
    detected = False

# Replace '/dev/tty.usbmodemXXXX' with your Arduino's port
ser = serial.Serial('/dev/tty.usbmodem1101', 9600)
time.sleep(2)  # Wait for Arduino to reset

if detected:
    ser.write(b'1')  # Send a byte to Arduino
    os.system('open "/Users/ellawessendorff/Documents/CCI/Cybernetic_Dawn_Chorus/Python_scripts/SYMPHONY .mp3"')
else:
    ser.write(b'0')

ser.close()