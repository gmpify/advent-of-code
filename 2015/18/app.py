class Light:
    OFF = '.'
    ON = '#'

    def __init__(self, state):
        self.state = state

    def __str__(self):
        return self.state

    def is_on(self):
        return self.state == self.ON

    def calculate_next_state(self, neighbours_on_count):
        if self.state == self.ON and neighbours_on_count != 2 and neighbours_on_count != 3:
            self.next_state = self.OFF
        elif self.state == self.OFF and neighbours_on_count == 3:
            self.next_state = self.ON
        else:
            self.next_state = self.state

    def do_next_state(self):
        self.state = self.next_state

class AlwaysOnLight(Light):
    def __init__(self):
        self.state = self.ON

    def calculate_next_state(self, _):
        self.next_state = self.ON

class Grid:
    def __init__(self, initial_state, special_corner_light = False):
        self.state = []

        for line in initial_state.split('\n'):
            lights_line = []
            for light in line:
                lights_line.append(Light(light))
            self.state.append(lights_line)

        if special_corner_light:
            self.state[0][0] = AlwaysOnLight()
            self.state[0][-1] = AlwaysOnLight()
            self.state[-1][0] = AlwaysOnLight()
            self.state[-1][-1] = AlwaysOnLight()

    def count_lights_on(self):
        count = 0
        for line in self.state:
            for light in line:
                if light.is_on():
                    count += 1
        return count

    def step(self):
        size = len(self.state)
        for x in range(size):
            for y in range(size):
                neighbours_on = self.count_neighbours_on(x, y)
                self.state[x][y].calculate_next_state(neighbours_on)
        
        for x in range(size):
            for y in range(size):
                self.state[x][y].do_next_state()
    
    def count_neighbours_on(self, x, y):
        neighbours_on = 0
        size = len(self.state)

        for i in range(-1, 2):
            if (x + i < 0) or (x + i >= size):
                continue

            for j in range(-1, 2):
                if (y + j < 0) or (y + j >= size):
                    continue

                if i == 0 and j == 0:
                    continue

                if self.state[x + i][y + j].is_on():
                    neighbours_on += 1
        return neighbours_on

    def print(self):
        print("")
        for line in self.state:
            for l in line:
                print(l, end=" ")
            print("")

if __name__ == "__main__":
    initial_state = open('input.txt').read().strip()

    steps = 100

    print("Part 1")
    grid = Grid(initial_state)
    for i in range(steps):
        grid.step()
    lights_on = grid.count_lights_on()
    print(f"After {steps} steps, grid has {lights_on} lights on")

    print("Part 2")
    grid = Grid(initial_state, special_corner_light=True)
    for i in range(steps):
        grid.step()
    lights_on = grid.count_lights_on()
    print(f"After {steps} steps, grid has {lights_on} lights on")
