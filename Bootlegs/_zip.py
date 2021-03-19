def _zip(*data):
  return [tuple(x[i] for x in data) for i in range(len(data[0]))]
