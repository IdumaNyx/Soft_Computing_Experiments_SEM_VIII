import numpy as np

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

input=[(0, 0), (0, 1), (1, 0), (1, 1)]

for i in input:
    print(AND_gate_ip(i))
