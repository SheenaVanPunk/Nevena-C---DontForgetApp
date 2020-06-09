class Circle:

    def __init__(self, radius):
        self._radius = radius

    def compute_area(self):
        return 3.14 * (self._radius * self._radius)

    def compute_perimeter(self):
        return 2*3.14*self._radius



