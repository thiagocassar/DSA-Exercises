for i in range(1,20):
    j = 2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            j += 1
        else:
            j += 1
    
    if counter == 0:
        print(str(i) + " é um número primo \n")
        counter = 0
    else:
        counter = 0

# Racional do Código


for i in range(1,20):
    j = 2
    counter = 0
    while j < i:
        #Condição If Inicial
        if i % j == 0:
            print('No Loop ' + str(i) + ', temos:')
            print('i = ' + str(i))
            print('j = ' + str(j))
            print('counter = ' + str(int(counter)))
            counter = 1
            j += 1
            print('O número '+ str(i) + ' acionou a condição "if" INICIAL')
            print('E j FICA IGUAL A ' + str(j) + ' E counter FICA IGUAL A ' + str(int(counter)) + ', levando para a próxima condição do Loop ' + str(i))

        #Condição Else Inicial
        else:
            print('No Loop ' + str(i) + ', temos:')
            print('i = ' + str(i))
            print('j = ' + str(j))
            print('counter = ' + str(int(counter)))
            j += 1
            print('O número '+ str(i) + ' acionou a condição "else" INICIAL')
            print('E j FICA IGUAL A ' + str(j) + ' E counter FICA IGUAL A ' + str(int(counter)) + ', levando para a próxima condição do Loop ' + str(i))

    if counter == 0:
        print('No Loop ' + str(i) + ', temos:')
        print('i = ' + str(i))
        print('j = ' + str(j))
        print('counter = ' + str(int(counter)))
        print('O número '+ str(i) + " É UM NÚMERO PRIMO")
        print('E COMO j = i ---> j VOLTA A SER IGUAL A ' + str(2))
        counter = 0
        print('E counter FICA IGUAL A ' + str(int(counter)) + ', seguindo para o Loop ' + str(i + 1))
        
    #Condição Else Final
    else:
        print('No Loop ' + str(i) + ', temos:')
        print('i = ' + str(i))
        print('j = ' + str(j))
        print('counter = ' + str(int(counter)))
        counter = 0
        print('O número '+ str(i) + ' acionou a condição "else" FINAL')
        print('E COMO j = i ---> j VOLTA A SER IGUAL A ' + str(2) + ' E counter FICA IGUAL A ' + str(int(counter)) + ', seguindo para o Loop ' + str(i + 1))
