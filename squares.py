squares=[]
for value in range(1,10):
 square =value**2
 squares.append(square)
print(squares)

"""matches=[]
for car in range(1,5):
 matches.append(car**)
print(matches)"""
numbers = []
for count in range(0,20):
    number=count+1
    numbers.append(number)
    #numbers.append(count+1)
    #print(numbers)

squares = [value**2 for value in range(1, 11)]
print(squares)
numbers=[count+1 for count in range(1, 10)]
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(numbers[7])