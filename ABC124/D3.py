N, K = list(map(int, input().split()))

S = input()

zero_flag = False
zero_counter = 0
sum_counter =

for i in S:
    if i == '0' and zero_flag == False:
        zero_flag = True
        zero_counter += 1
    if i == '1' and zero_flag == True:
        zero_flag = False
    