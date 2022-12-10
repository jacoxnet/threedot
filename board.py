import pygame
from constants import BLACK, GRAY, RED, GREEN, YELLOW, SIZE, PADDING

class Board:
    def __init__(self, board_string):
        self.board_string = board_string
        self.map = {}
        self.rows = self.board_string.count("|") // 2
        self.cols = self.board_string.count("-") // 2
        self.read_in_board_string()
        
    def __repr__(self):
        return str(self.map)
   
    # legend -  R, G, Y: current location of red, green, yellow markers
    #           r, g, y: target location of red, green, yellow markers
    #           * obstacles
    #           <space> empty
    def read_in_board_string(self):
        bcounter = 0
        for row_count in range(self.rows):
            for col_count in range(self.cols):
                while self.board_string[bcounter] not in ("RGYrgy *"):
                    bcounter += 1
                # no need to record empty spaces
                if self.board_string[bcounter] != " ":
                    thelist = self.map.get(self.board_string[bcounter], [])
                    thelist.append((row_count, col_count))
                    self.map[self.board_string[bcounter]] = thelist
                bcounter += 1

    def return_proposed(self, piece, move):
        current = self.map[piece][0]
        if move == "→":
            proposed = (current[0], current[1] + 1)
        elif move == "←":
            proposed = (current[0], current[1] - 1)
        elif move == "↑":
            proposed = (current[0] - 1 , current[1])
        elif move == "↓":
            proposed = (current[0] + 1, current[1])
        else:
            raise KeyError
        return proposed
    
    def can_i_move(self, piece, move):
        proposed = self.return_proposed(piece, move)
        if proposed[0] < 0 or proposed[0] >= self.rows or proposed[1] < 0 or proposed[1] >= self.cols:
            return False
        elif proposed in self.map["*"]:
            return False
        elif proposed in self.map["R"]:
            return self.can_i_move("R", move)
        elif proposed in self.map["G"]:
            return self.can_i_move("G", move)
        elif proposed in self.map["Y"]:
            return self.can_i_move("Y", move)
        else:
            return True
    
    def move(self, move):
        rmove, gmove, ymove = tuple(self.can_i_move(piece, move) for piece in "RGY")
        if rmove:
            self.map["R"] = [self.return_proposed("R", move)]
        if gmove:
            self.map["G"] = [self.return_proposed("G", move)]
        if ymove:
            self.map["Y"] = [self.return_proposed("Y", move)]
    
    def get_node(self):
        return [self.map[piece][0] for piece in "RGY"]

    def set_node(self, position):
        self.map["R"] = [position[0]]
        self.map["G"] = [position[1]]
        self.map["Y"] = [position[2]]

    # def find_path(self):
        
    #     open_set = [start]
    #     tolls.set_g(start, 0)
        
    #     while open_set:
    #         current = open_set[0]
    #         if current == finish:
    #             return tolls.reconstruct_path(current)
    #         open_set.remove(current)
    #         for neighbor in tolls.get_neighborhood(current):
    #             tent_g = tolls.get_g(current) + tolls.tolls[neighbor]
    #             if tent_g < tolls.get_g(neighbor):
    #                 tolls.came_from[neighbor] = current
    #                 tolls.set_g(neighbor, tent_g)
    #                 if neighbor not in open_set:
    #                     open_set.append(neighbor)
    #                     open_set.sort(key=lambda x:tolls.get_g(x))
    #     return False

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(win, GRAY, (col * SIZE + PADDING // 2, row * SIZE + PADDING // 2, SIZE - PADDING // 2, SIZE - PADDING // 2))
    

    def draw(self, win):
        self.draw_squares(win)
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) in self.map["R"]:
                    pygame.draw.circle(win, RED, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING)
                elif (row, col) in self.map["G"]:
                    pygame.draw.circle(win, GREEN, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING)
                elif (row, col) in self.map["Y"]:
                    pygame.draw.circle(win, YELLOW, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING)
                elif (row, col) in self.map["r"]:
                    pygame.draw.circle(win, RED, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING, width=PADDING)
                elif (row, col) in self.map["g"]:
                    pygame.draw.circle(win, GREEN, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING, width=PADDING)
                elif (row, col) in self.map["y"]:
                    pygame.draw.circle(win, YELLOW, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING, width=PADDING)
                elif (row, col) in self.map["*"]:
                    pygame.draw.rect(win, BLACK, (col * SIZE + PADDING, row * SIZE + PADDING, SIZE - 2*PADDING, SIZE - 2*PADDING))
                
                    