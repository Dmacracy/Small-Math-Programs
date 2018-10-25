import sys

def wonder(n):
 '''This function tries to 
    determine if a given natural number
    is a 'wondrous' number.'''
  print(n)
  if n != 1:
    if n % 2 == 0:
      wonder(n / 2)
    else:
      wonder(3 * n + 1)
  else:
   print('Wonder!')

if __name__ == '__main__':
  wonder(int(sys.argv[1]))
