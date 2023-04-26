

try:



    n = int(input("Enter a number: "))
    def fib(n):   
        if n in (1, 2):
            return 1
        
        return fib(n-1) + fib(n-2)
    print(fib(n))
       

except Exception as e:
    print(e)

