import re, itertools

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def load(input):
        m = re.match(r'(?P<name>\w*): capacity (?P<capacity>[-\d]*), durability (?P<durability>[-\d]*), flavor (?P<flavor>[-\d]*), texture (?P<texture>[-\d]*), calories (?P<calories>[-\d]*)', input)
        name = m.group('name')
        capacity = int(m.group('capacity'))
        durability = int(m.group('durability'))
        flavor = int(m.group('flavor'))
        texture = int(m.group('texture'))
        calories = int(m.group('calories'))

        return Ingredient(name, capacity, durability, flavor, texture, calories)

class Recipe:
    def __init__(self):
        self.ingredients = {}
        self.capacity = 0
        self.durability = 0
        self.flavor = 0
        self.texture = 0
        self.calories = 0

    def add_ingredient(self, ingredient, ammount):
        self.ingredients[ingredient.name] = ammount
        self.capacity += ammount * ingredient.capacity
        self.durability += ammount * ingredient.durability
        self.flavor += ammount * ingredient.flavor
        self.texture += ammount * ingredient.texture
        self.calories += ammount * ingredient.calories

    def score(self):
        if sum(self.ingredients.values()) != 100:
            raise "Not 100 ingredients yet!"

        capacity = self.capacity if self.capacity > 0 else 0
        durability = self.durability if self.durability > 0 else 0
        flavor = self.flavor if self.flavor > 0 else 0
        texture = self.texture if self.texture > 0 else 0

        return capacity * durability * flavor * texture

def process(file):
    ingredients = []
    for line in open(file):
        ingredient = Ingredient.load(line)
        ingredients.append(ingredient)

    combinations = [p for p in itertools.product(range(1, 101), repeat=len(ingredients)) if sum(p) == 100]

    winner = None
    for combination in combinations:
        recipe = Recipe()
        for i in range(len(ingredients)):
            recipe.add_ingredient(ingredients[i], combination[i])
        if winner is None or recipe.score() > winner.score():
            winner = recipe

    print(f"Winner recipe has score {winner.score()}")

if __name__ == '__main__':
    process('input.txt')
