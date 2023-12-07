import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parameters
face_radius = 5
eye_radius = 0.5
mouth_radius = 3
center = (0, 0)
noise_level = 0.1  # Adjust the level of noise
sample_fraction = 0.7  # Fraction of points to sample

# Function to add noise and sample points
def add_noise_and_sample(x, y, noise_level, sample_fraction):
    # Add noise
    x_noisy = x + np.random.normal(0, noise_level, x.shape)
    y_noisy = y + np.random.normal(0, noise_level, y.shape)
    
    # Sample points
    num_points = len(x_noisy)
    sample_size = int(num_points * sample_fraction)
    indices = np.random.choice(num_points, sample_size, replace=False)
    
    return x_noisy[indices], y_noisy[indices]

# Create face outline
theta = np.linspace(0, 2*np.pi, 100)
x_face = face_radius * np.cos(theta) + center[0]
y_face = face_radius * np.sin(theta) + center[1]
x_face_noisy, y_face_noisy = add_noise_and_sample(x_face, y_face, noise_level, sample_fraction)

# Create eyes
e1_center = (-2, 2)
e2_center = (2, 2)
x_eye1 = eye_radius * np.cos(theta) + e1_center[0]
y_eye1 = eye_radius * np.sin(theta) + e1_center[1]
x_eye2 = eye_radius * np.cos(theta) + e2_center[0]
y_eye2 = eye_radius * np.sin(theta) + e2_center[1]
x_eye1_noisy, y_eye1_noisy = add_noise_and_sample(x_eye1, y_eye1, noise_level, sample_fraction)
x_eye2_noisy, y_eye2_noisy = add_noise_and_sample(x_eye2, y_eye2, noise_level, sample_fraction)

# Create smile
theta_smile = np.linspace(np.pi/4, 3*np.pi/4, 50)
x_smile = mouth_radius * np.cos(theta_smile) + center[0]
y_smile = -mouth_radius * np.sin(theta_smile) + center[1]
x_smile_noisy, y_smile_noisy = add_noise_and_sample(x_smile, y_smile, noise_level, sample_fraction)

# Combine all points
x = np.concatenate([x_face_noisy, x_eye1_noisy, x_eye2_noisy, x_smile_noisy])
y = np.concatenate([y_face_noisy, y_eye1_noisy, y_eye2_noisy, y_smile_noisy])

pd.DataFrame({'x': x, 'y': y}).to_csv('how_are_you_feeling.csv', index=False)

# Plot for visualization
plt.scatter(x, y)
plt.axis('equal')
plt.show()
