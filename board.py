import pygame
from constants import BLACK, GRAY, RED, GREEN, YELLOW, SIZE, PADDING

class Board:
    def __init__(self):
        self.board_string = ""
        self.map = {}
        self.rows = 0
        self.cols = 0
        self.g_score = {}
        self.f_score = {}
        self.came_from = {}
        
    def __repr__(self):
        return str(self.map)
   
    # legend -  R, G, Y: current location of red, green, yellow markers
    #           r, g, y: target location of red, green, yellow markers
    #           * obstacles
    #           <space> empty
    def read_in_board_string(self, board_string):
        self.board_string = board_string
        self.rows = self.board_string.count("|") // 2
        self.cols = self.board_string.count("-") // 2
        bcounter = 0
        for row_count in range(self.rows):
            for col_count in range(self.cols):
                while True:
                    letter = self.board_string[bcounter]
                    if letter in ("RGYrgy *"):
                        break
                    else:
                        bcounter += 1
                if letter in "RGYrgy":
                    self.map[letter] = (row_count, col_count)
                elif letter == "*":
                    existing_list = self.map.get(letter, [])
                    existing_list.append((row_count, col_count))
                    self.map[letter] = existing_list
                else:
                    pass
                bcounter += 1

    # calclated new location after proposed move (UDLR)
    # for a single piece (RG or Y)
    def return_proposed(self, piece, move):
        current = self.map[piece]
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
        elif proposed == self.map["R"]:
            return self.can_i_move("R", move)
        elif proposed == self.map["G"]:
            return self.can_i_move("G", move)
        elif proposed == self.map["Y"]:
            return self.can_i_move("Y", move)
        else:
            return True
    
    def move(self, move):
        rmove, gmove, ymove = tuple(self.can_i_move(piece, move) for piece in "RGY")
        # print('move request from ', self.get_node())
        if rmove:
            self.map["R"] = self.return_proposed("R", move)
        if gmove:
            self.map["G"] = self.return_proposed("G", move)
        if ymove:
            self.map["Y"] = self.return_proposed("Y", move)
        # print('moved:', rmove or gmove or ymove, 'now', self.get_node())
        return rmove or gmove or ymove
    
    def reconstruct_path(self, node):
        total_path = []
        while True:
            next_node = self.came_from.get(node, None)
            if next_node:
                diffx = (node[0][0] - next_node[0][0]) + (node[1][0] - next_node[1][0]) + (node[2][0] - next_node[2][0])
                diffy = (node[0][1] - next_node[0][1]) + (node[1][1] - next_node[1][1]) + (node[2][1] - next_node[2][1])
                if diffx >= 1:
                    insertword = '↓'
                elif diffx <= -1:
                    insertword = '↑'
                elif diffy >= 1:
                    insertword = '→'
                elif diffy <= -1:
                    insertword = '←'
                else:
                    break
                node = next_node
                total_path.insert(0, insertword)
            else:
                break
        return "".join(total_path)
    
    def find_path(self):
        start = self.get_node()
        finish = self.get_finish()
        open_set = [start]
        closed_set = []
        self.set_g(start, 0)
        while open_set:
            current = open_set[0]
            if current == finish:
                return self.reconstruct_path(current)
            open_set.remove(current)
            closed_set.append(current)
            for neighbor in self.get_neighborhood(current):
                tent_g = self.get_g(current) + 1
                if tent_g < self.get_g(neighbor):
                    self.came_from[neighbor] = current
                    self.set_g(neighbor, tent_g)
                    self.set_f(neighbor, tent_g + self.heuristic(neighbor, finish))
                    if neighbor not in open_set and neighbor not in closed_set:
                        open_set.append(neighbor)
                        open_set.sort(key=lambda x:self.get_f(x))
        return False

    def get_neighborhood(self, node):
        orig_posn = self.get_node()
        self.set_node(node)
        neighbors = []
        for amove in "→←↑↓":
            if self.move(amove):
                neighbors.append(self.get_node())
            self.set_node(node)
        self.set_node(orig_posn)
        return neighbors

    def get_finish(self):
        return tuple(self.map[piece] for piece in "rgy")

    def get_node(self):
        return tuple(self.map[piece] for piece in "RGY")

    def set_node(self, position):
        self.map["R"] = position[0]
        self.map["G"] = position[1]
        self.map["Y"] = position[2]

    def get_g(self, node):
        return self.g_score.get(node, float('inf'))

    def get_f(self, node):
        return self.f_score.get(node, float('inf'))

    def set_g(self, node, value):
        self.g_score[node] = value
    
    def set_f(self, node, value):
        self.f_score[node] = value

    # manhattan distance heuristic
    # def heuristic(self, node, finish):
    #     diffr = abs(node[0][0] - finish[0][0]) + abs(node[0][1] - finish[0][1])
    #     diffg = abs(node[1][0] - finish[1][0]) + abs(node[1][1] - finish[1][1])
    #     diffy = abs(node[2][0] - finish[2][0]) + abs(node[2][1] - finish[2][1])
    #     return max([diffr, diffg, diffy])
    
    # squared euclidean distance (maybe not admissible)
    def heuristic(self, node, finish):
        diffr = (node[0][0] - finish[0][0])**2 + (node[0][1] - finish[0][1])**2
        diffg = (node[1][0] - finish[1][0])**2 + (node[1][1] - finish[1][1])**2
        diffy = (node[2][0] - finish[2][0])**2 + (node[2][1] - finish[2][1])**2
        return max([diffr, diffg, diffy])

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(win, GRAY, (col * SIZE + PADDING // 2, row * SIZE + PADDING // 2, SIZE - PADDING // 2, SIZE - PADDING // 2))
    

    def draw(self, win):
        self.draw_squares(win)
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) == self.map["R"]:
                    pygame.draw.circle(win, RED, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING)
                elif (row, col) == self.map["G"]:
                    pygame.draw.circle(win, GREEN, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING)
                elif (row, col) == self.map["Y"]:
                    pygame.draw.circle(win, YELLOW, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING)
                elif (row, col) == self.map["r"]:
                    pygame.draw.circle(win, RED, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING, width=PADDING)
                elif (row, col) == self.map["g"]:
                    pygame.draw.circle(win, GREEN, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING, width=PADDING)
                elif (row, col) == self.map["y"]:
                    pygame.draw.circle(win, YELLOW, (col * SIZE + SIZE // 2, row * SIZE + SIZE // 2), SIZE // 2 - PADDING, width=PADDING)
                elif (row, col) in self.map["*"]:
                    pygame.draw.rect(win, BLACK, (col * SIZE + PADDING, row * SIZE + PADDING, SIZE - 2*PADDING, SIZE - 2*PADDING))
                
                    