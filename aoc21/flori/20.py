#!/usr/bin/env python3


with open('20.in', 'r') as f:
  alg, img  = f.read().split("\n\n")
  img = img.splitlines()

print(alg)
print(img)

def nice(img):
  for i in img:
    print(i)
  print()

def pad(img, p=3, s='.'):
  pad = [*img]
  for _ in range(p):
    pad.insert(0, s*(len(pad[0])))
    pad.append(s*(len(pad[0])))
  for y in range(len(pad)):
    pad[y] = (s*p) + pad[y] + (s*p)
  return pad

print('xx', alg[33], alg[34], alg[35])
print()

I = pad(img)
nice(I)

for c in range(50):
  O = []
  for y in range(len(I)-2):
    O.append('')
    for x in range(len(I[y])-2):
      #print(I[y][x], end='')
      w = [
        I[y][x:x+3],
        I[y+1][x:x+3],
        I[y+2][x:x+3],
      ]
      binstr = ''.join(['1' if c == '#' else '0' for c in ''.join(w)])
      dec = int(binstr,2)
      v = alg[dec]
      O[-1] += v
      #print(binstr, dec, v)
      #print()
      #for x in w:
      #  print(x)
      #prfnt()

  if c % 2 != 0:
    #print('yep')
    I = pad([l[3:-3] for l in pad(O,3,'#')[3:-3]])
  else:
    I = pad(O,3,'#')
  print(c+1, ''.join(I).count('#'))
  nice(I)

