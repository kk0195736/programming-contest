import math

bets = int(input())

payout = 1.90


def new_bets(bets):
    return bets + math.ceil(bets / (payout - 1))


a = new_bets(bets)
b = new_bets(new_bets(bets))
c = new_bets(new_bets(new_bets(bets)))
d = new_bets(new_bets(new_bets(new_bets(bets))))
e = new_bets(new_bets(new_bets(new_bets(new_bets(bets)))))
f = new_bets(new_bets(new_bets(new_bets(new_bets(new_bets(bets))))))

print(a)
print(b, a+b)
print(c, a+b+c)
print(d, a+b+c+d)
print(e, a+b+c+d+e)
print(f, a+b+c+d+e+f)

