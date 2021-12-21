import random
a = 0
dl = 10
hp = 100
r = 20
wes = 30
while r <= 100 or (hp or wes or dl > 0): 
    print('День')
    print('Что будете делать? 1 - копать нору, 2 - поесть травки, 3 - пойти подраться, 4 - просто спать')
    a = input()
    if a == '1':
        print('Как вы собираетесь копать нору? 1 - Интенсивно, 2 - Лениво ')
        a = input()
        if a == '1':
            dl = dl + 5
            print(" Длина стала: ", dl)
            hp = hp - 30
            print(" Здоровье стало: ", hp)
        else:
            dl = dl + 2
            print(" Длина стала: ", dl)
            hp = hp - 10
            print(" Здоровье стало: ", hp)
    elif a == '2':
        print('Какую травку вы будете кушать? 1 - Жухлую, 2 - Зеленую')
        b = input()
        if b == '1':
            hp = hp + 10
            print(" Здоровье стало: ", hp)
            wes = wes + 15
            print(" Вес стал: ", wes)
        elif b == '2' and r < 30:
            hp = hp - 30
            print("Здоровье стало: ", hp)
        else:
            hp = hp + 30
        print("Здоровье стало: ", hp)
        wes = wes + 30
        print(" Вес стал: ", wes)
    elif a == '3':
        print('С каким существом будешь драться? 1 - слабый, 2 - средний, 3 - сильный')   
        c = input()

        def slabiy_boss():
            global hp, r
            wes_bossa = 30
            s = random.randint(0, 60)
            if s > 30:
                hp = hp - 5
                print('Здоровье стало:', hp)
                print('Уважения стало:', r)
                print('Победил босс')
            else:
                hp = hp - 5
                r = r + 5
                print('Здоровье стало:', hp)
                print('Уважения стало:', r)
                print('Победил кролик')


        def sredniy_boss():
             global hp, r
             wes_bossa = 50
             s = random.randint(0, 80)
             if s > 40:
                hp = hp - 20
                print('Здоровье стало:', hp)
                print('Уважения стало:', r)
                print('Победил босс')
             else:
                hp = hp - 20
                r = r + 20
                print('Здоровье стало:', hp)
                print('Уважения стало:', r)
                print('Победил кролик')

        def strong_boss():
             global hp, r
             wes_bossa = 70
             s = random.randint(0, 100)
             if s > 50:
                hp = hp - 40
                print('Здоровье стало:', hp)
                print('Уважения стало:', r)
                print('Победил босс')
             else:
                hp = hp - 40
                r = r + 40
                print('Здоровье стало:', hp)
                print('Уважения стало:', r)
                print('Победил кролик')

        if c == '1':
            slabiy_boss()
        elif c == '2':
            sredniy_boss()
        elif c == '3':
            strong_boss()
    else:
        print('Вы проспали весь день')
        hp = hp + 20
        print(" Здоровье стало: ", hp)
        wes = wes - 5
        print(" Вес стал: ", wes)
        dl = dl - 2
        print("Длина норы стала: ", dl)
        r = r - 2
        print(" Уважение стало: ", r)

