def euclidean_algorithm(first,second):
    if (second ==0):
        return first
    else:
        return euclidean_algorithm(second,first % second)

print euclidean_algorithm(1071,462)
