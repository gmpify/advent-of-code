import re

class Reindeer:
    def __init__(self, name, speed, flying_time, resting_time):
        self.name = name
        self.speed = speed
        self.flying_time = flying_time
        self.resting_time = resting_time
        self.distance_cache = []

    def calculate_until(self, time):
        distance = 0
        for i in range(time + 1):
            self.distance_cache.append(distance)
            if i % (self.flying_time + self.resting_time) < self.flying_time:
                distance += self.speed

    def distance_at(self, time):
        return self.distance_cache[time]

    def load(line):
        m = re.match(r'(?P<name>\w*) can fly (?P<speed>\d*) km/s for (?P<flying_time>\d*) seconds, but then must rest for (?P<resting_time>\d*) seconds.', line)
        name = m.group('name')
        speed = int(m.group('speed'))
        flying_time = int(m.group('flying_time'))
        resting_time = int(m.group('resting_time'))
        return Reindeer(name, speed, flying_time, resting_time)

    def load_all(file_name):
        result = []
        for line in open(file_name):
            reindeer = Reindeer.load(line)
            result.append(reindeer)
        return result

def process_part_1(file_name, time):
    reindeers = Reindeer.load_all(file_name)
    winner = None
    for reindeer in reindeers:
        reindeer.calculate_until(time)
        if not winner or reindeer.distance_at(time) > winner.distance_at(time):
            winner = reindeer
    print(f"The winner reindeer is {winner.name} with {winner.distance_at(time)} kms")

def process_part_2(file_name, time):
    points_per_reindeers = {}
    reindeers = Reindeer.load_all(file_name)
    for reindeer in reindeers:
        points_per_reindeers[reindeer.name] = 0
        reindeer.calculate_until(time)

    for i in range(1, time):
        winners = []
        for reindeer in reindeers:
            if len(winners) == 0 or reindeer.distance_at(i) > winners[0].distance_at(i):
                winners = [reindeer]
            elif reindeer.distance_at(i) == winners[0].distance_at(i):
                winners.append(reindeer)

        for reindeer in winners:
            points_per_reindeers[reindeer.name] += 1

    winner = None
    for reindeer in reindeers:
        if winner is None or points_per_reindeers[reindeer.name] > points_per_reindeers[winner.name]:
            winner = reindeer

    print(f"The winner reindeer is {winner.name} with {points_per_reindeers[winner.name]} points")

if __name__ == '__main__':
    process_part_1('input.txt', 2503)
    process_part_2('input.txt', 2503)
