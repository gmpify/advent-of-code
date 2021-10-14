class Box:
    def __init__(self, length: int, width: int, height: int) -> None:
        self.length = length
        self.width = width
        self.height = height

    def needed_wrapping_paper(self) -> int:
        return self.surface_area() + self.smallest_side_area()

    def surface_area(self) -> int:
        l, w, h = self.length, self.width, self.height
        return 2*l*w + 2*w*h + 2*h*l

    def smallest_side_area(self) -> int:
        l, w, h = self.length, self.width, self.height
        return min(l*w, w*h, h*l)
