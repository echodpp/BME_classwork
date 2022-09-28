# example of exception
# def div_example():
#     for x in [3, 5, 7, 0, 9]:
#         try:
#             y = 1 / x
#         except ZeroDivisionError:
#             print("div by 0, skipping this iteration")
#             continue
#         print("Inverse of {} is {}".format(x, y))


def add_two_numbers(a, b):
    if type(a) is not int or type(b) is not int:
        raise TypeError("a and b must be integers")
    if a < 0 or b < 0:
        raise ValueError("a and b must be positive")
    return a + b


def main():
    add_two_numbers(1, -2)


if __name__ == "__main__":
    main()
