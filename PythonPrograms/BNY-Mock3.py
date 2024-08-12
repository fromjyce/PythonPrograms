def atm_withdrawal(max_notes, amount, notes_100, notes_200, notes_500, notes_1000):
    # Initialize the result
    result = {
        100: 0,
        200: 0,
        500: 0,
        1000: 0
    }
    
    total_notes_used = 0

    # Check if the amount is valid
    if amount % 100 != 0:
        return 0

    # Process each denomination starting from the smallest
    for denom, available_notes in [(100, notes_100), (200, notes_200), (500, notes_500), (1000, notes_1000)]:
        if amount == 0:
            break
        # Determine the maximum number of notes of this denomination we can use
        num_notes = min(amount // denom, available_notes)
        print(num_notes)
        # Calculate the potential total notes if we use these notes
        potential_total_notes = total_notes_used + num_notes
        print(potential_total_notes, total_notes_used, num_notes)
        if potential_total_notes > max_notes:
            num_notes = max_notes - total_notes_used
            print(num_notes, total_notes_used)
        result[denom] = num_notes
        print(result)
        total_notes_used += num_notes
        print(total_notes_used, num_notes)
        # Reduce the amount
        amount -= num_notes * denom
        print(amount, num_notes, denom)
    
    # Check if we have successfully withdrawn the required amount
    if amount == 0 and total_notes_used <= max_notes:
        return total_notes_used
    else:
        return 0

# Input Reading
N = int(input().strip())
amount = int(input().strip())
notes_100 = int(input().strip())
notes_200 = int(input().strip())
notes_500 = int(input().strip())
notes_1000 = int(input().strip())

# Calculate the result
result = atm_withdrawal(N, amount, notes_100, notes_200, notes_500, notes_1000)
print(result)
