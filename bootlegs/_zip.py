def _zip(l1, l2):
  bootleg = [(l1[x], l2[x]) for x in range(len(l1))]

  return bootleg


#I ALSO MADE A LAMBDA:

bootlegged = lambda l1, l2: [(l1[x], l2[x]) for x in range(len(l1))]
