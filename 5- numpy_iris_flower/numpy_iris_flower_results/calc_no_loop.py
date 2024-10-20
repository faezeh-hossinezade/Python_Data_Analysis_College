# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    return np.sum(new_points**2, axis=1)[:, np.newaxis] + np.sum(points**2, axis=1) - 2*(new_points@points.T)
