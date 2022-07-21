from itertools import combinations

def find_combinations_n(total_liters, containers, n):
    result = []
    for c in combinations(containers, n):
        if sum(c) == total_liters:
            result.append(c)
        elif sum(c) < total_liters:
            break
    return result

def find_combinations(total_liters, containers):
    result = []

    containers.sort(reverse=True)
    for n in range(len(containers)):
        result.extend(find_combinations_n(total_liters, containers, n))

    return result

if __name__ == '__main__':
    pass
