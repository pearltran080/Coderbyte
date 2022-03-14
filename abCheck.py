def StringChallenge(strParam):
  # code goes here
  length = 0
  for i in range(len(strParam)):
    if strParam[i] == 'a':
      if i+4 < len(strParam) and strParam[i+4] == 'b':
        return True
    if strParam[i] == 'b':
      if i+4 < len(strParam) and strParam[i+4] == 'a':
        return True
  return False

# keep this function call here 
print(StringChallenge(input()))

'''
Check if a is 3 letters apart from b, left or right
Score: 10/10
'''