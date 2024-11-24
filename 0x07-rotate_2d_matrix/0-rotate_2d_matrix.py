#!/usr/bin/python3
"""module to reverse matrix clockwise"""


def rotate_2d_matrix(matrix):
	"""reverse matrix 90 degrees clockwise"""
	n = len(matrix)
	for i in range(n):
		for j in range(i + 1):
			m[i][j], m[j][i] = m[j][i], m[i][j]
	for i in range(n):
		m[i] = m[i][::-1]
