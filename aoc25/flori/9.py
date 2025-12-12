#/usr/bin/env python3

F = open('9.in').read()
C = [(int(x),int(y)) for x,y in [f.split(",") for f in F.splitlines()]]

xx = sorted({x for x,_ in C})
yy = sorted({y for _,y in C})

xx_c = {xx[i]: i for i in range(len(xx))}
yy_c = {yy[i]: i for i in range(len(yy))}
c_xx = {v: k for k,v in xx_c.items()}
c_yy = {v: k for k,v in yy_c.items()}
C = [(xx_c[x], yy_c[y]) for x,y in C]

mx = -1
for i in range(len(C)-1):
  x,y = C[i]
  for k in range(i+1, len(C)):
    x1,y1 = C[k]
    mx = max([mx, (abs(c_xx[x]-c_xx[x1])+1) * (abs(c_yy[y]-c_yy[y1])+1)])
print(mx)

B = []
for x in xx_c.values():
  arr = sorted({y for x1,y in C if x1 == x})
  assert len(arr) % 2 == 0
  arr = [arr[i:i+2] for i in range(0, len(arr), 2)]
  for i in range(len(arr)):
    B.extend((x,y) for y in range(arr[i][0], arr[i][1]+1))
for y in yy_c.values():
  arr = sorted({x for x,y1 in C if y1 == y})
  assert len(arr) % 2 == 0
  arr = [arr[i:i+2] for i in range(0, len(arr), 2)]
  for i in range(len(arr)):
    B.extend((x,y) for x in range(arr[i][0], arr[i][1]+1))

I = []
for y in range(yy_c[min(yy)], yy_c[max(yy)]+1):
  ins = False
  for x in range(xx_c[min(xx)], xx_c[max(xx)]+1):
    if (x,y) in B:
      if (x-1,y) not in B:
        ins = not ins
    elif ins:
      I.append((x,y))

ALL = {*I, *B, *C}
mx = -1
for i in range(len(C)-1):
  x,y = C[i]
  for k in range(i+1, len(C)):
    x1,y1 = C[k]
    xf,xt = min([x,x1]), max([x,x1])
    yf,yt = min([y,y1]), max([y,y1])
    if all((x2,y2) in ALL for y2 in range(yf, yt+1) for x2 in range(xf, xt+1)):
      mx = max([mx, (abs(c_xx[x]-c_xx[x1])+1) * (abs(c_yy[y]-c_yy[y1])+1)])
print(mx)

