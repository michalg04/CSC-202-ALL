# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:
# -----------------------------------------------------------------------------
'''

'''
import tkinter
import random
import random


class Game(object):
    '''
    Module to implement a tic tac toe game
    '''

    square_size = 100
    user_color = 'pink'
    computer_color = 'blue'

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent
        self.frame = tkinter.Frame(parent)
        # register it with a geometry manager
        self.frame.grid()

        # Create the restart button widget
        self.restart_button = tkinter.Button(self.frame, text='RESTART',
                                      width = 10,
                                      command=self.restart)
        self.restart_button.grid()

        # Create a canvas widget
        self.draw_board()
        self.canvas.bind("<Button-1>", self.play)

        # Create a label widget for the win/lose message
        self.message = tkinter.Label(self.frame, text='')
        self.message.grid()


        # Create any additional instance variable you need for the game
        # Initializing rectangle colors
        self.init_board_color()
        self.active = True

    def init_board_color(self):
        '''Initialize a list representing the board '''
        self.board_color = [['white', 'white', 'white'],
                            ['white', 'white', 'white'],
                            ['white', 'white', 'white']]
    def draw_board(self):
        '''Initialize the game board '''
        # create a canvas to draw our board
        self.canvas = tkinter.Canvas(self.frame,
                                     width=self.square_size * 3,
                                     height=self.square_size * 3)
        # register it with a geometry manager
        self.canvas.grid()

        # draw the tiles on the canvas
        for row in range(3):
            for column in range(3):
                color = 'white'
                self.canvas.create_rectangle(
                                             self.square_size * column,
                                             self.square_size * row,
                                             self.square_size * (column + 1),
                                             self.square_size * (row + 1),
                                             fill=color)

    def check_result(self, x, y, color):
        """
        This method checks who won
        Parameters: x (int), y(int) color(string)
        Returns: res (boolean)
        """
        if color == self.user_color:
            mess = 'You'
        else:
            mess = 'Computer'
        res = True
        for i in range(3):
            if self.board_color[x][i] != color:
                res = False
        if res:
            self.message.configure(text=mess + ' won!')
            return res
        res = True
        for i in range(3):
            if self.board_color[i][y] != color:
                res = False
        if res:
            self.message.configure(text=mess + ' won!')
            return res
        res = True
        for i in range(3):
            if self.board_color[i][i] != color:
                res = False
        if res:
            self.message.configure(text=mess + ' won!')
            return res
        res = True
        for i in range(3):
            if self.board_color[i][2-i] != color:
                res = False
        if res:
            self.message.configure(text=mess + ' won!')
            return res

    def play(self, event):
        """
        This method is invoked when the user clicks on the canvas
        It fills the enclosing square with the paint color
        """
        if not self.active:
            return
        rectangle = self.canvas.find_closest(event.x, event.y)
        #print(event.x, event.y)
        x = int(event.y / self.square_size)
        y = int(event.x / self.square_size)
        if self.board_color[x][y] == 'white':
            self.canvas.itemconfigure(rectangle, fill=self.user_color)
            self.board_color[x][y] = self.user_color
            if self.check_result(x,y, self.user_color):
                self.active = False
                return
            else:
                (rx, ry) = self.get_random()
                if rx == -1 and ry == -1:
                    self.message.configure(text='It\'s a tie')
                    self.active = False
                else:
                    self.canvas.itemconfigure(self.find_rectangle(rx,ry), fill=self.computer_color)
                    self.board_color[rx][ry] = self.computer_color
                    if self.check_result(rx, ry, self.computer_color):
                        self.active = False
                        return

    def find_rectangle(self, x, y):
        """
        This method finds the coordinates of the rectangles and returns them
        Parameters: x (int) y(int)
        Returns: rec
        """
        for rec in self.canvas.find_all():
            coords = self.canvas.coords(rec)
            print(coords)
            if (coords[0]/self.square_size) == x and (coords[1]/self.square_size) == y:
                return rec

    def get_random(self):
        """
        This method returns a random coordinate for the computer's turn to play
        """
        random_x = -1
        random_y = -1
        for i in range(3):
            for j in range(3):
                if self.board_color[i][j] == 'white':
                    random_x = i
                    random_y = j
                    return (random_x, random_y)
        return random_x, random_y

    def restart(self):
        """
        This method restarts the tic tac toe game
        """
        #This method is invoked when the user clicks on the RESTART button.
        self.init_board_color()
        for rectangle in self.canvas.find_all():
            self.canvas.itemconfigure(rectangle, fill='white')
        self.message.configure(text='')
        self.active = True

    
def main():
    # Instantiate a root window
    root = tkinter.Tk()

    # Instantiate a Game object
    my_game = Game(root)

    # Enter the main event loop
    root.mainloop()

if __name__ == '__main__':
        main()