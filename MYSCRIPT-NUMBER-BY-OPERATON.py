print('Welcome To Quiz Competation')
name = input("What is your name? \n")
print("All The Best ! ", name)
option1=('1.Addition')
option2=('2.Subraction')
option3=('3.Multiplication')
option4=('4.Division')
print(option1)
print(option2)
print(option3)
print(option4)
print('No Should Equal To 625  With Any Mathamathics Operation')
print('Please  Also Try Another Operation')
print('Enter First Number = ')
a = input()
aa = int(a)
print('Enter Second Number = ')
b = input()
bb = int(b)

cc = input('Enter Option = ')

if cc == '1':
    print(aa+bb==625)
    print(cc)
elif (cc == '2'):
    print(aa-bb==625)
elif (cc == '3'):
    print(aa * bb==625)
elif (cc == '4'):
    print(aa / bb==625)
