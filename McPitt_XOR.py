import numpy as np
import pandas as pd

def step_function(ip,threshold=0):
    if ip >= threshold:
        return 1
    else:
        return 0

def cal_gate(x, w, b, threshold=0):
    linear_combination = np.dot(w, x) + b
    #print(linear_combination)
    y = step_function(linear_combination,threshold)
    #clear_output(wait=True)
    return y

def AND_gate_ip(x):
    w = np.array([1, 1])
    b = -1.5
    #threshold = cal_output_or()
    return cal_gate(x, w, b)

def NOT_gate_ip(x):
    w = -1
    b = .5
    #threshold = cal_output_not()
    return cal_gate(x, w, b)

def OR_ip(x):
    w = np.array([1, 1])
    b = -0.5
    return cal_gate(x, w, b)

def Logical_XOR(x):
    A = AND_gate_ip(x)
    C = NOT_gate_ip(A)
    B = OR_ip(x)
    AND_output = np.array([C, B])
    output = AND_gate_ip(AND_output)
    return output

input=[(0, 0), (0, 1), (1, 0), (1, 1)]

for i in input:
    print(Logical_XOR(i))
