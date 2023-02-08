def gugu():
  i = 1;
  n = input(f'몇 단을 보시겠습니까? : ')
  while i < 10:
    print(f'{n} x {i} = {int(n) * i}')
    i += 1