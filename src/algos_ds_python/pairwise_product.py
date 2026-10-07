from functools import reduce


def compute_max_values(max_vals: tuple[int, int], number: int) -> tuple[int, int]:
    current_max, current_second_max = max_vals
    if number < current_second_max:
        return max_vals
    elif number < current_max:
        return current_max, number
    else:
        return number, current_max


def max_pair_product(numbers: list[int]) -> int:
    max_val, second_max_val = reduce(compute_max_values, numbers, (-1, -1))
    return max_val * second_max_val


def naive_max_pair_product(numbers: list[int]) -> int:
    return max(
        [
            x * y
            for idx2, y in enumerate(numbers)
            for idx1, x in enumerate(numbers)
            if idx2 < idx1
        ]
    )


if __name__ == "__main__":
    _ = input()
    numbers = list(map(int, input().split()))
    print(max_pair_product(numbers))
