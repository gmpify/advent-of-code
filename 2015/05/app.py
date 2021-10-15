import re
from enum import Enum

class Exercise(Enum):
    PART1 = 1
    PART2 = 2

class Validator:
    def __init__(self, string, validations=Exercise.PART1):
        self.string = string
        if validations == Exercise.PART1:
            self.validations = [
                self.contains_three_vowels,
                self.contains_repeated_letter,
                self.contains_only_allowed_substring
            ]
        else:
            self.validations = [
                self.contains_repeated_substring,
                self.contains_repeated_letter_distant_of_2
            ]

    def is_nice_string(self):
        for validation in self.validations:
            if not validation():
                return False
        return True

    def contains_three_vowels(self):
        matches = re.findall(r'[aeiou]', self.string)
        return len(matches) >= 3

    def contains_repeated_letter_distant_of_2(self):
        return self.contains_repeated_letter(2)

    def contains_repeated_letter(self, distance=1):
        for i in range(distance, len(self.string)):
            if self.string[i] == self.string[i - distance]:
                return True
        return False

    def contains_only_allowed_substring(self):
        blocked_substrings = ['ab', 'cd', 'pq', 'xy']
        for substring in blocked_substrings:
            if substring in self.string:
                return False
        return True
    
    def contains_repeated_substring(self):
        substrings = [self.string[i] + self.string[i + 1] for i in range(len(self.string) - 1)]
        repeated_substrings = [substring for substring in substrings if self.string.count(substring) > 1]
        return len(repeated_substrings) > 0


if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read().split('\n')

    nice_strings = [s for s in input if Validator(s).is_nice_string()]
    print('Part One - Number of nice strings: ', len(nice_strings))

    nice_strings = [s for s in input if Validator(s, Exercise.PART2).is_nice_string()]
    print('Part Two - Number of nice strings: ', len(nice_strings))
