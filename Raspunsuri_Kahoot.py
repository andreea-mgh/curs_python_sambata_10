def afiseaza_raspuns(nr):
    if nr == 1:
        if 3%6 == 3:
            print('yes')
        else:
            print("no")



    elif nr == 2:
        print(4 * '0' + 7 * '1')



    elif nr == 3:
        a = 33 // 6
        b = 21 % 8

        if a == b:
            print("acelasi rezultat :)")
        else:
            print("alt rezultat :(")
    


    elif nr == 4:
        for i in range(5):
            print(i)



    elif nr == 5:
        list = ['biscuiti', 'chipsuri', 'gogosi', 'covrigi']
        print('Mananc '+list[2])



    elif nr == 6:
        def calculeaza_ceva(a, b=2, c=3):
            print(a + b - c)

        calculeaza_ceva(4, 6)



    else:
        print("ups, am gresit numarul")



afiseaza_raspuns(6)