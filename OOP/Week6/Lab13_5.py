def add_fractions(tuple1, tuple2):
    denominator = tuple1[1] * tuple2[1]
    numerator = (denominator / tuple1[1]) * tuple1[0] + (denominator / tuple2[1]) * tuple2[0]

    return (numerator, denominator)


def multiply_fractions(tuple1, tuple2):
    denominator = tuple1[1] * tuple2[1]
    numerator = tuple1[0] * tuple2[0]

    return (numerator, denominator)


print(add_fractions((2, 3), (3, 4)))
print(multiply_fractions((2, 3), (3, 4)))
