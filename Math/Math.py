from random import*

print('Valige raskusaste')
print('Tase 1=>"1" Tase 2=>"2" Tase 1 extra=>"3" Tase 3=>"4" ')
while True:
    tase=int(input(' '))
    if tase==1:
        j=0
        for i in range(1,11):
            arv_1=randint(-10,10)
            arv_2=randint(-10,10)
            i=(f'Mis on {arv_1}+{arv_2}?')
            vastus=arv_1+arv_2
            print(i)
            user_vastus=int(input('vastus=>'))
            if vastus==user_vastus: 
                j+=10
                print('Õige')
            else:
                print('Vale')
        if j<=60:
            print(f'Te saate {j}% Hinne on 2')
        elif j>=61 and j<75:
            print(f'Te saate {j}% Hinne on 3')
        elif j>=75 and j<=90:
            print(f'Te saate {j}% Hinne on 4')
        else:
            print(f'Te saate {j}% Hinne on 5')
    elif tase==2:
        j=0
        for i in range(1,11):
            arv_1=randint(-10,10)
            arv_2=randint(-10,10)
            i=(f'Mis on {arv_1}*{arv_2}?')
            vastus=arv_1*arv_2
            print(i)
            user_vastus=int(input('vastus=>'))
            if vastus==user_vastus: 
                j+=10
                print('Õige')
            else:
                print('Vale')
        if j<=60:
            print(f'Te saate {j}% Hinne on 2')
        elif j>=61 and j<75:
            print(f'Te saate {j}% Hinne on 3')
        elif j>=75 and j<=90:
            print(f'Te saate {j}% Hinne on 4')
        else:
            print(f'Te saate {j}% Hinne on 5')
    elif tase==3:
        j=0
        for i in range(1,11):
            arv_1=randint(-100,100)
            arv_2=randint(-100,100)
            i=(f'Mis on {arv_1}+{arv_2}?')
            vastus=arv_1+arv_2
            print(i)
            user_vastus=int(input('vastus=>'))
            if vastus==user_vastus:
                j+=10   
                print('Õige')
            else:
                print('Vale')
        if j<=60:
            print(f'Te saate {j}% Hinne on 2')
        elif j>=61 and j<75:
            print(f'Te saate {j}% Hinne on 3')
        elif j>=75 and j<=90:
            print(f'Te saate {j}% Hinne on 4')
        else:
            print(f'Te saate {j}% Hinne on 5')
    elif tase==4:
        j=0
        for i in range(1,11):
            arv_1=randint(1,10)
            arv_2=randint(1,3)
            i=(f'Mis on {arv_1}**{arv_2}?')
            vastus=arv_1**arv_2
            print(i)
            user_vastus=int(input('vastus=>'))
            if vastus==user_vastus:
                j+=10
                print('Õige')
            else:
                print('Vale')
        if j<=60:
            print(f'Te saate {j}% Hinne on 2')
        elif j>=61 and j<75:
            print(f'Te saate {j}% Hinne on 3')
        elif j>=75 and j<=90:
            print(f'Te saate {j}% Hinne on 4')
        else:
            print(f'Te saate {j}% Hinne on 5')
    if tase>0 and tase<5: break
    print('Te saate valida ainult 1,2,3 või 4')