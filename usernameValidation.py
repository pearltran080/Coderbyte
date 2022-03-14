def SearchingChallenge(strParam):
  
  # code goes here
  passed = True

  if (len(strParam) < 4 or len(strParam) > 25):
    passed = False


  if (strParam[0].isdigit()):
    passed = False
  elif strParam[0] == "_":
    passed = False

  if strParam[-1] == "_":
    passed = False

  for i in strParam:
    if i != "_":
      if (i.isdigit() == False and isinstance(i,str) == False):
        passed = False



  return passed

# keep this function call here 
print(SearchingChallenge(input()))

'''
return True is all Rules pass:
- first character is a letter
- username is 4 to 25 chars
- last char is not _
- chars are either ints, letters, or _
Score: 10/10
'''