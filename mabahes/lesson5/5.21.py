def display_number_pyramid():
    size = 5

    for i in range(size):
        for j in range(size - i - 1):
            print(' ', end=' ')

        for j in range(i + 1):
            print(j + 1, end=' ')

        for j in range(i, 0, -1):
            print(j, end=' ')

        print()

display_number_pyramid()
