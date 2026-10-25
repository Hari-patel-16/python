# Define the parameters of the sequence
start_value = 15
step = 10
# Replace 105 with your actual ending number (e.g., 95, 155, etc.)
end_value = 105

# Generate the sequence and calculate the sum
sequence = range(start_value, end_value + 1, step)
total_sum = sum(sequence)

# Print the results
print("Your sequence:", list(sequence))
print("The sum of the sequence is:", total_sum)
