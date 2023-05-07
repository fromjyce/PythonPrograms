num_dictionaries = int(input("How many dictionaries do you want to create? "))
main_dict = {}
for i in range(num_dictionaries):
    dict_name = input(f"What do you want to name dictionary {i+1}? ")
    sub_dict = {}
    while True:
        key = input(f"Enter a key for {dict_name} (or 'done' to stop adding): ")
        if key == 'done':
            break
        value = input(f"Enter a value for {key}: ")
        sub_dict[key] = value
    main_dict[dict_name] = sub_dict
print("Main dictionary:", main_dict)
