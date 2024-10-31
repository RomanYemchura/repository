def find(number):
    previous = number[0]
    for current in number[1:]:
        if current > previous  :
            print(True)
        else :
            print(False)
            return current
        previous = current
    return None



print(find([1, 2, 3, 4, 3, 7, 8]))



