def sum(*numbers):
    sm=0
    for element in numbers:
        sm = sm+element
    print(sm)
    return sm
sum(12,12,13,14,15)