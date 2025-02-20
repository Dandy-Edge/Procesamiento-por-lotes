
def rewrite_line(original_line: str):
    hex_to_int = []
    int_to_hex = []

    for value in original_line.split(':', 8):
        try:
            hex_to_int.append(int(value, 16))
        except ValueError:
            line = value
    
    splited_line = line.split('/', 1)
    hex_to_int.append(int(splited_line[0], 16))
    line = splited_line[1]

    splited_line = line.split(',')
    modified_line = splited_line[2] + ':'

    line = splited_line[5]

    for value in line.split('.'):
        int_to_hex.append(format(int(value), 'x'))

    for value in hex_to_int:
        modified_line += str(value) + ':'

    for value in int_to_hex:
        modified_line += str(value) + '.'

    modified_line = modified_line[:-1] + '\n'

    with open('result.txt', 'a') as w_file:
        w_file.write(modified_line)
    

with open('prueba2.txt', 'r') as r_file:
    for line in r_file:
        rewrite_line(line)