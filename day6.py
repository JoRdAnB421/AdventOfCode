import numpy as np;
import re, os

# Load the data
data = np.loadtxt(os.path.join('Inputs', 'day6Input.txt'), usecols=[1,2,3,4])
# data = np.loadtxt('day6Test', usecols=[1,2,3])
# print(data)

tm = data[0,:]; D = data[1,:]

'''
We need to solve the quadratic inequality tp^2 - tmtp + D < 0  
Where tp is the time spent pressing the button, tm is the maximum time of the race
and D is the distance we need to beat.
'''

# Find roots of equation 
maximum = (tm + np.sqrt(tm**2 - 4*D))/2
minimum = (tm - np.sqrt(tm**2 - 4*D))/2

# Check if maximum is equal to its floor if so reduce by 1 
maximum[maximum==np.floor(maximum)]-=1

# All integers between the roots are times where we win
# Num of ints found by difference in floor
numWins = np.floor(maximum)-np.floor(minimum)
print(f'Number of ways to win each game {numWins}')

# Product of wins for each game
print(f'Product of number of winning ways {np.prod(numWins).astype(int)}')


####################################
print('############# PART 2#############')
# read data as strings and remove the words/spaces to max 1 number
with open(os.path.join('Inputs', 'day6Input.txt')) as f:
    # Read first time row Strip non-digits 
    tm = int(re.sub(r'[^\d+]', '', f.readline()))

    # Read distance row and strip
    D = int(re.sub(r'[^\d+]', '', f.readline()))


# Find roots of equation 
maximum = (tm + np.sqrt(tm**2 - 4*D))/2
minimum = (tm - np.sqrt(tm**2 - 4*D))/2

# Check if maximum is equal to its floor if so reduce by 1 
if maximum == np.floor(maximum):
    maximum-=1

# All integers between the roots are times where we win
# Num of ints found by difference in floor
numWins = np.floor(maximum)-np.floor(minimum)
print(f'Number of ways to win this one game: {int(numWins)}')

