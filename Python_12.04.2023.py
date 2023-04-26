
try: 


    def count_vowels_consonants(string):
        
        vowels = "aeiouAEIOU"
        num_vowels = 0
        num_consonants = 0
        
        for char in string:
            if char in vowels:
                num_vowels += 1
            elif char.isalpha():
                num_consonants += 1
            
        print("Number of vowels:", num_vowels)
        print("Number of consonants:", num_consonants)
    count_vowels_consonants('Hello World')   
        



except Exception as e:
    print(e)

try: 

    vowel= 0
    consonant_l = 0
    vse_gls = "aeiouAEIOU"
    poem = input('Enter string: ')
    for i in poem:
        if i.isalpha() :
            if i.isalpha() :
                if i in vse_gls:
                    vowel += 1
                else:
                    consonant_l += 1
                break
        elif i.isalpha() == False:
            if i.isdigit():
                print('ONLY DIGIT IN THE STRING' )
                break
        else:
            print('errorrrr')
      
    print('num of vowel:', vowel)
    print('num of consonant:', consonant_l)

except Exception as e:
    print(e)