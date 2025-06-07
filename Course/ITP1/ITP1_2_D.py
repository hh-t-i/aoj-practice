def process(W, H, x, y, r):
    if (0 <= x - r and
        0 <= y - r and
        W >= x + r and
        H >= y + r):
        return "Yes"
    else:
        return "No"


input_numbers = tuple(map(int, input().split()))
print(process(*input_numbers))
