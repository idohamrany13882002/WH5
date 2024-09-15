# START
x: float = float(input('enter height: '))
while not 0.4 <= x <= 2.5:
    print('wrong input!')
    x: float = float(input('enter height: '))
# END

# START
a: int = int(input('enter a number: '))
b: int = int(input('enter a number: '))
if b > a:
    for x in range(b, a - 1, -1):
        print(x, end=' ')
    print()
else:
    for x in range(b, a + 1, 1):
        print(x, end=' ')
    print()
# END

# START
counter: int = 1
pi: float = float(input('how much is pi? '))
while pi!=3.14 and counter<3:
    counter += 1
    print ('try again!')
    pi: float = float(input('how much is pi? '))
if counter<=3 and pi==3.14:
    print("you're correct")
else:
    print ('pi is 3.14')
# END

#START
while True:
    num1: int = int(input('enter a number: '))
    num2: int = int(input('enter a number: '))
    num3: int = int(input('enter a number: '))
    avg = (num1 + num2 + num3) / 3
    if 0 <= num1 <= 10 and 10 <= num2 <= 60 and 60 <= num3 <= 100 and avg == num2:
        break
# END

# START
beer: int = 1
age: int = int(input('enter age: '))
while beer<=10::
    if age >= 18
        beer +=1
        print('have a beer')
    age: int = int(input('enter age: '))
# END
