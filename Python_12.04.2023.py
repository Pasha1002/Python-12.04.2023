
try:

    import random
    list=[random.randint(0,10) for i in range(5)]
    list2=[random.randint(0,10 ) for i in range(5)]
    print(list,list2)

    def scalar(list,list2):
        scalar = sum([list[i]*list2[i] for i in range(len(list))])
        return(scalar)
    print(scalar(list,list2))

except Exception as e:
    print(e)

