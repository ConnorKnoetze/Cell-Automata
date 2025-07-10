import pygame as py
import random

py.init()

# Set up the display
screen_width, screen_height = 1000, 1000
screen = py.display.set_mode((screen_width, screen_height), )
py.display.set_caption("Cellular Automata")

class cell():
    def __init__(self, coords):
        self.coords = coords
        self.size = 10
        self.state = False
        self.rect = py.Rect(coords[0], coords[1], self.size, self.size)
        self.r_rand = random.randint(50,255)
        self.g_rand = random.randint(50,255)
        self.b_rand = random.randint(50,255)
    
    def __str__(self):
        return str(self.rect)
    
    def get_state(self):
        return self.state
    
    def draw(self):
        if self.state:
            py.draw.rect(screen, (self.r_rand, self.g_rand, self.b_rand), self.rect)
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

        self.board[random.randint(1, 98)][random.randint(1, 98)].toggle()

        
    
    def draw(self):
        for item in self.board:
            for c in item:
                c.draw()

    def life(self):
        for i in range(len(self.board)):
            for y, c in enumerate(self.board[i]):
                if c.is_edge():
                    c.kill()
                else:
                    neighbours = self.neighbours((i, y))
                    if self.is_full(neighbours):
                        c.kill()
                    
                    else:
                        n_weight = 0
                        for line in neighbours:
                            for z in line:
                                if z.get_state():
                                    n_weight += 1
                        
                        if n_weight > 3:
                            c.kill()
                        else:
                            for line in neighbours:
                                for z in line:
                                    if not z.get_state():
                                        z.toggle()
                                    else:
                                        z.kill

    def neighbours(self, pos):
        neighbours=[[self.board[i+pos[0]][j+pos[1]] for j in range(-1, 2, 1) if (i,j) != (0,0)] for i in range(-1, 2, 1)]
        return neighbours
    
    def is_full(self, n):
        for line in n:
            for c in line:
                if not c.get_state():
                    return False
        
        return True

        

def main():
    screen_size = py.display.get_window_size()
    print(screen_size)

    # Set up the clock for controlling the frame rate
    clock = py.time.Clock()

    board = display()

    # Main game loop
    running = True
    while running:
            

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        # Fill the screen with a background color (e.g., black)
        screen.fill((0, 0, 0))

        board.life()

        board.draw()

        # Update the display
        py.display.flip()
        clock.tick(5)

    py.quit()



if __name__ == "__main__":
    main()


