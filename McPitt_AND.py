import numpy as np
import pandas as pd
def cal_output_and(threshold=0):
    weight1 = 1
    weight2 = 1
    bias = 0
    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    correct_outputs = [False, False, False, True]
    outputs = []
    for test_input, correct_output in zip(test_inputs, correct_outputs):
        linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
        output = int(linear_combination >= threshold)
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])
    num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
    output_frame = pd.DataFrame(outputs, columns=['Input 1', ' Input 2', ' Linear Combination', ' Activation Output', ' Is Correct'])
    if not num_wrong:
        print('all correct for threshold {}.\n'.format(threshold))
    else:
        threshold = threshold + 1
        cal_output_and(threshold)
        print('{} wrong, for threshold {} \n'.format(num_wrong,threshold))
    print(output_frame.to_string())
    return threshold
t = cal_output_and()
