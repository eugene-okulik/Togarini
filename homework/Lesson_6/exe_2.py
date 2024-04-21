for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print('FuzzBuzz')
    elif numbers % 3 == 0:
        print('fuzz')
    elif numbers % 5 == 0:
        print('buzz')
    else:
        print(numbers)
