def fib(n):
    if n == 0: #to start fibonacci seraries value must be >= 1
        print('Enter postive integer')
    elif n ==1:
        print(0)
    else:
        li = [0, 1]
        for i in range(2, n): # start the loop from second index as 'li' is assigned for 0th and 1st index
            li.append(li[-1] + li[-2])
            i += 1
        print(*li)  # '*' is used to print elements from list in single line with spaces

n = int(input('Enter the number for which you want to generate fibonacci series\n'))
fib(n)
