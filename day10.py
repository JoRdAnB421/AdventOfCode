import numpy as np
import matplotlib.pyplot as plt
import os

# Make a dictionary of all moves
moves = {'|':'NS',
         '-':'EW',
         'L':'NE',
         'J':'NW',
         '7':'SW',
         'F':'SE',
}

with open(os.path.join('Inputs', 'day10Input.txt'),'r') as f:
    # Open map and find the start
    mapping=[]
    for i, line in enumerate(f):
        line = line.strip()
        mapping.append(line)
        
        if 'S' in line:
            # If start is found record row and column
            startpos = (i, line.find('S')) 

def CheckStep(currPos, pipe, direction, mapping=mapping, moves=moves):
    '''
    Finds the next possible step based on what has come before
    and the pipes layout
    '''
    # Define looking proceures
    def lookNorth(currPos):
        # Look North if not at top
        if currPos[0]==0:return

        pipe=mapping[currPos[0]-1][currPos[1]]
        if pipe=='S':
            # If reached the end
            return [(currPos[0]-1, currPos[1]), 'END']
        if pipe not in moves.keys():
            return
        if 'S' in moves[pipe]:
            # Step if allowed
            return [(currPos[0]-1, currPos[1]), 'S']
        else: return

    def lookSouth(currPos):    
        # Look south if not at bottom
        if currPos[0]+1==len(mapping):return
        pipe=mapping[currPos[0]+1][currPos[1]]
        if pipe=='S':
            # If reached the end
            return [(currPos[0]+1, currPos[1]), 'END']
        if pipe not in moves.keys():
            return
        if 'N' in moves[pipe]:
            # Step if allowed
            return [(currPos[0]+1, currPos[1]), 'N']
        else: return

    def lookEast(currPos):  
        # Look East if not at side
        if currPos[1]+1==len(mapping[0]): return
        pipe=mapping[currPos[0]][currPos[1]+1]
        if pipe=='S':
            # If reached the end
            return [(currPos[0], currPos[1]+1), 'END']
        if pipe not in moves.keys():
            return
        if 'W' in moves[pipe]:
            # Step if allowed
            return [(currPos[0], currPos[1]+1), 'W']
        else: return

    def lookWest(currPos):
        # Look West if not at side
        if currPos[1]==0:return
        pipe=mapping[currPos[0]][currPos[1]-1]
        if pipe=='S':
            # If reached the end
            return [(currPos[0], currPos[1]-1), 'END']
        if pipe not in moves.keys():
            return
        if 'E' in moves[pipe]:
            # Step if allowed
            return [(currPos[0], currPos[1]-1), 'E']
        else: return

    looking = {'N': lookNorth, 
               'S':lookSouth,
               'E':lookEast,
               'W':lookWest}
    
    
    if pipe=='S':
        print('At start')
        # If at start look in all directions for connecting pipes
        for _,look in looking.items():
            check = look(currPos)
            if check:
                return(check)
            
    else:
        assert direction!=None, "Direction not updated" # Ensure we have stepped
        # Look to next step
        look = looking[direction]
        check = look(currPos)
        if check:
            return(check)


# List for the positions
coords = [startpos]
route=[mapping[coords[-1][0]][coords[-1][1]]]
dirlook=None # First step could be any direction

end=False
while not end:
    # Set current position and pipe state
    pos = coords[-1]
    pipe = route[-1]
    
    # Find next step, and direction we step
    newpos, dirCame = CheckStep(pos, pipe, dirlook)    

    # Append new position and pipe state
    coords.append(newpos)
    route.append(mapping[newpos[0]][newpos[1]])

    if route[-1] == 'S':
        # If we have returned to the start stop the loop
        print('returned')
        end=True

    else:
        # Find next place for the pipe
        pipeType = moves[route[-1]]
        dirlook=pipeType.replace(dirCame,'')

# print(coords)
# print(route)

print(f'Total length of route is {len(coords)}')
print(f'Max distance from start is {int(np.floor(len(coords)/2))}')


###### PART B ######
print('\n####### Part B #######\n')

def PointOnEdge(x, y, p1x, p1y, p2x, p2y):
    """
    Check if the point (x, y) lies exactly on the edge (p1x, p1y) to (p2x, p2y).
    """
    if min(p1x, p2x) <= x <= max(p1x, p2x) and min(p1y, p2y) <= y <= max(p1y, p2y):
        if (p2x - p1x) * (y - p1y) == (x - p1x) * (p2y - p1y):
            return True
    return False

def PointInsideLoop(x, y, loop):
    """
    Determine if the point (x, y) is inside the given polygon.
    Polygon is a list of tuples, each representing a vertex.

    Ray-casting algorithm, essentially shooting a ray horizontally
    from a give point, if the ray passes through an odd number of edges
    then the origin point lies in the polygon, otherwise it is outside

    returns true if point is inside loop
    """
    n = len(loop)
    inside = False

    p1x, p1y = loop[0] # Coords of testing point
    for i in range(n + 1):
        # Loop through vertices of the loop
        p2x, p2y = loop[i % n] 
        if PointOnEdge(x, y, p1x, p1y, p2x, p2y):
            return False  # Exclude points on the edge
        # Check if it crosses an edge of the loop
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    # If the edge is vertical, check if left of vertex
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

def CountPointsInLoop(loop):
    """
    Count the number of integer points inside the polygon.
    """
    # Find the bounding box (reduces number to check through)
    min_x = min(loop, key=lambda p: p[0])[0]
    max_x = max(loop, key=lambda p: p[0])[0]
    min_y = min(loop, key=lambda p: p[1])[1]
    max_y = max(loop, key=lambda p: p[1])[1]

    # Count points in the polygon
    count = 0
    insideCoords=[]
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if PointInsideLoop(x, y, loop):
                count += 1
                insideCoords.append((x,y))
            
            print(f'x search {x/(max_x+1):.0%} --- y search {y/(max_y+1):.0%}', end='\r')

    return count, insideCoords

numPoints, insideCoords = CountPointsInLoop(coords)
print(f'There are {numPoints} inside of the loop')

x, y = zip(*coords)
inx, iny = zip(*insideCoords)

plt.plot(x, y)
plt.plot(inx, iny, 'x', color='black')
plt.show()