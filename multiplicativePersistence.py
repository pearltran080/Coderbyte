def MathChallenge(num):

  # code goes here
  numb = str(num)
  count = 0
  while len(numb) != 1:
    count += 1
    notYet = numb[0]
    for i in range(1, len(numb)):
      notYet = str(int(notYet) * int(numb[i]))
    numb = notYet


  return count

# keep this function call here 
print(MathChallenge(input()))

'''
Multiplicative Persistence
Given a string of numbers
Multiply the digits in num until the result is a single digit
Score: 10/10
'''