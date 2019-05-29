import pygame



pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
LIGHT_BLUE = (0,255,255)

a=pygame.mixer.music.load("lagu.mp3")
pygame.mixer.music.play(-1)


class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """

    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image = pygame.image.load("naga.png").convert()

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom



class Room(object):
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):
    """This creates all the walls in room 1"""

    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 300, WHITE],
                 [0, 300, 20, 300, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE]
                 ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):
    """This creates all the walls in room 2"""

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250,  BLUE],
                 [780, 350, 20, 250, LIGHT_BLUE],
                 [20, 0, 760, 20, GREEN],
                 [20, 580, 760, 20, RED],
                 [150, 20, 20, 500, GREEN],
                 [590, 60, 20, 550, GREEN]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):
    """This creates all the walls in room 3"""

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)
class Room4(Room):
    """This creates all the walls in room 1"""

    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [100,40, 20, 540, RED],
                 [50, 20, 20, 540, GREEN],
                 [200, 40, 20, 540, BLUE],
                 [150, 20, 20, 540, GREEN],
                 [300, 40, 20, 540, PURPLE],
                 [250, 20, 20, 540, LIGHT_BLUE],
                 [400, 40, 20, 540, RED],
                 [350, 20, 20, 540, GREEN],
                 [500, 40, 20, 540, BLUE],
                 [450, 20, 20, 540, GREEN],
                 [600, 40, 20, 540, PURPLE],
                 [550, 20, 20, 540, LIGHT_BLUE],
                 [700, 40, 20, 540, RED],
                 [650, 20, 20, 540, GREEN],
                 ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)



class Room5(Room):
    """This creates all the walls in room 1"""

    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [20,230, 100, 20, RED],
                 [20, 350, 100, 20, RED],
                 [100, 20, 20, 230, RED],
                 [100, 350, 20, 230, RED],
                 [150, 40, 20, 520, RED],
                 [150, 40, 200, 20, RED],
                 [350, 40, 20, 60, RED],
                 [390, 20, 20, 500, RED],
                 [150, 80, 200, 20, RED],
                 [190, 120, 220,20, RED],
                 [150, 160, 220, 20, RED],
                 [190, 200, 220, 20, RED],
                 [150, 240, 220, 20, RED],
                 [190, 280, 220, 20, RED],
                 [150, 320, 220, 20, RED],
                 [190, 360, 220, 20, RED],
                 [150, 400, 220, 20, RED],
                 [190, 440, 220, 20, RED],
                 [150, 480, 220, 20, RED],
                 [150, 540, 620, 20, RED],
                 [430, 40, 20, 500, BLUE],
                 [470, 20, 20, 500, PURPLE],
                 [510, 40, 20, 500, GREEN],
                 [550, 20, 20, 500, LIGHT_BLUE],
                 [590, 40, 20, 500, WHITE],
                 [630, 20, 20, 500, LIGHT_BLUE],
                 [670, 40, 20, 500, WHITE],
                 [710, 20, 20, 500, LIGHT_BLUE],



                 ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)



def main():
    """ Main Program """


    font = pygame.font.SysFont("comicsans", 30, True)
    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])

    # Set the title of the window
    pygame.display.set_caption('Maze Runner')

    # Create the player paddle object
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    room = Room4()
    rooms.append(room)

    room = Room5()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False


    while not done:

        # --- Event Processing ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

        # --- Game Logic ---


        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 4
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 1:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 3:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 4:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 790

            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0

            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0

            elif current_room_no == 2:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 0

            elif current_room_no == 3:
                current_room_no = 4
                current_room = rooms[current_room_no]
                player.rect.x = 0


            else:
                current_room_no = 5
                current_room = rooms[current_room_no]
                player.rect.x = 0

        # --- Drawing ---
        screen.fill(BLACK)

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()