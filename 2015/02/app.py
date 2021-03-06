class Box:
    def __init__(self, length: int, width: int, height: int) -> None:
        self.length = length
        self.width = width
        self.height = height

    def __eq__(self, other):
        if (isinstance(other, Box)):
            return self.length == other.length and self.width == other.width and self.height == other.height
        return False

    def needed_wrapping_paper(self) -> int:
        return self.surface_area() + self.smallest_side_area()
    
    def needed_ribbon(self) -> int:
        return self.smallest_perimeter() + self.volume()

    def surface_area(self) -> int:
        l, w, h = self.length, self.width, self.height
        return 2*l*w + 2*w*h + 2*h*l

    def smallest_side_area(self) -> int:
        l, w, h = self.length, self.width, self.height
        return min(l*w, w*h, h*l)
    
    def smallest_perimeter(self) -> int:
        l, w, h = self.length, self.width, self.height
        return min(2*(l+w), 2*(w+h), 2*(h+l))
    
    def volume(self) -> int:
        l, w, h = self.length, self.width, self.height
        return l*w*h

def parse_boxes(boxes_measures):
    result = []
    for box_measures in boxes_measures:
        l, w, h = box_measures.split('x')
        l, w, h = int(l), int(w), int(h)
        result.append(Box(l, w, h))
    return result

def calculate_total_paper_needed(boxes):
    return sum([box.needed_wrapping_paper() for box in boxes])

def calculate_total_ribbon_needed(boxes):
    return sum([box.needed_ribbon() for box in boxes])

if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read().split('\n')

    boxes = parse_boxes(input)
    total_paper_needed = calculate_total_paper_needed(boxes)
    print('Paper needed: ', total_paper_needed, 'ft2')

    total_ribbon_needed = calculate_total_ribbon_needed(boxes)
    print('Ribbon needed: ', total_ribbon_needed, 'ft')
