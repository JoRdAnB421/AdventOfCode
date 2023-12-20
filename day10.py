import numpy as np
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
                print(_, check)
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

print(coords)
print(route)

print(f'Total length of route is {len(coords)}')
print(f'Max distance from start is {int(np.floor(len(coords)/2))}')