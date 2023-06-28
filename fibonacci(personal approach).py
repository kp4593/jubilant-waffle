m = int(input("Enter the number of terms"))

lst=[0,1]

def fib(m):
    if m==1:
        return 0
    elif m==2:
        return 0,1
    else:
        for i in range(m+1):
            if i==0 or i==1:
                continue
            else:
                nth = lst[i-2] + lst[i-1]
                lst.append(nth)
        return lst


print(fib(m))