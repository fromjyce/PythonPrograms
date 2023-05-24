def calc_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def display_sleeping_pattern(seconds, temperature):
    time_formatted = calc_time(seconds)
    temperature_fahrenheit = convert_to_fahrenheit(temperature)

    print("Sleeping pattern information:")
    print(f"Time: {time_formatted}")
    print(f"Temperature: {temperature_fahrenheit}°F")

    if seconds >= 3 * 3600:
        print("The baby is in deep sleep.")
    elif seconds < 2 * 3600:
        print("The baby is cranky.")


# Example usage
hours = 4
sleeping_seconds = hours * 3600  # 4 hours in seconds
temperature_celsius = 25

display_sleeping_pattern(sleeping_seconds, temperature_celsius)
