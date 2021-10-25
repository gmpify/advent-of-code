def get_literal_length(line):
    return len(line)

def get_string_length(line):
    return len(eval(line.decode('utf-8'))) 

def process_file(file_name):
    total_string_literals = total_string = 0
    for line in open(file_name, 'rb'):
        line = line.strip()
        total_string_literals += get_literal_length(line)
        total_string += get_string_length(line)
    return (total_string_literals, total_string)

if __name__ == '__main__':
    total_string_literals, total_string = process_file('input.txt')

    print('Solution 1: ', total_string_literals - total_string)
