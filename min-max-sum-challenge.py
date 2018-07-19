import  sys

IntList = list(map(int, input('Enter a line of space-separated integers ').strip().split(' ')))
maximum = max(IntList)
minimum = min(IntList)

sumIntList = sum(IntList)

print(sumIntList - maximum, sumIntList - minimum)