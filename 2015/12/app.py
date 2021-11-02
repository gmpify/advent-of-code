import re

class JsonParser:
    def __init__(self, content):
        self.content = content
        self.nums = []
        self.parse_nums()

    def parse_nums(self):
        matches = re.findall(r'-?\d+', self.content)
        self.nums = [int(m) for m in matches]

    def sum_all_nums(self):
        return sum(self.nums)

if __name__ == '__main__':
    f = open('input.txt')
    content = f.read()

    jp = JsonParser(content)
    jp_sum = jp.sum_all_nums()

    print('Part One:', jp_sum)