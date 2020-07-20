numBottles = 15
numExchange = 4

res = numBottles

while numBottles >= numExchange:
    remain = numBottles%numExchange
    numBottles //= numExchange
    res += numBottles
    numBottles += remain

print(res)