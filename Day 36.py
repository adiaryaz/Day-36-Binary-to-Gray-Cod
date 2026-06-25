def binary_to_gray(binary_str):
    """
    Function to convert a binary number to its corresponding Gray Code.
    :param binary_str: The input binary string.
    :return: The converted Gray Code string.
    """
    gray_code = binary_str[0]
    for i in range(1, len(binary_str)):
        gray_bit = str(int(binary_str[i - 1]) ^ int(binary_str[i]))
        gray_code += gray_bit
    return gray_code

binary_input = input("Enter a binary number to convert into Gray Code: ")

if all(bit in '01' for bit in binary_input):

    result = binary_to_gray(binary_input)
    # Display the result
    print(f"Binary number: {binary_input}")
    print(f"Corresponding Gray Code: {result}")
else:
    print("Invalid input. Please enter a valid binary number consisting only of 0's and 1's.")