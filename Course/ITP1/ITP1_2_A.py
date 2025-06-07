def compare_numbers(a, b):
    if a < b:
        return "a < b"
    elif a > b:
        return "a > b"
    elif a == b:
        return "a == b"

input_num_a, input_num_b = map(int, input().split())
print(compare_numbers(input_num_a, input_num_b))
