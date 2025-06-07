def process(numbers):
    numbers.sort()
    return " ".join(map(str, numbers))


input_numbers = list(map(int, input().split()))
print(process(input_numbers))
