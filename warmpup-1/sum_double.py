# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum

print(sum_double(1,2))
print(sum_double(3,4))