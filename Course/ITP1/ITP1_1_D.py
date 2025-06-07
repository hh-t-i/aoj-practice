def format_seconds_to_hms(seconds):
    if not isinstance(seconds, int) or seconds < 0:
        raise ValueError("引数は0以上の整数である必要がある")
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    return f"{hours}:{minutes}:{remaining_seconds}"

input_num = int(input())
print(format_seconds_to_hms(input_num))
