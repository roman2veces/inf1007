

def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)

    # if index != 0:
    #     return index - 1 + fibonacci(index - 1)
    # else:
    #     return index


# print(fibonacci(5))


def get_fibonacci_sequence(length, seq=[0, 1]):
    # sequence = []
    # for index in range(length):
    #     if index >= 2:
    #         sequence.append(
    #             (lambda element: (element - 1) + (element - 2))(index))
    #         print((lambda element: (element - 1) + (element - 2))(index))
    #         # sequence.append(fibonacci(index))
    #         # print(fibonacci(index))
    #     else:
    #         sequence.append(seq[index])
    #         print(seq[index])

    # return [(lambda element: (element - 1) + (element - 2))(index) if index > 2 else seq[index] for index in range(length-1)]

    return get_fibonacci_sequence(0).extend([get_fibonacci_sequence(index) if index >= 2 else seq[index] for index in range(length)])


print(get_fibonacci_sequence(6))


# data = {
#     "foo": 42.6942,
#     "bar": 42.9000,
#     "qux": 69.4269,
#     "yeet": 420.1337
# }


# def get_sorted_dict_by_decimals(dict_arg):
#     return {key: value for key, value in sorted(dict_arg.items(), key=lambda element: element[1] - int(element[1]))}


# print(get_sorted_dict_by_decimals(data))
