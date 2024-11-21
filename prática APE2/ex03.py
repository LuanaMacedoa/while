while True:
    x = int(input('Digite o valor de X: '))
    y = int(input('Digite o valor de Y: '))
    if x == 0 or y == 0:
        break
    if x > 0 and y > 0:
        print('primeiro')
    elif y < 0 and x > 0:
        print('quarto')
    elif x < 0 and y < 0:
        print('terceiro')
    else:
        print('segundo')