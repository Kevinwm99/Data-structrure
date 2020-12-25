from collections import deque
def fibo(n):
    if n <= 0:
        return ("incorect inputs")
    if n == 1: 
        return 1
    q = deque()
    q.appendleft(0)
    q.appendleft(1)
    for i in range(2,n):
        q.appendleft(q.popleft()+q[0])
        q.pop()
    return q.popleft

print(fibo(9))