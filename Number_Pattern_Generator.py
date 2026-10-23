def number_pattern(n):
    # Check that the argument is an integer.
    # If not, return an error message.
    if not isinstance(n, int):
        return 'Argument must be an integer value.'

    # Check that the integer is greater than 0.
    # If not, return an error message.
    if n < 1:
        return 'Argument must be an integer greater than 0.'

    # Create an empty string to store the pattern.
    pattern = ''

    # Loop through numbers from 1 up to and including n.
    for number in range(1, n + 1):
        # Convert each number to a string and add it to the pattern,
        # followed by a space.
        pattern = pattern + str(number) + ' '

    # Remove the trailing space at the end of the string
    # and return the final pattern.
    return pattern.strip()