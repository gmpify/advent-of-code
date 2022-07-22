from itertools import combinations

def find_combinations_n(total_liters, containers, n):
    result = []
    for c in combinations(containers, n):
        if sum(c) == total_liters:
            result.append(c)
    return result

def find_combinations(total_liters, containers):
    result = {}

    containers.sort(reverse=True)
    for n in range(len(containers) + 1):
        c = find_combinations_n(total_liters, containers, n)
        if len(c) > 0:
            result[n] = c

    return result

if __name__ == '__main__':
    containers = [int(l) for l in open('input.txt')]
    result = find_combinations(150, containers)

    m = map(lambda x: len(x), result.values())
    print(f"Part 1: {sum(m)} combinations")

    m = min(result.keys())
    print(f"Part 2: {len(result[m])} combinations")
