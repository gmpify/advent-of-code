import re

class Validator:
    def __init__(self, string):
        self.string = string
        self.validations = [
            self.contains_three_vowels,
            self.contains_repeated_letter,
            self.contains_only_allowed_substring
        ]

    def is_nice_string(self):
        for validation in self.validations:
            if not validation():
                return False
        return True

    def contains_three_vowels(self):
        matches = re.findall(r'[aeiou]', self.string)
        return len(matches) >= 3

    def contains_repeated_letter(self):
        previous_letter = ''
        for letter in self.string:
            if letter == previous_letter:
                return True
            previous_letter = letter
        return False

    def contains_only_allowed_substring(self):
        blocked_substrings = ['ab', 'cd', 'pq', 'xy']
        for substring in blocked_substrings:
            if substring in self.string:
                return False
        return True

if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read().split('\n')

    nice_strings = [s for s in input if Validator(s).is_nice_string()]
    print('Number of nice strings: ', len(nice_strings))
