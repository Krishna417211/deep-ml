import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	
	mag = 0
	for i in gradient:
		mag += i ** 2

	mag = mag ** 0.5

	dirc = [x/mag if mag > 0 else 0 for x in gradient]

	dirc_ac = [-x for x in dirc]

	return {'magnitude': mag, 'direction': dirc,'descent_direction':dirc_ac}
	