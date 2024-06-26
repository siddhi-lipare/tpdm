import numpy as np
import os
import matplotlib.pyplot as plt

# Define the path to the folder containing the .npy files
npy_folder = 'invp_results/BMR_ZSR_256/x5/K2/lamb4.0/240618_135735/recon'

# Get the list of .npy files
npy_files = sorted([file for file in os.listdir(npy_folder) if file.endswith('.npy')])

# Load the first .npy file to get the dimensions
sample_array = np.load(os.path.join(npy_folder, npy_files[0]))
print(sample_array.shape)
_, height, width = sample_array.shape

# Create an empty array to store the 3D volume
volume = np.zeros((len(npy_files), height, width), dtype=sample_array.dtype)

# Read and stack each .npy file
for i, npy_file in enumerate(npy_files):
    array_path = os.path.join(npy_folder, npy_file)
    volume[i] = np.load(array_path)[0]  # Remove the extra singleton dimension

# Now 'volume' is a 3D numpy array representing the 3D volume
print(f"3D volume shape: {volume.shape}")

# Optional: Save the 3D volume to a file
np.save('dataset_sample/3d_volume_result.npy', volume)