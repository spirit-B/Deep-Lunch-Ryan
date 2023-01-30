from random import randint
import os
import time

count = 20
comNum = randint(1, 100)


def check_int(input):
  try:
    return int(input)
  except:
    return False


# 횟수가 남아 있는 경우 계속해서 반복
while count >= 0:
  os.system('clear')
  print(f'컴퓨터가 선택한 숫자는 몇 일까요?(현재 남은 횟수 : {count})')
  userNum = input('정답 입력 : ')

  # 남은 횟수가 있는지 체크
  if count < 0:
    os.system('clear')
    print(f'안타깝습니다! 컴퓨터가 선택한 숫자는 {comNum} (이)였습니다!!')
    break
  else:
    # 문자 혹은 범위 밖의 숫자 입력 시 예외 처리
    if (check_int(userNum) is False) or (check_int(userNum) not in range(1, 100)):
      print('잘못된 입력입니다. 1부터 100사이의 "숫자"만 입력 가능합니다.')
      time.sleep(2)
      continue
    else:
      # 정답을 맞췄을 경우
      if check_int(userNum) == comNum:
        print('정답입니다!')
        break
      # 입력한 값이 컴퓨터가 선택한 값보다 높을 경우
      elif check_int(userNum) > comNum:
        print('DOWN!')
        count -= 1
        time.sleep(1)
      # 입력한 값이 컴퓨터가 선택한 값보다 낮을 경우
      elif check_int(userNum) < comNum:
        print('UP!')
        count -= 1
        time.sleep(1)
