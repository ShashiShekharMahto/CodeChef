# cook your dish here
t = int(input())
for i in range(t):
    nmxy = list(map(int, input().split(" ")))
    n = nmxy[0]
    m = nmxy[1]
    x = nmxy[2]
    y = nmxy[3]
    if(n == 1 and m == 1):
        print(x)
    elif((n*m) %2 == 0):
        if(2*x <= y):
            print(n * m *x)
        elif(2*x > y):
            print(((n * m)//2)*y)
    else:
        if(2*x <= y):
            print((((n * m)//2)*2*x) + x)
        elif(2*x > y):
            a = x if x<y else y
            print((((n * m)//2)*y) + a)
