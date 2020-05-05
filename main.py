# deviation

from statistics import mean
import math
n = int(input("Enter total elements in array (5 to 100)"))
arr = list(map(int, input("Enter elements in array (0 to 100000)").split()))

xi = []
for num in arr:
    xi.append((num-mean(arr))**2)
print(round(math.sqrt(sum(xi)/n), 1))
