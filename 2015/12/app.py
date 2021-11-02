import re
import json

class JsonParser:
    def __init__(self, content):
        self.content = json.loads(content)
        self.nums = []
        self.parse(self.content)

    def parse(self, content):
        if isinstance(content, int):
            self.parse_int(content)
        elif isinstance(content, list):
            self.parse_list(content)
        elif isinstance(content, dict):
            self.parse_dict(content)

    def parse_int(self, content):
        self.nums.append(content)

    def parse_list(self, content):
        for elem in content:
            self.parse(elem)

    def parse_dict(self, content):
        for elem_key, elem_value in content.items():
            self.parse(elem_key)
            self.parse(elem_value)

    def sum_all_nums(self):
        return sum(self.nums)


class JsonParserRed(JsonParser):
    def parse_dict(self, content):
        if 'red' not in content.values():
            super().parse_dict(content)


if __name__ == '__main__':
    f = open('input.txt')
    content = f.read()

    jp = JsonParser(content)
    jp_sum = jp.sum_all_nums()

    print('Part One:', jp_sum)

    jp_red = JsonParserRed(content)
    jp_sum_red = jp_red.sum_all_nums()

    print('Part Two:', jp_sum_red)
