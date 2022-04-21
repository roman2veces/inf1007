import numpy as np


def get_length(vector):
    return np.sqrt(vector[0] ** 2 + vector[1] ** 2)


def get_angle(vector):
    return np.arctan2(vector[1], vector[0])


def to_polaire(coordinates: np.array):
    converted_coordinates = np.array(
        [[get_length(vector), get_angle(vector)] for vector in coordinates])

    return converted_coordinates


polaire_coordinates = to_polaire(np.array([
    [1, 1],
    [2, 0],
    [3, 3],
    [4, 4]
]))

print(polaire_coordinates)
