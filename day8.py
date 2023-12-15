import numpy as np
import os, ast

# Load the file
mapping = {}

with open(os.path.join('Inputs', 'day8Input.txt'), 'r') as f:
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
        
