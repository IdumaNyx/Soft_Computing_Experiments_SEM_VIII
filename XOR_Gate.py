import pandas as pd
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [False, True, True, False]
outputs = []
for test_input, correct_output in zip(test_inputs, correct_outputs):
    output = int(test_input[0] ^ test_input[1])
    outputs.append([test_input[0], test_input[1], output])
    output_frame = pd.DataFrame(outputs, columns=['Input A', ' Input B', 'Output'])
print(output_frame.to_string(index=False))
