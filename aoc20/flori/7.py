class Bag:

  def __init__(self, color):
    self.color = color
    self.containing = {}

  def add_containing(self, bag, amount):
    self.containing[bag] = amount

  def containing_colors(self):
    return list(map(lambda b: b.color, self.containing.keys()))

  def total_containing(self):
    res = 0
    for a in self.containing.values():
      res += a
    return res

  def __str__(self):
    containing = {}
    for c in self.containing:
      containing[self.containing[c]] = str(c.color)
    return "Bag{color='%s', containing=%s}" % (self.color, containing)

  def __hash__(self):
      return hash((self.color,))

  def __eq__(self, other):
      return self.color == other.color


def nice(ll):
  bag_containing = []
  for l in ll:
    split = l.split('contain')
    b = Bag(' '.join(split[0].split(' ')[:2]).strip())
    containing = split[1:][0].split(',')
    colors = []
    if 'no other bags' not in containing[0]: 
      for c in containing:
        [amount, *color] = c.strip().split(' ')
        colors.append([int(amount), color[0] + ' ' + color[1]])
    bag_containing.append([b, colors])
  res = []
  for b in bag_containing:
    for ac in b[1:][0]:
      finding = None
      for b1 in bag_containing:
        if b1[0].color == ac[1]:
          finding = [b1[0], ac[0]]
          break
      if finding is None:
        raise Exception("None found for %s" % b[0])
      b[0].add_containing(finding[0], finding[1])
    res.append(b[0])
  return res


def do(ll):
  bb = nice(ll)
  res = []
  t = 'shiny gold'
  for b in bb:
    if t in b.containing_colors():
      res.append(b.color)
      continue
    stack = [*b.containing]
    contains = False
    while len(stack) > 0:
      b1 = stack.pop(0)
      if t in b1.containing_colors():
        contains = True
        break
      stack = [*b1.containing, *stack]
    if contains:
      res.append(b.color)
  print("res1:", len(res))
  shiny_gold_bags = list(filter(lambda x: x.color == t, bb))
  if len(shiny_gold_bags) > 1:
    raise Exception("Didn't expect more than one shiny gold bag")
  shiny = shiny_gold_bags[0]
  res = 0
  stack = [shiny]
  while len(stack) > 0:
    for b, a in stack.pop(0).containing.items():
      res += a
      for i in range(a):
        stack.append(b)
  print("res2", res)


with open('7.in', 'r') as input:
  print("res", do(input.read().splitlines()))

