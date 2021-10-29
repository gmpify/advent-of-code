class LookAndSay:
    def process(self, input):
        result = ''
        first_ocurrence = last_occurrence = 0

        while last_occurrence < len(input):
            if input[first_ocurrence] != input[last_occurrence]:
                result = result + str(last_occurrence - first_ocurrence) + input[first_ocurrence]
                first_ocurrence = last_occurrence
            last_occurrence += 1
        result = result + str(last_occurrence - first_ocurrence) + input[first_ocurrence]

        return result

if __name__ == '__main__':
    look_and_say = LookAndSay()
    num = '3113322113'
    for _ in range(40):
        num = look_and_say.process(num)

    print('Part One: ', len(num))

    for _ in range(10):
        num = look_and_say.process(num)

    print('Part Two: ', len(num))
