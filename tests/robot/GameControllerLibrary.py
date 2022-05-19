from levelup.controller import GameController


class GameControllerLibrary:
     
    def initialize_controller(self):
        self.controller = GameController()

   
    
    def create_player_with_name(self, playername):
        self.controller.create_player(playername)

    def player_name_should_be(self, expected):
        if self.controller.status.player.name != expected:
            raise AssertionError(
                "%s != %s" % (self.controller.status.player.name, expected)
            )

    def move_player(self, direction):
        pass

    def existing_position_should_be(self, expected):
        pass

    def position_should_be(self, expected):
        if self.controller.status.player.position != expected:
            raise AssertionError(
                "%s != %s" % (self.controller.status.player.position, expected)
            )

    def increment_count (self, count):
         return count+1  

    def update_count(self, count):     
          count = count
    
    def set_player_position():
       pass

    def current_position_should_be(self, expected):
        if self.controller.status.player.position == expected:
            raise AssertionError(
                "%s != %s" % (self.controller.status.player.position, expected)
            )