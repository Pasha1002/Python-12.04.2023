
try:


    import string
    def capitalize_words(string):
        return string.title()
    string = input('Enter a string of words: ')
    print (capitalize_words(string))

except Exception as e:
    print(e)

