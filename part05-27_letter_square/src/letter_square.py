# Write your solution here
def print_square(layers):
    if layers < 1 or layers > 26:
        print("Invalid number of layers. Please enter a value between 1 and 26.")
        return

    size = 2 * layers - 1
    center = layers - 1
    square = [['C' for _ in range(size)] for _ in range(size)]

    for layer in range(layers):
        letter = chr(ord('A') + layer)

        for i in range(center - layer, center + layer + 1):
            for j in range(center - layer, center + layer + 1):
                if i == center - layer or i == center + layer or j == center - layer or j == center + layer:
                    square[i][j] = letter

    for row in square:
        print(''.join(row))



print("Sample output\nLayers: 3\n")
print_square(3)

print("\nSample output\nLayers: 4\n")
print_square(4)
