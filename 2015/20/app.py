import multiprocessing

class Elf:
    def __init__(self, number, present_per_house) -> None:
        self.number = number
        self.presents = number * present_per_house
        self.houses_visited = 0

class House:
    def __init__(self, number) -> None:
        self.number = number
        self.presents = 0

class Street:
    def __init__(self, target) -> None:
        self.houses = []
        if target > 100:
            self.houses_count = target // 10
        else:
            self.houses_count = target

        for i in range(self.houses_count):
            self.houses.append(House(i + 1))

    def visit_houses(self, limit = None, presents_per_house = 10):
        if not limit:
            limit = self.houses_count

        for i in range(self.houses_count):
            elf = Elf(i + 1, presents_per_house)
            for h in range(i, self.houses_count, elf.number):
                if elf.houses_visited > limit:
                    break

                self.houses[h].presents += elf.presents
                elf.houses_visited += 1

    def lowest_house_number(self):
        for h in self.houses:
            if h.presents >= target:
                return h.number


if __name__ == '__main__':
    target = 34000000
    print(f'Part 1: Testing first house with {target} presents')
    street = Street(target)
    street.visit_houses()
    print(f'Lowest house number: {street.lowest_house_number()}')

    print(f'Part 2: Testing first house with {target} presents, but with limits and different presents per house')
    street = Street(target)
    street.visit_houses(limit=50, presents_per_house=11)
    print(f'Lowest house number: {street.lowest_house_number()}')

