import random

def factor_quadratic_problem_basic():
  '''A Program that randomly generates quadratic functions and asks for the user to factor them.'''
  root1 = random.randint(1, 10)
  root2 = random.randint(1, 10)
  signs = [1, -1]
  sign1 = signs[random.randint(0, 1)]
  sign2 = signs[random.randint(0, 1)]
  root1 *= sign1
  root2 *= sign2
  if root1 + root2 > 0:
    term1 = ' + ' + str(root1 + root2) + 'x'
  elif root1 + root2 < 0:
    term1 = ' - ' + str(abs(root1 + root2)) + 'x'
  elif root1 + root2 == 0:
    term1 = ''
  if bool(sign1) ^ bool(sign2):
    term2 = ' - ' + str(abs(root1 * root2))
  else:
    term2 = ' + ' + str(root1 * root2)
  answer = input("Factor the following quadratic function:\n" + "xx" + term1 + term2 + ' :\n')
  if term1 == '':
    # Handle case of difference of perfect squares:
    if answer == '(x' + ' + ' + str(abs(root1)) + ')(x' + ' - ' + str(abs(root2)) + ')' or \
       answer == '(x ' + ' - ' + str(abs(root1)) + ')(x ' + ' + ' + str(abs(root2)) + ')':
      print('CORRECT!!')
      return 1
    else:
      print('Sorry, we were looking for:')
      print('(x' + ' + ' + str(abs(root1)) + ')(x' + ' - ' + str(abs(root2)) + ')')
      return 0
  else:
    # Handle other cases by determining the string expressions for each factor:
    if str(root1)[0] == '-':
      answerpart1 = '(x - ' + str(abs(root1)) + ')'
    else:
      answerpart1 = '(x + ' + str(abs(root1)) + ')'
    if str(root2)[0] == '-':
      answerpart2 = '(x - ' + str(abs(root2)) + ')'
    else:
      answerpart2 = '(x + ' + str(abs(root2)) + ')'
    if answer == answerpart1 + answerpart2 or answer == answerpart2 + answerpart1:
      print('CORRECT!!')
      return 1
    else:
      print('Sorry, we were looking for:')
      print(answerpart1 + answerpart2)
      return 0
      

if __name__ == '__main__':
  Correct = 0
  Total = 0
  while True:
    Correct += factor_quadratic_problem_basic()
    Total += 1
    print(str(Correct) + '/' + str(Total) + ' questions answered correctly\n')

  
  
