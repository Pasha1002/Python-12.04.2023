

try:

    n = int(input('Enter number: '))
    def delitel(n):
        for i in range(1,int(n/2)+1):
            if n%i == 0:
                yield i
    print('Divisors of a number',list(delitel(n)))

except Exception as e:
    print(e)

