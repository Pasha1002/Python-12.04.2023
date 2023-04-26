try:

    numbers = [1, 2, 3, 4, 5]
    def average(numbers):
        if len(numbers) == 0:
            return 0  
        return sum(numbers) / len(numbers)
    print(average(numbers))
    
except Exception as e:
    print(e)
