import random

def create_empty_grid(width, height):
    return[["|" for _ in range(width)] for _ in range(height)]

def get_neighbors(x,y,width,height):
    neighbours=[ ]
    if (x>1): neighbours.append((x-2,y))
    if (x<1): neighbours.append((x+2,y))
    if (y>1): neighbours.append((y-2,x))
    if (y<1): neighbours.append((y+2,y))
    return neighbours

def generate_grid(grid,x,y,width,height):
    grid[y][x]=""
    neighbours=get_neighbors(x,y,width,height)
    random.shuffle(neighbours)
    for nx, ny, in neighbours:
        if grid[nx][ny]=="|":
            grid[(y+ny)//2][(x+nx)//2]='_'
            generate_grid(grid,nx,ny,width,height)

def print_grid(grid):
    for row in grid: 
        print(" ".join(row))

def user_move(grid,x,y,dx,dy):
    new_x = x+dx
    new_y=y+dy
    
    if grid[new_y][new_x] != "|":
        grid[y][x]=' '
        grid[new_y][new_x] != "p"
        return new_x, new_y
    
    return x,y
def main( ):    
    width = 25
    height = 25

    if width % 2 == 0 or height % 2 ==0:
        raise ValueError("width and height should be odd numbers.")

    maze_grid = create_empty_grid(width,height)
    start_x, start_y= 1,1

    generate_grid(maze_grid, start_x, start_y, width, height)
    maze_grid[start_y][start_x] = 'p'
    maze_grid[height - 2][width - 2] = 'X'

    print("welcome to the game")
    print("use 'w', 'a', 's', 'd', to move. press q to quit")
    print_grid(maze_grid)
    
    player_x, player_y, = start_x, start_y
    
    while maze_grid[player_y][player_x] != 'X':
        direction = input("enter direction: ").lower()

        if direction == 'q':
            print("thanks for playing")
            break

        if direction == 'w':
            player_x, player_y = move_player(maze_grid, player_x, player_y, 0, -1)
        elif direction == 'a':
            player_x, player_y = move_player(maze_grid, player_x, player_y, -1, 0)
        elif direction == 's':
            player_x, player_y = move_player(maze_grid, player_x, player_y, 0, 1)
        elif direction == 'd':
            player_x, player_y = move_player(maze_grid, player_x, player_y, 1, 0)

        print_grid(maze_grid)

    if maze_grid[player_y][player_x] == 'X':
        print("you reached the goal")
if __name__=="__main__":
    main()