import numpy as np
import imageio

# Load the 3D volume
volume = np.load('dataset_sample/3d_volume_result.npy')

# Normalize the volume to the range [0, 255] and convert to uint8
volume = (volume - np.min(volume)) / (np.max(volume) - np.min(volume)) * 255
volume = volume.astype(np.uint8)

# Create a list to store the images
images = []

# Read and store each slice as an image
for i in range(volume.shape[0]):
    # Convert the slice to RGB by repeating the grayscale values across 3 channels
    image_rgb = np.stack([volume[i, :, :]]*3, axis=-1)
    images.append(image_rgb)

# Save as a GIF
imageio.mimsave('3d_volume_result.gif', images, duration=0.8)  # Adjust duration as needed

# Save as a video using ffmpeg
writer = imageio.get_writer('3d_volume_result.mp4', fps=10, format='FFMPEG')
for image in images:
    writer.append_data(image)
writer.close()

print("GIF and video saved successfully.")
