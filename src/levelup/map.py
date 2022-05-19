class Map:
    _width: int
    _height: int
    
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height
    
    def is_valid_position(self, position):
        return (position[0] >= 0 and position[0] < self.get_width()) and (position[1] >= 0 and position[1] < self.get_height())
    