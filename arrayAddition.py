def ArrayChallenge(arr):

  # code goes here
  largest = max(arr)
  bestSum = 0

  arr.remove(largest)
  lst = []
  for i in arr:
    arr.remove(i)
    temp = []
    for j in arr:
      temp.append(j)
    arr.append(i)
    lst.append(temp)
  
  for l in lst:
    for n in l:
      if bestSum + n <= largest:
        bestSum += n
      if bestSum == largest:
        return True
    bestSum = 0
  

  return False

# keep this function call here 
print(ArrayChallenge(input()))

'''
Return true if the sum of any subset of integers in arr(-largest int) is equal to the largest integer
Score: 6/10

1. For input [1,2,3,4] the output was incorrect. The correct output is true

2. For input [10,20,30,40,100] the output was incorrect. The correct output is true

3. For input [54,49,1,0,7,4] the output was incorrect. The correct output is true

4. For input [31,2,90,50,7] the output was incorrect. The correct output is true
'''