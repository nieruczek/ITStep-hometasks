def generate(max):
    number = 2
    divider = 2

    while number <= max:
        if number == divider:
            yield number
            divider = 2
            number += 1
        if number % divider != 0:
            divider += 1
            if number == divider:
                yield number
                divider = 2
                number += 1
        else:
            divider = 2
            number += 1

gen = generate(25)
for i in range (1, 9):
    i = print(next(gen))