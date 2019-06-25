def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def lcm(a, b):
	return a * b // gcd (a, b)

A, B, C, D= list(map(int, input().split()))

cd = lcm(C,D)

print(B - A + 1 - (B // C - (A-1) // C) -(B // D - (A-1) // D) + (B // cd - (A-1) // cd))