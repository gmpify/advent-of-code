import string

class PasswordValidator:
    def __init__(self):
        self.validations = [
            self.validate_increasing_three_letters,
            self.validate_has_only_allowed_letters,
            self.validate_has_two_pairs_of_letters
        ]
    
    def valid(self, password):
        if len(password) != 8:
            return False

        for validation in self.validations:
            if not validation(password):
                return False
        return True
    
    def validate_increasing_three_letters(self, password):
        substring_start = 0
        substring_end = 3
        while substring_end <= len(string.ascii_lowercase):
            if string.ascii_lowercase[substring_start:substring_end] in password:
                return True
            substring_start += 1
            substring_end += 1
        return False

    def validate_has_only_allowed_letters(self, password):
        blocked_letters = ['i', 'o', 'l']
        for letter in blocked_letters:
            if letter in password:
                return False
        return True

    def validate_has_two_pairs_of_letters(self, password):
        num_of_pairs = 0
        i_letter = 1
        while i_letter < len(password):
            if password[i_letter] == password[i_letter - 1]:
                num_of_pairs += 1
                i_letter += 1
            i_letter += 1
        return num_of_pairs >= 2

class PasswordGenerator:
    def __init__(self):
        self.validator = PasswordValidator()
    
    def generate_next_valid(self, password):
        next_password = self.generate_next(password)
        while not self.validator.valid(next_password):
            next_password = self.generate_next(next_password)
        return next_password

    def generate_next(self, password):
        added = False
        result = ''
        for char in password[::-1]:
            if added:
                result += char
            elif char == 'z':
                result += 'a'
            else:
                added = True
                next_char_i = string.ascii_lowercase.index(char) + 1
                result += string.ascii_lowercase[next_char_i]
        return result[::-1]

if __name__ == '__main__':
    generator = PasswordGenerator()
    next_password = generator.generate_next_valid('hepxcrrq')
    print('Part One:', next_password)

    next_password = generator.generate_next_valid(next_password)
    print('Part Two:', next_password)
