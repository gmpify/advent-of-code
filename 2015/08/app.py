def get_encoded_length(line):
    srting = line.decode('utf-8')
    string = repr(srting)[1:-1]
    string = '"' + string.replace('"', '\\"') + '"'
    return len(string)

def get_literal_length(line):
    return len(line)

def get_string_length(line):
    string = line.decode('utf-8')
    return len(eval(string))

def process_file(file_name):
    total_string_literals = total_string = total_string_encoded = 0
    for line in open(file_name, 'rb'):
        line = line.strip()
        total_string_literals += get_literal_length(line)
        total_string += get_string_length(line)
        total_string_encoded += get_encoded_length(line)
    return (total_string_literals, total_string, total_string_encoded)

if __name__ == '__main__':
    total_string_literals, total_string, total_string_encoded = process_file('input.txt')

    print('Solution 1: ', total_string_literals - total_string)
    print('Solution 2: ', total_string_encoded - total_string_literals)
