
def rewrite_line(line: str):
    hex_to_int = []
    new_string = ''
    int_to_hex = []

    for value in line.split(':', 8):
        try:
            hex_to_int.append(int(value, 16))
        except ValueError:
            line = value
    
    splited_line = line.split('/', 1)
    hex_to_int.append(int(splited_line[0], 16))
    line = splited_line[1]

    splited_line = line.split(',')
    new_string = splited_line[2] + ':'

    line = splited_line[5]

    for value in line.split('.'):
        int_to_hex.append(format(int(value), 'x'))

    for value in hex_to_int:
        new_string += str(value) + ':'

    for value in int_to_hex:
        new_string += str(value) + '.'

    new_string = new_string[:-1] + '\n'

    with open('result.txt', 'a') as w_file:
        w_file.write(new_string)
    

with open('prueba2.txt', 'r') as r_file:
    for line in r_file:
        rewrite_line(line)