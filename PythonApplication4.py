#猜数游戏2.1
print('you only have three chances.')
import random
n =random.randint(1,10)
guess_count = 1
guess = int(input('enter an interger number.'))
while guess_count < 3 :
    print('you have tried;',guess_count)
    if guess > n:
        print('it is high,please input a lower number')
        guess=int(input())
    elif guess < n:
        print('it is low,please input a higher number')
        guess=int(input())
    else:
        print('you are right!')
        break
    guess_count=guess_count+1
else:
    print('Sorry,game over.')
print('The right num is:',n)




