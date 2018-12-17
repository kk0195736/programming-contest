def judge_empty(int_array):
    for i in int_array:
        if i != 0:
            return False
    return True

S = [1 for i in range(10)]

print(judge_empty(S))