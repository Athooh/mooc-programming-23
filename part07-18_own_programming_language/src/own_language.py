# # Write your solution here
def run(program):
    variables = {chr(ord('A') + i): 0 for i in range(26)}
    output = []

    def get_value(val):
        if val.isdigit():
            return int(val)
        else:
            return variables[val]

    line = 0
    while line < len(program):
        command = program[line].split()
        if command[0] == 'PRINT':
            output.append(get_value(command[1]))
        elif command[0] == 'MOV':
            variables[command[1]] = get_value(command[2])
        elif command[0] == 'ADD':
            variables[command[1]] += get_value(command[2])
        elif command[0] == 'SUB':
            variables[command[1]] -= get_value(command[2])
        elif command[0] == 'MUL':
            variables[command[1]] *= get_value(command[2])
        elif command[0] == 'IF':
            condition = f"{get_value(command[1])} {command[2]} {get_value(command[3])}"
            if not eval(condition):
                line += 1
        elif command[0] == 'JUMP':
            line = program.index(f"{command[1]}::") - 1
        elif command[0] == 'END':
            break

        line += 1

    return output

if __name__ == '__main__':
    program1 = [
        "MOV A 1",
        "MOV B 2",
        "PRINT A",
        "PRINT B",
        "ADD A B",
        "PRINT A",
        "END"
    ]
    result1 = run(program1)
    print(result1) 

    program2 = [
        "MOV A 1",
        "MOV B 10",
        "begin:",
        "IF A >= B JUMP quit",
        "PRINT A",
        "PRINT B",
        "ADD A 1",
        "SUB B 1",
        "JUMP begin",
        "quit:",
        "END"
    ]
    result2 = run(program2)
    print(result2)  

    program3 = [
        "MOV A 1",
        "MOV B 1",
        "begin:",
        "PRINT A",
        "ADD B 1",
        "MUL A B",
        "IF B <= 10 JUMP begin",
        "END"
    ]
    result3 = run(program3)
    print(result3)  

    program4 = [
        "MOV N 50",
        "PRINT 2",
        "MOV A 3",
        "begin:",
        "MOV B 2",
        "MOV Z 0",
        "test:",
        "MOV C B",
        "new:",
        "IF C == A JUMP error",
        "IF C > A JUMP over",
        "ADD C B",
        "JUMP new",
        "error:",
        "MOV Z 1",
        "JUMP over2",
        "over:",
        "ADD B 1",
        "IF B < A JUMP test",
        "over2:",
        "IF Z == 1 JUMP over3",
        "PRINT A",
        "over3:",
        "ADD A 1",
        "IF A <= N JUMP begin",
    ]
    result4 = run(program4)
    print(result4)  

