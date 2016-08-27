import game.game as game
import game.constants.colors as colors
import curses
import argparse

def main(screen):
    """ This is the games main loop.

    - screen: game screen accepted from curses.wrapper(main)
    """
    colors.init_colors()
    
    # Turn off blinking cursor.
    curses.curs_set(0)
    
    main_game = game.EoLGame(80, 20, screen)
    main_game.draw_game()
    curses.doupdate()

    while(True):
        state = main_game.do_turn()
        if state == 'quit':
            break

def parse_arguments():
    parser = argparse.ArgumentParser(description='Play Evolution of Light')
    parser.add_argument("-w",
                        help="Start the game in Wizard Mode",
                        action="store_true")
    parser.parse_args()


# Run main. curses.wrapper() initializes noecho, cbreak and keypad(1)
if __name__ == '__main__':
    
    parse_arguments()
    
    curses.wrapper(main)