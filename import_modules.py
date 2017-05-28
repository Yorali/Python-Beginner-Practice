
import module_practice as mp #can use -as ~- to assign a shortcut name to call

#To import individual bits from module without using above:
from module_practice import find_index, test #can also use -as ~ here

emotions = ['Regret','Sorrow','Wrath','Avarice']

index = mp.find_index(emotions, 'Sorrow')
print (index)


index2 = find_index(emotions, 'Wrath') #Thanks to from ... in line 5
print (index)

print(test)


# Standard Library Modules #






