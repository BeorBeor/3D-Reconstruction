import numpy as np

from flip import compute_flip
from utils import *

if __name__ == '__main__':
	# Set viewing conditions
	monitor_distance = 0.7
	monitor_width = 0.7
	monitor_resolution_x = 3840
	
	# Compute number of pixels per degree of visual angle
	pixels_per_degree = monitor_distance * (monitor_resolution_x / monitor_width) * (np.pi / 180)
	
	# Load sRGB images
	reference = load_image_array('../images/reference.png')
	test = load_image_array('../images/test.png')

	# Compute FLIP map
	deltaE = compute_flip(reference, test, pixels_per_degree)

	# Save error map
	index_map = np.floor(255.0 * deltaE.squeeze(0))

	use_color_map = True
	if use_color_map:
		result = CHWtoHWC(index2color(index_map, get_magma_map()))
	else:
		result = index_map / 255.0
	save_image("../images/flip.png", result)
	print("Done")
