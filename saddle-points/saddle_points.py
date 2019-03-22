def saddle_points(matrix):
    points = set()
    if matrix:
        first_column_length = len(matrix[0])
    for x_index, column in enumerate(matrix):
        if len(column) != first_column_length:
            raise ValueError("Matrix isn't square or rectangular.")
        for y_index, element in enumerate(column):
            if element == max(column) and element == min([z[y_index] for z in matrix]):
                points.add((x_index+1, y_index+1))
    return points
