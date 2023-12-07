import numpy as np
import os 

# Setting card strengths [reversed so index follows card relative strength]
cards = np.array(['A','K','Q','J','T','9', '8','7','6','5','4','3','2'])[::-1]
vals = np.arange(10, 10+len(cards)+1).astype(str) # Start from 10 so that every let has a 2 digit code
cardStrength = {cards[i]: vals[i] for i in range(len(cards))}

def OrderHands(hands, index, strength = cardStrength):
    '''
    Orders hands based on the highest card going through the cards
    '''
    # Select only the required hand states
    temp = hands[index]
    
    # Convert hand to an integer based on each card strength
    converted=[]
    for tmp in temp:
        codedInt = int(''.join([cardStrength[i] for i in tmp]))
        converted.append(codedInt)
    codedInt = np.asarray(codedInt)

    # Find indices of these converted integers
    ind = np.asarray(np.argsort(converted), dtype='int64')

    return index[0][ind]



# Load the hands
data = np.loadtxt(os.path.join('Inputs', 'day7Input.txt'), dtype=str)

# Loop through hand and find all of the groups of hands
# i.e., number of unique characters
hands = np.array([np.asarray(list(hand)) for hand in data[:,0]])

# Sort hands by number of unique characters
counts = np.array([[max(np.unique(hand, return_counts=True)[1]), 
                    len(np.unique(hand, return_counts=True)[1])] for hand in hands])

# Indices for all hand possibilities
fiveKind = np.where(counts[:,0]==5)
fourKind = np.where(counts[:,0]==4)
fullHouse = np.where((counts[:,0]==3)&(counts[:,1]==2))
threeKind = np.where((counts[:,0]==3)&(counts[:,1]==3))
twopair = np.where((counts[:,0]==2)&(counts[:,1]==3))
onepair = np.where((counts[:,0]==2)&(counts[:,1]==4))
highCard = np.where(counts[:,0]==1)


indices = [fiveKind, fourKind, fullHouse, threeKind, twopair, onepair, highCard]

finalOrder = np.array([], dtype='int64')
# Loop through the hand indexes to order in kind 
for index in indices:
    if len(index[0])==1:
        # If only one hand no need to sort order
        finalOrder = np.append(finalOrder, index[0])
    else:
        # Sort sub group of hands into order then append to total order
        newIndex = OrderHands(data[:,0], index)[::-1]
        finalOrder = np.append(finalOrder, newIndex).astype('int64')

# Sort all hands
sortedData = data[finalOrder][::-1]

# Find bids and make array the same length of consecutive rank numbers
bids = sortedData[:,1].astype('int64')
ranks = np.arange(1, len(bids)+1)

print(f'Total winnings of this set of hands {sum(bids*ranks)}')


########## PART 2 #############
print('\n###########PART 2#############\n')

print('Playing with J as Joker not Jack!\n')

# Setting card strengths [reversed so index follows card relative strength]
cards = np.array(['A','K','Q','T','9', '8','7','6','5','4','3','2','J'])[::-1]
vals = np.arange(10, 10+len(cards)+1).astype(str) # Start from 10 so that every let has a 2 digit code
cardStrength = {cards[i]: vals[i] for i in range(len(cards))}

# Load the hands
data = np.loadtxt(os.path.join('Inputs', 'day7Input.txt'), dtype=str)

# Loop through hand and find all of the groups of hands
# i.e., number of unique characters
hands = np.array([np.asarray(list(hand)) for hand in data[:,0]])

# Sort hands by number of unique characters
counts=[]
for hand in hands:
    card, count = np.unique(hand, return_counts=True)
    if (len(card)==1)&(card[0]=='J'):
        counts.append([0,0])
    else:
        counts.append([max(count[card!='J']), len(count[card!='J'])])
counts = np.asarray(counts)

# Find the number of Jokers in each hand
jokerCount = np.sum(np.isin(hands, 'J'), axis=1)

# Indices for all hand possibilities
fiveKind = np.where(counts[:,0]+jokerCount==5)
fourKind = np.where(counts[:,0]+jokerCount==4)
fullHouse = np.where((counts[:,0]+jokerCount==3)&(counts[:,1]==2))
threeKind = np.where((counts[:,0]+jokerCount==3)&(counts[:,1]==3))
twopair = np.where((counts[:,0]+jokerCount==2)&(counts[:,1]==3))
onepair = np.where((counts[:,0]+jokerCount==2)&(counts[:,1]==4))
highCard = np.where(counts[:,0]+jokerCount==1)


indices = [fiveKind, fourKind, fullHouse, threeKind, twopair, onepair, highCard]

finalOrder = np.array([], dtype='int64')
# Loop through the hand indexes to order in kind 
for index in indices:
    if len(index[0])==1:
        # If only one hand no need to sort order
        finalOrder = np.append(finalOrder, index[0])
    else:
        # Sort sub group of hands into order then append to total order
        newIndex = OrderHands(data[:,0], index)[::-1]
        finalOrder = np.append(finalOrder, newIndex).astype('int64')

# Sort all hands
sortedData = data[finalOrder][::-1]

# Find bids and make array the same length of consecutive rank numbers
bids = sortedData[:,1].astype('int64')
ranks = np.arange(1, len(bids)+1)

print(f'Total winnings of this set of hands {sum(bids*ranks)}')