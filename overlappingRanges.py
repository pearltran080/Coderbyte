def ArrayChallenge(arr):

  # code goes here
  lst1 = []
  lst2 = []
  for i in range(arr[0], arr[1]+1):
    lst1.append(i)
  for j in range(arr[2], arr[3]+1):
    lst2.append(j)

  print(lst1, lst2)

  count = 0
  for i in lst1:
    if i in lst2:
      count += 1
  
  if count == arr[4]:
    return True
  return False

# keep this function call here 
print(ArrayChallenge(input()))

'''
Given 5 integers in an array, [0] and [1] is a range. [2] and [3] is a range. [4] is a number.
If the ranges overlap, return true if the overlap count is equal to [4]
Score: 7/10

1. For input [1,2,1,3,1] the output was incorrect. The correct output is true

2. For input [1,10,9,10,1] the output was incorrect. The correct output is true

3. For input [4,10,5,8,2] the output was incorrect. The correct output is true
'''