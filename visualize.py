import h5py
import matplotlib.pyplot as plt

# give the file path here
file_path = "data/test/R19061119368410.h5"

# Open the .h5 file
with h5py.File(file_path, "r") as h5_file:  
    data = h5_file["ir069"]  # Reference the dataset

    # Loop through the first 5 slices along the third dimension
    for i in range(5):
        slice_data = data[:, :, i]  # Extract the ith slice
        plt.figure(figsize=(6, 6))  # Set figure size
        plt.imshow(slice_data, cmap="viridis")
        plt.colorbar()
        plt.title(f"Visualizing Slice {i + 1} of 'ir069'")
        plt.show()


# h5 file metadata

# import h5py

# # Path to your .h5 file
# file_path = "file.h5"

# # Open the .h5 file
# with h5py.File(file_path, "r") as h5_file:
#     # Get the list of datasets
#     dataset_names = list(h5_file.keys())
    
#     print(f"Number of datasets: {len(dataset_names)}")
#     print("Details of datasets:")
    
#     # Print details for each dataset
#     for dataset_name in dataset_names:
#         dataset = h5_file[dataset_name]
#         print(f"Dataset: {dataset_name} | Shape: {dataset.shape} | Dtype: {dataset.dtype}")
