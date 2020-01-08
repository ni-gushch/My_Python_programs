from functools import reduce

print(
    reduce(
        lambda x, y: x or y, list(
            map(lambda x: int(input()) == 0, range(int(input())))
            )
        )
    )
