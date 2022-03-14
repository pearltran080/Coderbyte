def StringChallenge(strParam):
  x = 0
  o = 0
  for i in strParam:
    if i == 'x':
      x += 1
    else:
      o += 1
  if (x != o):
    return False
  else:
    return True
  # code goes here

# keep this function call here 
print(StringChallenge(input()))

'''
Check if count of x's and o's are equal
Score: 10/10
'''