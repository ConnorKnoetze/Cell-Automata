import pygame as py
import random

py.init()

# Set up the display
screen_width, screen_height = 1000, 1000
screen = py.display.set_mode((screen_width, screen_height), )
py.display.set_caption("Cellular Automata")

class cell():
    def __init__(self, coords, state=False):
        self.coords = coords
        self.size = 10
        self.state = state
        self.rect = py.Rect(coords[0], coords[1], self.size, self.size)
    
    def __str__(self):
        return str(self.rect)
    
    def get_state(self):
        return self.state
    
    def draw(self):
        if self.state:
            py.draw.rect(screen, (255, 255, 255), self.rect)
        else:
            py.draw.rect(screen, (20, 20, 20), self.rect, width=1)
    
    def is_edge(self):
        if self.coords[0] == 0 or self.coords[0] == 990 or self.coords[1] == 0 or self.coords[1] == 990:
            return True
        else: return False
    
    def kill(self):
        self.state = False

    def toggle(self):
        self.state = not self.state

class display():
    def __init__(self):
        self.size = screen_width // 10, screen_height // 10
        self.board = [[cell((x*10, y*10)) for x in range(self.size[0])] for y in range(self.size[1])]

        for line in self.board:
            for c in line:
                if random.randint(0, 1):
                    c.toggle()

        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                           (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def draw(self):
        for item in self.board:
            for c in item:
                c.draw()

    def life(self):
        nextGen = [[cell((x*10, y*10), self.board[y][x].get_state()) for x in range(self.size[0])] for y in range(self.size[1])]

        for i in range(len(self.board)):
            for j, c in enumerate(self.board[i]):
                live = 0

                for dx, dy in self.directions:
                    x, y = i + dx, j + dy

                    if 0 <= x < self.size[1] and 0 <= y < self.size[0] and self.board[x][y].get_state():
                        live += 1

                if c.get_state():
                    if live < 2 or live > 3:
                        nextGen[i][j].kill()
                else:
                    if live == 3:
                        nextGen[i][j].toggle()
        
        self.board = nextGen
        self.draw()
        

def main():
    screen_size = py.display.get_window_size()
    print(screen_size)

    clock = py.time.Clock()

    board = display()

    running = True
    while running:
            

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        screen.fill((0, 0, 0))

        board.life()

        py.display.flip()
        clock.tick(5)

    py.quit()



if __name__ == "__main__":
    main()


