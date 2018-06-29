abc = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
x = input("What is your string ")
x = x.lower()
num =0
num1 = 0
answer = ""
while num < len(x):
    letter = x[num]
    num = num + 1
    if letter in abc:
        num1 = num1 + 1
        if num1 %2 ==0:
            even = True
        else:
            even = False
        if even:
            letter = letter.upper()
    answer = answer + letter
print(answer)
num = 0
num1 = 0
answer = ""
A = "A"
E = "E"
I = "I"
O = "O"
U = "U"
while num < len(x):
    letter = x[num]
    num = num + 1
    if letter in abc:
        num1 = num1  + 1
        if num1 %2 == 0:
            even = True
        else:
            even = False
        if even:
            letter = letter.upper()
            if letter == A:
                letter == "*"
            if letter == E:
                letter = "*"
            if letter == I:
                letter = "*"
            if letter == O:
                letter = "*"
            if letter == U:
                letter = "*"
        answer = answer + letter
print(answer)
num2 = 0
num3 = 0
while num3 < len(answer):
    letter = answer[num3]
    if "(" == x[num3]:
        num2 = num2 + 1
    if ")" == x[num3]:
        num2 = num2 - 1
    num3 = num3 + 1
if num2 == 0:
    print("Balanced? True")
else:
    print("Balanced? False")
