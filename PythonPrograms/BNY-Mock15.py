import math

def will_erode(x, y):
    while True:
        radius_squared = (100 * year) / math.pi2
        if x**2 + y**2 <= radius_squared:
            return year
        year += 1

def main():
    data = input().strip().split("\n")
    
    N = int(data[0])
    results = []
    
    for i in range(1, N + 1):
        x, y = map(float, data[i].split())
        year = will_erode(x, y)
        results.append(f"Property {i}: This property will begin eroding in year {year}.")
    
    # Print all results
    for result in results:
        print(result)
    print("END OF OUTPUT.")

main()
