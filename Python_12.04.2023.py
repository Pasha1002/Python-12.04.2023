
try:

    a = input('Enter name: ')
    b = int(input('Enter age: '))
    a1 = input('Enter name: ')
    b1 = int(input('Enter age: '))
    a2 = input('Enter name: ')
    b2 = int(input('Enter age: '))
    list = [(a,b),(a1,b1),(a2,b2)]
    def sort_age(list):
        list.sort(key=lambda x: x[1])
        return(list)
    print(sort_age(list))


except Exception as e:
    print(e)

