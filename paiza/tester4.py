counter = 0

def A_function(int_array):
    counter += 1
    for i in int_array:
        yield i + 1


def B_function(number):
    counter += 1
    return number *2

N = [1, 2, 3, 4]

print(counter)
for i in A_function(N):
    print(counter)
    print("結果:{}".format(B_function(i)))
    print(counter)