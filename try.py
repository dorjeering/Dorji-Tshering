def find_max(num_list):
  """
  Finds the maximum number in a list of numbers.
  """
  # Step 3: Assume the first number in the list is the largest.
  max_num = num_list[0] 
  
  # Step 4: Iterate through each number in the list.
  for num in num_list:
    # Step 5 & 6: Check and update the largest number if a larger one is found.
    if num > max_num:
      max_num = num
      
  # Step 7: Return the final largest number.
  return max_num

# Example usage:
numbers = input("Enter numbers:")
largest_number = find_max(numbers)
print("Maximum number:", largest_number) # Output: Maximum number: 9
