import h5py
import numpy as np

# Open the .h5 file
file_path = "data/train/R18062014457581.h5"
# with h5py.File(file_path, "r") as f:
#     # List all datasets in the file
#     print("Datasets in the file:")
#     def explore_group(group, indent=0):
#         for key in group.keys():
#             item = group[key]
#             if isinstance(item, h5py.Dataset):
#                 print("  " * indent + f"Dataset: {key}, Shape: {item.shape}, DataType: {item.dtype}")
#             elif isinstance(item, h5py.Group):
#                 print("  " * indent + f"Group: {key}")
#                 explore_group(item, indent + 1)
    
#     explore_group(f)

import h5py
import matplotlib.pyplot as plt

# Load the file
# file_path = file_path
# with h5py.File(file_path, "r") as f:
#     vil_data = f["/vil"][:]  # Load the full 3D dataset
    
#     # Print the shape to understand time points
#     print(f"Dataset shape: {vil_data.shape} (Lat, Lon, Time)")

#     # Visualize a slice for a specific time index
#     time_index = 1  # Change this to explore other time points
#     plt.imshow(vil_data[:, :, time_index], cmap="jet")
#     plt.colorbar()
#     plt.title(f"Weather Data (Time Index: {time_index})")
#     plt.show()


import h5py

# Load the file
# file_path = "path_to_your_file.h5"

with h5py.File(file_path, "r") as f:
    # Print all keys and subkeys in the file
    def print_structure(name, obj):
        print(f"{name}: {obj}")
        if isinstance(obj, h5py.Dataset):
            print(f"  Shape: {obj.shape}, Type: {obj.dtype}")

    print("\n--- File Structure ---")
    f.visititems(print_structure)
    
    # Print file attributes
    print("\n--- File Attributes ---")
    for attr in f.attrs:
        print(f"{attr}: {f.attrs[attr]}")

with h5py.File(file_path, "r") as f:
    # Read latitude and longitude datasets if they exist
    if "/latitude" in f:
        latitudes = f["/latitude"][:]
        print(f"Latitude values: {latitudes}")
    else:
        print("Latitude dataset not found.")

    if "/longitude" in f:
        longitudes = f["/longitude"][:]
        print(f"Longitude values: {longitudes}")
    else:
        print("Longitude dataset not found.")

    # Time extraction example
    if "/time" in f:
        time_data = f["/time"][:]
        print(f"Time values: {time_data}")
    else:
        print("Time dataset not found.")

