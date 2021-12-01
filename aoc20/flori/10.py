def do(ll):
  nn = list(map(int, ll))
  mm = [*nn]
  nn.sort()
  last = nn[-1] + 3
  nn.append(last)
  rr = [0]
  diffs = [0,0,0]
  while len(nn) > 0:
    poss = list(filter(lambda x: (x-rr[-1] in [1,2,3]), nn))
    prev = rr[-1]
    for x in poss:
      diff = x - prev
      prev = x
      diffs[diff-1]+=1
    del nn[:len(poss)]
    rr.extend(poss)
  adj = create_adj(mm, last)
  print('adj', adj)
  return trav(adj, 0, last, 0, {})

def create_adj(nn, last):
  nn.sort()
  nn.insert(0,0)
  nn.append(last)
  adj = [None] * (last+1)
  for n in nn:
    adj[n] = []
  for n in nn:
    aa = list(filter(lambda x: x-n in [1,2,3], nn))
    adj[n].extend(aa)
  return adj

def trav(adj, u, d, count, memo):
  if u == d:
    return count+1
  for i in adj[u]:
    if i in memo:
      count += memo[i]
    else:
      count = trav(adj, i, d, count, memo)
      memo[i] = count
  return count

with open('10.in', 'r') as input:
  print("res", do(input.read().splitlines()))

