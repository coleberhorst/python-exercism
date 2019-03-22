def transpose(input_lines):
    input_lines = input_lines.split("\n")
    max_length = max([len(i) for i in input_lines])
    matrix_transpose_list = ["" * max_length]
    
