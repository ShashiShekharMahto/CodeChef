t = int(input())
for i in range(t):
    N = int(input())
    P = list(map(int, input().split(" ")))
    P.sort(reverse = True) #sorting the price in descending order
    sum = 0
    for i in range(N):
        if(P[i]-i<0): #if price of the car falls below zero then remaining car price will be zero
            break
        else:
            sum = sum +P[i]-i
            sum = sum % 1000000007
    print(sum)
