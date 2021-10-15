import re

class Validator:
    def __init__(self, string):
        self.string = string
        self.validations = [
            self.contains_three_vowels,
            self.contains_repeated_letter,
            self.not_contains_blocked_substring
        ]

    def contains_three_vowels(self):
        matches = re.findall(r'[aeiou]', self.string)
        return len(matches) >= 3

    def contains_repeated_letter(self):
        pass

    def not_contains_blocked_substring(self):
        pass
