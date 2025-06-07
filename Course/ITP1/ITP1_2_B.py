def check_ascending_order(a, b, c):
    if a < b and b < c:
        return "Yes"
    else:
        return "No"
    
input_numbers = tuple(map(int, input().split()))
print(check_ascending_order(*input_numbers))
