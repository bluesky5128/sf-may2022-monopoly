from enum import Enum
from dataclasses import dataclass
from levelup.character import Player

DEFAULT_PLAYER_NAME = "Player"


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

map = []
for x in range(10):
  for y in range(10):
    map.append((x, y))

counter: int =0

@dataclass
class GameStatus:
    running: bool = False
    player: Player = Player(DEFAULT_PLAYER_NAME)


class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def create_player(self, player_name: str) -> None:
        if not player_name:
            player_name = DEFAULT_PLAYER_NAME
        self.status.player = Player(player_name)


    def calculate_newposition(self, position, direction: Direction):
        print('direction', direction)
        newposition=position
        if direction==Direction.SOUTH:
            newposition = (position[0], position[1] - 1)
        if direction==Direction.NORTH:
            newposition = (position[0], position[1] +1)
        if direction==Direction.EAST:
            newposition = (position[0]+1, position[1])
        if direction==Direction.WEST:
            newposition = (position[0] - 1, position[1])
        if newposition in map:
            return newposition
        return position

    def move(self, direction: Direction) -> None:
        current_pos = self.status.player.getposition()
        #curr_counter = self.status.player.getCounter()
        print('current position', current_pos)
        print('direction.name',direction.name)
        #new_counter = self.status.player.updatecounter(curr_counter)
        #print('counter', curr_counter)
        new_pos = self.calculate_newposition(current_pos, direction)
        #self.status.player.setposition(new_pos)
        #self.status.player.setcounter(new_counter)
        print('new position',new_pos)
        print('curr position',current_pos)
        print('map',map)
        counter = counter + 1
        # is_valid = validate_newposition(new_pos)
        

