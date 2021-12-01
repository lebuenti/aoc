def get_seat(rows, row_idx, seat_idx, row_calc, seat_calc):
  row_idx = int(row_idx)
  seat_idx = int(seat_idx)
  first = True
  while rows[row_idx][seat_idx] == '.' or first:
    row_idx+=row_calc
    seat_idx+=seat_calc
    if row_idx < 0 or row_idx >= len(rows):
      return None
    if seat_idx < 0 or seat_idx >= len(rows[row_idx]):
      return None
    first = False
  return rows[row_idx][seat_idx]

def pprint(rows):
  for row in rows:
    if row == None:
      print([None] * len(row))
    else:
      print(''.join(row))

def do(ll):
  rows = []
  for l in ll:
    rows.append([s for s in l])
  change = True
  while change == True:
    change = False
    cp = [None] * len(rows)
    for row_idx,row in enumerate(rows):
      cp[row_idx] = [None] * len(row)
      for seat_idx,seat in enumerate(row):
        if seat == 'L' or seat == '#':
          adj = [
            get_seat(rows, row_idx, seat_idx, 0, -1), get_seat(rows, row_idx, seat_idx, 0, +1),  # left, right
            get_seat(rows, row_idx, seat_idx, -1, 0), get_seat(rows, row_idx, seat_idx, 1, 0),  # top, bottom
            get_seat(rows, row_idx, seat_idx, -1, -1), get_seat(rows, row_idx, seat_idx, -1, +1),  # top left, top right
            get_seat(rows, row_idx, seat_idx, +1, -1), get_seat(rows, row_idx, seat_idx, 1, 1),  # bottom left, bottom right
          ]
          if seat == 'L':
            if '#' not in adj:
              cp[row_idx][seat_idx] = '#'
              change = True
            else:
              cp[row_idx][seat_idx] = rows[row_idx][seat_idx]
          elif seat == '#':
            if len(list(filter(lambda x: x == '#', adj))) >= 5:
              cp[row_idx][seat_idx] = 'L'
              change = True
            else:
              cp[row_idx][seat_idx] = rows[row_idx][seat_idx]
        else:
            cp[row_idx][seat_idx] = '.'
    rows = cp
    pprint(rows)
  occ = 0
  for row in rows:
    for seat in row:
      if seat == '#':
        occ+=1
  return occ

with open('11.in', 'r') as input:
  print("res", do(input.read().splitlines()))

