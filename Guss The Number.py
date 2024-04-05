print('Guss The Number\n---------------')

import random

while True :
    print('Enter Lower range of number')
    lower_range = input('  : ')
    print('Enter Higher range of number')
    heigher_range = input('  : ')

    try :
        lower_range = int(lower_range)
        heigher_range = int(heigher_range)
    except :
        print('Error : Make sure that you entered numbers')
        continue

    