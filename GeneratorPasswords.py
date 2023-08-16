from string import printable
from random import choice
all_characters=list(printable)[:-6]
status = False
while status == False:
    size = int(input("какой длины вы хотите пароль?ㅤ"))
    if 21>= size >=3:
        status = True
    else:
        print("выброна неправильная длинна пароля")
run = False
while run == False:
    password = ''.join([choice(all_characters) for current in range(size)])
    print(password)
    answer = input("нравится вам пароль?ㅤ")
    if answer == "да":
        run = True
    elif answer == "нет":
        print("хорошо побробуй ещё раз")
    else:
        print("не корректный символ программа закрывается")
        break