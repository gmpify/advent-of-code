from itertools import combinations

def find_combinations_n(total_liters, containers, n):
    result = []
    for c in combinations(containers, n):
        if sum(c) == total_liters:
            result.append(c)
    return result

def find_combinations(total_liters, containers, only_minimum=False):
    result = []

    containers.sort(reverse=True)
    for n in range(len(containers) + 1):
        result.extend(find_combinations_n(total_liters, containers, n))
        if only_minimum and len(result) > 0:
            return result

    return result

if __name__ == '__main__':
    containers = [int(l) for l in open('input.txt')]
    print(f"Part 1: {len(find_combinations(150, containers))} combinations")

    print(f"Part 2: {len(find_combinations(150, containers, True))} combinations")
