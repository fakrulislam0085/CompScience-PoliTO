def flood_map(heights, water_level):
    """
    Creates a flood map based on terrain heights and the current water level.
    Returns a 2D list of the same size with '*' for flooded and ' ' for dry areas.
    """
    n = len(heights)  # assuming square matrix
    flood = []

    for row in range(n):
        flood_row = []
        for col in range(n):
            if heights[row][col] <= water_level:
                flood_row.append('*')  # flooded
            else:
                flood_row.append(' ')  # dry land
        flood.append(flood_row)
    
    return flood


def print_flood_map(flood):
    """
    Nicely prints the flood map row by row.
    """
    for row in flood:
        print(''.join(row))  # Join the row into a single string and print


def main():
    """
    Main program that:
    1. Reads 100 height values
    2. Builds a 10x10 matrix
    3. Finds min/max height
    4. Simulates 10 water levels from min to max
    5. Prints flood map for each water level
    """
    n = 10  # size of the square matrix
    total_values = n * n

    print(f"Hey cutie 💖, enter {total_values} height values separated by space:")

    # 🧠 Input: read 100 floats from user
    values = list(map(float, input().split()))

    # 💅 Check if input is valid
    if len(values) != total_values:
        print("Uh-oh 😟 You didn’t enter exactly 100 values.")
        return

    # 🌍 Build the 10x10 height matrix
    heights = []
    for i in range(n):
        row = values[i*n : (i+1)*n]
        heights.append(row)

    # 📈 Get min and max heights
    min_height = min(values)
    max_height = max(values)

    # 🪜 Step size: divide the range into 10 levels
    step = (max_height - min_height) / 10

    print("\n⛲ Flood simulation begins... 💦\n")

    for i in range(10):
        water_level = min_height + step * i
        print(f"\nWater level: {water_level:.2f} m")
        flood = flood_map(heights, water_level)
        print_flood_map(flood)


# 🔥 Run it
main()
