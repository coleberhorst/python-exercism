class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    result = []
    for line in input_data:
        line = [int(i) if i.isnumeric() else i for i in line.split(" ")]
        print(line)
        while len(line) >= 2:
            if  in line and len(line) < 3:
                raise StackUnderflowError("Not enough literals for math operations.")
            if '+' in line[:3]:
                line = [line[0] + line[1]] + line[3:]
            elif '-' == line[2]:
                line = [line[0] - line[1]] + line[3:]
            elif '*' == line[2]:
                line = [line[0] * line[1]] + line[3:]
            elif '/' == line[2]:
                line = [line[0] // line[1]] + line[3:]
            elif 'dup' == line[1]:
                if len(line) < 2:
                    raise StackUnderflowError("Not enough literals for dup.")
                line[1] = line[0]
            else:
                break

    return line
