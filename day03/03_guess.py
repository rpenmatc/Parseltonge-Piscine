import random
array = ["Apple", "array", "birth", "Plane", "bread", "catch"]
word = random.choice(array)
count = 9
print("Guess the five letter word with ten tries")
print("I will give you a hint: it starts with a", word.upper()[0])
print("Guess:")
guess = input()
while word != guess and count >= 1:
    if len(guess) == 0:
        print("You wasted a guess =P")
    elif len(guess) != 5:
        print("0:1:2:3:4 that's how we count to five")
    elif guess.upper()[0] != word.upper()[0]:
        print("abcdefghijklmnopqrstuvwqyz is the alphabet")
    print(f"You have only {count} tries left")
    count -= 1
    print("Guess:")
    guess = input()
if guess == word:
    print("Good Job! You are one with the Source")
else:
    print("You ran out of guesses")
