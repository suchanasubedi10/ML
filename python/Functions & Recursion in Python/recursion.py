def show(n):
    if(n == 0):#base case which decides when the recursion should stop
        return
    print(n)
    show(n-1)

show(7)