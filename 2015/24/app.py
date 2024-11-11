from itertools import combinations

def find_min_group_length(items, group_weigth):
    min_group_length = 0
    temp_sum = 0
    i = len(items) - 1
    while i >= 0:
        min_group_length += 1
        temp_sum += items[i]
        if temp_sum >= group_weigth:
            break
        i -= 1
    return min_group_length

def find_max_group_length(items, group_weigth):
    max_group_length = 0
    temp_sum = 0
    i = 0
    while i < len(items):
        max_group_length += 1
        temp_sum += items[i]
        if temp_sum >= group_weigth:
            break
        i += 1
    return max_group_length

def calculate_qe(items):
    res = 1
    for i in items:
        res *= i
    return res

def find_valid_group(items, group_weigth):
    items = sorted(items)
    
    min_group_length = find_min_group_length(items, group_weigth)
    max_group_length = find_max_group_length(items, group_weigth)

    length = min_group_length

    while length <= max_group_length:
        comb = combinations(items, length)
        groups = [c for c in list(comb) if sum(c) == group_weigth]
        sorted(groups, key=lambda g: calculate_qe(g))
        sorted(groups, key=lambda g: sum(g))
        for group in groups:
            remaining_group = [i for i in items if i not in group]
            if len(remaining_group) <= 0:
                return [group]
            g = find_valid_group(remaining_group, group_weigth)
            return [group, g]
        length += 1

if __name__ == '__main__':
    f = open('/home/gmpify/src/github.com/gmpify/advent-of-code/2015/24/input.txt', 'r')
    lines = f.read().split('\n')

    gifts = [int(l) for l in lines]

    print("Part 1")
    group_weigth = sum(gifts)//3

    print("Total number of gitfs:", len(gifts))
    print("Total weight of gifts:", sum(gifts))
    print("Group weight:", group_weigth)

    groups = find_valid_group(gifts, group_weigth)

    print("Groups:", groups)
    print("QE of group 1:", calculate_qe(groups[0]))


    print("Part 2")
    group_weigth = sum(gifts)//4

    print("Total number of gitfs:", len(gifts))
    print("Total weight of gifts:", sum(gifts))
    print("Group weight:", group_weigth)

    groups = find_valid_group(gifts, group_weigth)

    print("Groups:", groups)
    print("QE of group 1:", calculate_qe(groups[0]))
