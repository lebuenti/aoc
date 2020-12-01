def do(input):
  ii = list(map(lambda x: int(x), input))  
  for i_idx, i in enumerate(ii):
    for k_idx, k in enumerate(ii[i_idx+1:]):
      if i + k == 2020:
        return i*k
    

with open ('1.in', 'r') as input:
  print(do(input.read().splitlines()))

