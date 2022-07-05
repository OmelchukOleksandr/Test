try:
    print('=================================================')
    player_1 = input('Гравець 1, введіть своє ім*я: ')
    player_2 = input('Гравець 2, введіть своє ім*я: ')
    matches = int(input('Введіть загальну кількість сірників: '))
    print('=================================================')
    print('Гра починається!')
    while matches > 0:
        print(player_1, 'Ваш хід.')
        a = int(input())
        while a < 1 or a > 3:
            print('Ви можете взяти лише від одного до трьох сірників')
            print(player_1, 'Ваш хід.')
            a = int(input())
        while matches < a:
            print('Ви не можете взяти більше сірників ніж є. Сірників лишилось:', matches)
            print(player_1, 'Ваш хід.')
            a = int(input())
        matches -= a
        print('Сірників лишилось:', matches)
        if matches == 0:
            print(player_1, 'програв')
        else:   
            print('=================================================')
            print(player_2, 'Ваш хід.')
            a = int(input())
            while a < 1 or a > 3:
                print('Ви можете взяти лише від одного до трьох сірників')
                print(player_2, 'Ваш хід.')
                a = int(input())
            while matches < a:
                print('Ви не можете взяти більше сірників ніж є. Сірників лишилось:', matches)
                print(player_2, 'Ваш хід.')
                a = int(input())
            matches -= a
            print('Сірників лишилось:', matches)
            print('=================================================')
            if matches == 0:
               print(player_2, 'програв')
except ValueError:
    print('Помилка! В рядку де очікувався числовий тип даних будо введено інший тип даних.')
except:
    print ('Невідома помилка.')
