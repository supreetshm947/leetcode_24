def reverse_number(num):
  # Reverse the number
  out = []
  while num > 0:
      o = num % 10
      num = num // 10
      out.append(o)
  # Return the number
  return int("".join(list(map(str, out))))

## Example usage:
print(reverse_number(1223)) # Output: 3221
print(reverse_number(987654321)) # Output: 123456789