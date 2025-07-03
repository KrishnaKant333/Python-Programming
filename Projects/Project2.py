from random import randint
n = randint(1, 100)
a = 0
guesses = 1
while(a!=n):
	a = int(input("Guess a number from 1 to 100 : "))
	if a > n:
		print("Lower number please.")
		guesses += 1
	elif a < n:
		print("Higher number please.")
		guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempt(s).")
