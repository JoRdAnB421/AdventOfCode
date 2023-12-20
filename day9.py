import numpy as np 
import os

def FindNextNum(line, bottom=False, extrap='forward'):
    '''
    Looks for differences and then extrapolates initial line =
    '''
    chain=[line]
    while not bottom:
        # Append the difference of all points
        chain.append(np.diff(chain[-1]))
        
        if all(chain[-1]==0):
            bottom=True

    if extrap=='forward':
        # With the chain found now reverse the chain to find the extrapolated first line
        finalnum=0
        for i in chain[::-1]:
            finalnum+=i[-1]

        return finalnum

    elif  extrap=='backward':
        # With the chain found now reverse the chain to find the extrapolated backward first line
        finalnum=0
        for i in chain[::-1]:
            finalnum=i[0] - finalnum

        return finalnum


extrapNums=[]
with open(os.path.join('Inputs', 'day9Input.txt'), 'r') as f:
    # Read each line
    for line in f:
        # Ensure line is read as numbers
        line = np.asarray(line.strip().split(' '), dtype=float)
        
        # Extrapolate first line based on differences
        extrapNums.append(FindNextNum(line))
        

print(f'The sum of extrapolated nums is: {int(np.sum(extrapNums))}')

######## Part 2 #######
print('\n######## Part 2 ########\n')

extrapNums=[]
with open(os.path.join('Inputs', 'day9Input.txt'), 'r') as f:
    # Read each line
    for line in f:
        # Ensure line is read as numbers
        line = np.asarray(line.strip().split(' '), dtype=float)
        
        # Extrapolate first line based on differences
        extrapNums.append(FindNextNum(line, extrap='backward'))
        

print(f'The sum of extrapolated nums is: {int(np.sum(extrapNums))}')
