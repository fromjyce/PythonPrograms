speed = int(input("Enter the vehicle's speed: "))  # Assuming the speed is obtained from user input

speed_limit = 70
demerit_points = 0

if speed < speed_limit:
    print("Maintain the same speed")
else:
    demerit_points = (speed - speed_limit) // 5

    if demerit_points > 0:
        print("Demerit points:", demerit_points)

    if demerit_points > 12:
        print("Your license is suspended")
