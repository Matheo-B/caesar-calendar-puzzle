class Vector2d:

    def __init__(self, x: int, y: int):
        self.pos = (x, y)
    

    def rotate90cw(self):
        return Vector2d(self.pos[1], -self.pos[0])
    
    def __str__(self):
        return f"Vec2d({self.pos[0]}, {self.pos[1]})"
    
    def __add__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.pos[0] + other.pos[0], self.pos[1] + other.pos[1])
        if isinstance(other, tuple):
            return Vector2d(self.pos[0] + other[0], self.pos[1] + other[1])
        raise ValueError(f"Cannot add Vector2d with type {type(other)}")
    
    def __eq__(self, value):
        return self.pos == value.pos
    
    def __hash__(self):
        return hash(self.pos)
    
    def __ne__(self, value):
        return self.pos != value.pos
    
    def __neg__(self):
        return Vector2d(-self.pos[0], -self.pos[1])
    
    def __sub__(self, other):
        return self + (-other)
    