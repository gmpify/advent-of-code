import random
import copy
import re

class City:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if isinstance(other, City):
            return self.name == other.name
        return False

    def add_connection(self, other, distance):
        if other not in self.connections:
            self.connections[other] = distance

    def get_connection_distance(self, other):
        return self.connections[other]


class Path:
    def __init__(self, initial_city=None):
        self.total_distance = 0
        self.cities = []
        if initial_city is not None:
            self.cities.append(initial_city)

    def __copy__(self):
        other = Path()
        other.total_distance = self.total_distance
        other.cities = self.cities[:]
        return other

    def add_city(self, city):
        last_city = self.cities[-1]
        self.total_distance += last_city.get_connection_distance(city)
        self.cities.append(city)


def find_paths(graph):
    root = City('root')
    for _, city in graph.items():
        root.add_connection(city, 0)

    result = []
    find_path_recurse(Path(root), result, set())
    return result


def find_path_recurse(path, result, visited):
    city = path.cities[-1]
    if len(visited) == len(city.connections) + 1:
        result.append(path)
    for connection in city.connections:
        if connection not in visited:
            p = copy.copy(path)
            p.add_city(connection)
            v = copy.copy(visited)
            v.add(connection)
            find_path_recurse(p, result, v)


def get_shortest_path(paths):
    shortest_path = paths[0]
    for path in paths:
        if path.total_distance < shortest_path.total_distance:
            shortest_path = path
    return shortest_path


def get_longest_path(paths):
    longest_path = paths[0]
    for path in paths:
        if path.total_distance > longest_path.total_distance:
            longest_path = path
    return longest_path


def load_graph(file_name):
    result = {}
    file = open(file_name)
    for line in file:
        m = re.match(r'(?P<city_1>[a-zA-Z]+) to (?P<city_2>[a-zA-Z]+) = (?P<distance>\d+)', line)
        city_1_name, city_2_name, distance = m.group('city_1'), m.group('city_2'), int(m.group('distance'))
        city_1 = result.get(city_1_name, City(city_1_name))
        city_2 = result.get(city_2_name, City(city_2_name))
        city_1.add_connection(city_2, distance)
        city_2.add_connection(city_1, distance)
        result[city_1_name] = city_1
        result[city_2_name] = city_2
    return result


if __name__ == '__main__':
    graph = load_graph('input.txt')
    paths = find_paths(graph)
    shortest_path = get_shortest_path(paths)
    print('Solution One')
    print(' Distance: ', shortest_path.total_distance)
    print(' Path:')
    for c in shortest_path.cities:
        print('  ', c.name)

    longest_path = get_longest_path(paths)
    print('Solution Teo')
    print(' Distance: ', longest_path.total_distance)
    print(' Path:')
    for c in longest_path.cities:
        print('  ', c.name)
