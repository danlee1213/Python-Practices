def getbinary(n, binary_string, binary_string_arr):
  if n > 0:
    getbinary(n-1, binary_string + "0", binary_string_arr)
    getbinary(n-1, binary_string + "1", binary_string_arr)
  else:
    binary_string_arr.append(binary_string)


def generateBinaryStrings(n):
# your implementation
  binary_string_arr = []
  getbinary(n, "", binary_string_arr)

  return binary_string_arr
  
    

n = int(input())
print(generateBinaryStrings(n))
