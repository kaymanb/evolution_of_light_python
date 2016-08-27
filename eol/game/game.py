from levels.levels import Level
from maps.maps import Room
from game.input import InputHandler
from chars.chars import Character
import curses

class EoLGame:
    
    def __init__(self, x, y, screen):
        
        self.size_x = x
        self.size_y = y
        self.levels = [Level(x, y)]
        self.current_level = self.levels[0]
       
        
        start_room = self.current_level.level_map.rooms[0]
        (start_x, start_y) = start_room.list_floorspace()[0]
        start_tile = self.current_level.level_map.get_tile(start_x, start_y) 
        self.player = Character(start_tile, '@', curses.color_pair(1))

        self.screen = screen

    def draw_game(self):
        self.current_level.draw_all(self.screen, self.player)
    
    def do_turn(self):
        state = self.handle_input()
        self.run_npcs()
        return state

    def run_npcs(self):
        for npc in self.current_level.npcs:
            npc.wander(self.current_level.level_map)
            #npc.sentry(self.current_level.level_map)

    def handle_input(self):
        key = self.screen.getch()
        new = InputHandler(self.screen, self.current_level,self.player)
        state = new.handle_input(key)

        self.draw_game()
        curses.doupdate()
        return state