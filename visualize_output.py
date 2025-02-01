import h5py
import numpy as np
import matplotlib.pyplot as plt

# Load the HDF5 file
file_path = 'experiments/testOutput_wID/R19070915538410.h5'
with h5py.File(file_path, 'r') as f:
    y_hat_denorm = f['y_hat_denorm'][:]  # Shape: (1, 24, 384, 384, 1)

# Fix the shape: Remove batch and channel dimensions
y_hat_denorm = np.squeeze(y_hat_denorm, axis=(0, -1))  # Now shape: (24, 384, 384)

# Function to interpret weather from reflectivity values
def interpret_weather(reflectivity):
    if reflectivity < 20:
        return "🌦️ Light rain or drizzle"
    elif 20 <= reflectivity < 40:
        return "🌧️ Moderate rain"
    elif 40 <= reflectivity < 50:
        return "🌧️⚡ Heavy rain with thunderstorms"
    else:
        return "⛈️ Severe Thunderstorm or Hail"

# Display a single frame (first time step as an example)
time_step = 0  # Change this for other time steps
predicted_image = y_hat_denorm[time_step]  # Select the image at time_step

plt.figure(figsize=(8, 6))
plt.imshow(predicted_image, cmap='viridis', vmin=0, vmax=70)
plt.colorbar(label='Reflectivity (dBZ)')
plt.title(f'Predicted Weather at Time Step {time_step + 1}')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Analyze weather condition
max_reflectivity = np.max(predicted_image)
avg_reflectivity = np.mean(predicted_image)
weather_condition = interpret_weather(max_reflectivity)

print(f"\n🌍 **Weather Analysis for Time Step {time_step + 1}** 🌍")
print(f"🔹 Maximum Reflectivity: {max_reflectivity:.2f} dBZ")
print(f"🔹 Average Reflectivity: {avg_reflectivity:.2f} dBZ")
print(f"🔹 Forecast: {weather_condition}")