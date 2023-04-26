
try:

    import random
    list = [random.randint(0,10) for i in range(20)]
    print(list)
    def the_number_that_occurs_most_often(list):
        counts = {}
        for num in list:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        return max(counts, key=lambda x: (counts[x], -x))
    print(the_number_that_occurs_most_often(list))

except Exception as e:
    print(e)
