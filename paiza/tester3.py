def A_function(number):
    return number + 1

def B_function(number):
    return number * 2

N = [1, 2, 3, 4]

for i in N:
    print(B_function(A_function(i)))