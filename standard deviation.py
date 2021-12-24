import math
data = [60,61,65,63,98,99,90,95,91,96]
# finding mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total+=int(x)
    mean = total/n
    return mean
squared_list = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squared_list.append(a)
# getting sum
sum = 0
for i in squared_list:
    sum = sum+i
# dividing the sum by total values
result = sum/(len(data)-1)
# gettng the deviation by taking the square root of the result
std_deviation = math.sqrt(result)
print(std_deviation)
