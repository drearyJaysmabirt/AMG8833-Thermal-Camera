import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize plot
fig, ax = plt.subplots()
im = ax.imshow(np.zeros((8,8)), cmap='inferno', interpolation='bilinear')
plt.colorbar(im, label="Temperature (°C)")
plt.title("AMG8833 Thermal Camera (COM7)")

# Serial setup (COM7, 115200 baud)
ser = serial.Serial('COM7', 115200, timeout=1)

def update(frame):
    try:
        line = ser.readline().decode().strip()
        if line:
            data = list(map(float, line.split(',')))
            if len(data) == 64:
                pixels = np.array(data).reshape(8, 8)
                im.set_array(pixels)
                im.autoscale()
    except Exception as e:
        print(f"Error: {e}")
    return [im]  # Required for blitting

# Animation settings
ani = FuncAnimation(
    fig, 
    update, 
    blit=True, 
    interval=20,  # Match Arduino's delay (50ms = ~20 FPS)
    cache_frame_data=False  # Avoid memory warnings
)

plt.show()