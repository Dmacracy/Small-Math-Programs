'''This is a program that prints itself'''
with open(__file__, 'r') as Q:
  for line in Q:
    print(line[:-1])
