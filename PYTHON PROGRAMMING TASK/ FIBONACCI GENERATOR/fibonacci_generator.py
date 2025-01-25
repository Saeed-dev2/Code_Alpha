
def fibonacci_generator(limit):
    """
    Generate Fibonacci numbers up to the specified limit.
    :param limit: The number of terms or the maximum value to generate.
    """
    a, b = 0, 1  # Initial two Fibonacci numbers
    count = 0

    while count < limit:
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update to the next numbers in the series
        count += 1


# Get user input
n = int(input("Enter the number of Fibonacci terms to generate: "))

# Generate the Fibonacci series
print(f"Fibonacci series up to {n} terms:")
for num in fibonacci_generator(n):
    print(num)
