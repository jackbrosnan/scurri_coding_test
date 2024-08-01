def ThreeFive():
    num_array = []
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            num_array.append('ThreeFive')
        elif num % 3 == 0:
            num_array.append('Three')
        elif num % 5 == 0:
            num_array.append('Five')
        else:
            num_array.append(num)

    return num_array
