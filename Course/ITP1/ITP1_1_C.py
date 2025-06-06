def calc_rectangle_area(length, width):
    return length * width

def calc_rectangle_perimeter(length, width):
    return 2 * (length + width)

input_str = input()
length_str, width_str = input_str.split()
length = int(length_str)
width = int(width_str)

area = calc_rectangle_area(length, width)
perimeter = calc_rectangle_perimeter(length, width)
print(area, perimeter)