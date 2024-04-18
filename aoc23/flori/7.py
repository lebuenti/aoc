#!/usr/bin/env python3

from functools import cmp_to_key

L = open('7.in').read()
ll = L.splitlines()
hands, bids = zip(*[(h, int(b)) for h, b in [l.split(" ") for l in ll]])


for F in [
  ['A', 'K', 'Q', 'J', 'T', *[str(n) for n in [9, 8, 7, 6, 5, 4, 3, 2]]],
  ['A', 'K', 'Q', 'T', *[str(n) for n in [9, 8, 7, 6, 5, 4, 3, 2]], 'J']
]:
  def val(hand):
    hands = [hand]
    if F[-1] == "J":
      for i, h in enumerate(hand):
        if h != "J":
          continue
        for j in range(len(hands)-1, 0, -1):
          for f in F:
            hh = [h1 for h1 in hands[j]]
            hh[i] = f
            hands.append(''.join(hh))
        for f in F:
          hh = [h1 for h1 in hand]
          hh[i] = f
          hands.append(''.join(hh))
    mx = -1
    for h in hands:
      v = -1
      if any(h.count(x) == 5 for x in h):
        # five of a kind
        v = 7
      elif any(h.count(x) == 4 for x in h):
        # four of a kind
        v = 6
      elif any(h.count(x) == 3 for x in h) and any(h.count(x) == 2 for x in h):
        # full house
        v = 5
      elif any(h.count(x) == 3 for x in h):
        # three of a kind
        v = 4
      elif [h.count(x) for x in h].count(2) == 4:
        # two pair
        v = 3
      elif [h.count(x) for x in h].count(2) == 2:
        # one pair
        v = 2
      elif all(h.count(x) == 1 for x in h):
        # high card
        v = 1
      if v == -1:
        raise Exception(f"no value for h: {h}")
      mx = max(mx, v)
    return mx


  def comp(a,b):
    va, vb = val(a), val(b)
    if va == vb:
      assert a != b
      for i in range(len(a)):
        if a[i] != b[i]:
          return F.index(b[i]) - F.index(a[i])
    return va - vb


  X = sorted(hands, key=cmp_to_key(comp))
  print(sum(bids[hands.index(x)] * (i+1) for i, x in enumerate(X)))

