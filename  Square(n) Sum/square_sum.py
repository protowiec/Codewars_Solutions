def square_sum(numbers):
    num = []
    for i in numbers:
        i = pow(i, 2)
        num.append(i)
    return sum(num)


"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

"""