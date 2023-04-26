
try:

    string = (input("Введіть рядок: "))
    def output_first_and_last_three_chars(string):
        if len(string) < 6:
            return "Недостатньо символів"
        else:
            return string[:3] + string[-3:]
    print(output_first_and_last_three_chars(string))
    
except Exception as e:
    print(e)
