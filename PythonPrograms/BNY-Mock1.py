import sys
from io import StringIO

def normalize_number(number):
    # Mapping from letters to digits
    mapping = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9'
    }
    
    # Remove hyphens and map letters to digits
    normalized = []
    for char in number:
        if char in mapping:
            normalized.append(mapping[char])
        elif char.isdigit():
            normalized.append(char)
    
    # Return the normalized number in standard format
    return ''.join(normalized[:3]) + '-' + ''.join(normalized[3:])

def main():
    input_data = """12
4873279
ITS-EASY
888-4567
3-10-10-10
888-GLOP
TUT-GLOP
967-11-11
310-GINO
F101010
888-1200
-4-8-7-3-2-7-9-
487-3279"""
    
    # Redirecting input
    sys.stdin = StringIO(input_data)
    
    data = sys.stdin.read().strip().split('\n')
    
    num_count = int(data[0])
    number_counts = {}
    
    # Process each number
    for i in range(1, num_count + 1):
        original_number = data[i]
        normalized_number = normalize_number(original_number)
        
        if normalized_number in number_counts:
            number_counts[normalized_number] += 1
        else:
            number_counts[normalized_number] = 1
    
    # Collect and sort the duplicates
    duplicates = [(num, count) for num, count in number_counts.items() if count > 1]
    duplicates.sort()
    
    if duplicates:
        for num, count in duplicates:
            print(f"{num} {count}")
    else:
        print("No duplicates.")

if __name__ == "__main__":
    main()
