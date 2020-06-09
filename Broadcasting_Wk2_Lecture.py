#!/usr/bin/env python
# coding: utf-8

import numpy as np

A = np.array([[56, 9, 4.4, 68],
              [1.2, 104, 52, 8],
              [1.8, 135, 99, 0.9]])

print(A)

cal = A.sum(axis=0)
print(cal)

percentage = 100 * A/cal.reshape(1,4)
print(percentage)
