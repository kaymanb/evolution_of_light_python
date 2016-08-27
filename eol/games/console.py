import constants.colors as colors
import curses


def init_console(x, y, width, height):
    global STD
    STD = ConsoleManager(x, y, width, height)



class ConsoleManager:
    """ A class for managing output to the console. 
    """

    def __init__(self, x, y, width, height):
        """ Creates the console window at the input position with the given
        dimensions.
        """
        self.win = curses.newwin(height, width, y, x)
        self.win.addstr(0, 0, "Welcome to EoL!")
        self.win.refresh()
   
    def log(self, msg):
        
        # TODO: Make logs move and persist for a bit, also maybe write to file.
        self.win.erase()
        
        self.win.addstr(0, 0, msg)
        self.win.refresh()
