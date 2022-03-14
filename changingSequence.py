def ArrayChallenge(arr):

  # code goes here
  index = 0
  increase = False
  decrease = False
  for i in range(len(arr)):
    if ( i+1 < len(arr) and arr[i+1] > arr[i]):
      if decrease == True:
        return index
      index += 1
      increase = True
      continue

    if increase == False:
      if ( i+1 < len(arr) and arr[i+1] < arr[i]):
        if increase == True:
          return index
        index += 1
        decrease = True
  
  return -1

# keep this function call here 
print(ArrayChallenge(input()))

'''
Return index of when the integers in the array stop increasing or stop decreasing (only once)
-1 if the direction never changed
Score: 5/10

1. For input [1, 2, 4, 6, 4, 3, 1] the output was incorrect. The correct output is 3

2. For input [1, 2, 1] the output was incorrect. The correct output is 1

3. For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 1] the output was incorrect. The correct output is 8

4. For input [4, 5, 6, 5, 4, 2, 1] the output was incorrect. The correct output is 2

5. For input [100, 101, 102, 101] the output was incorrect. The correct output is 2
'''