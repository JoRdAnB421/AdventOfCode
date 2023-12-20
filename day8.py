import numpy as np
import os, math
from functools import reduce

parta = input('Solve part a?[y/n]')
if parta=='y':
    # Load the file
    mapping = {}

    with open(os.path.join('Inputs', 'day8Test'), 'r') as f:
        moves = f.readline().strip() # Read first line, remove \n

        for line in f:
            line = line.strip()
            if not line: # Skip empty lines
                continue

            # Define key and items
            key, value = line.strip().split('=')
            key = key.strip()

            # Manually construct the tuple
            value = value.strip().strip('()') 
            value = tuple(value.split(', ')) 

            # Fill dictionary
            mapping[key] = value


    counter=0
    start='AAA'; currentPos = mapping[start]
    moves=moves.replace('L', '0').replace('R','1') # Easy to index later
    finish=False
    print('Start ' + start)
    while not finish:
        # Keep searching till 'ZZZ' is found
        for i in moves:
            counter+=1
            i=int(i) # Make integer 
            newPos = currentPos[i] # Find new position
            print('Step to ' + newPos)

            if newPos == 'ZZZ':
                # If final step found break
                print('\nFound ' + newPos + f' in {counter} steps.')
                finish=True
                break
            
            currentPos=mapping[newPos]


###### Part B #######
print('\n############Part B############\n')


mapping = {}

startlist=[] # All keys ending in A
with open(os.path.join('Inputs', 'day8Input.txt'), 'r') as f:
    moves = f.readline().strip() # Read first line, remove \n

    for line in f:
        line = line.strip()
        if not line: # Skip empty lines
            continue

        # Define key and items
        key, value = line.strip().split('=')
        key = key.strip()

        # If key ends in A add to start list 
        if key[-1]=='A':
            startlist.append(key)

        # Manually construct the tuple
        value = value.strip().strip('()') 
        value = tuple(value.split(', ')) 

        # Fill dictionary
        mapping[key] = value

startlist=np.asarray(startlist)
print(startlist)

# currentPoslist = np.array([mapping[start] for start in startlist]) # Current position is all of the 
moves=moves.replace('L', '0').replace('R','1') # Easy to index later

#### TESTING ####
lim=1e5
points = []
print(points)

for j in startlist:
    found=False
    counter=0
    startPos=j
    currentPos=mapping[startPos]
    test = {}

    while not found:
        for i in moves:
            counter+=1
            i = int(i)
            newPos = currentPos[i]
            # print(newPos)
            if newPos[-1]=='Z':
                # When 'Z' term is found skip to the next start position
                test[newPos] = (startPos, currentPos, counter)
                points.append(counter)
                found=True
                break
            currentPos = mapping[newPos]

# Make into array
points = np.asarray(points, dtype='int64')

print(points)

def lcm(a, b):
    # Find the Lowest common multiple
    return abs(a*b) // math.gcd(a, b)

# Calculating the LCM for a list of numbers
lcm_result = reduce(lcm, points)

print(f'All start points reach final Z at step {lcm_result}')