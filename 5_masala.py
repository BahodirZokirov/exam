from time import perf_counter


def timer(func):
    def inner1(*args, **kwargs):
        start = perf_counter()

        abc = func(*args, **kwargs)

        end = perf_counter()
        print("Average time : ", end - start)
        return abc

    return inner1

@timer
def egizak_tub_son(numer):
    result = []
    lt = []
    amount = 0
    for i in range (1, numer):
        k = 0
        for j in range(1, i + 1):
            if i % j == 0:
                k += 1
        if k == 2:
            # amount += 1
            lt.append (j)
    for m in range (len (lt) - 1):
        if lt[m + 1] - lt[m] == 2:
            result.append (f"{lt[m]} : {lt[m + 1]}")
    return result



print (egizak_tub_son(50))



# egizak_tub_sonn uchun 4.9203999878955074e-05 ishladi