def BinaryToNumber(Binary):
    result = 0
    length = len(Binary) - 1
    for Title in range(len(Binary)):
        result += int(Binary[Title]) * (2 ** length)
        length -= 1
    return result

while True:
  INP = input("Please enter binary: ")
  check = False
  for i in range(len(INP)):
    if INP[i] != "0" or INP[i] != "1":
      check = True
      break

  if check == True:
    print("NO")
    pass
  else:
    print("Yes")
    break

if int(INP) < 0:
    while int(INP) < 0:
        print("Invalid binary number! Please enter only 0s and 1s.")
        INP = input("Please enter binary: ")
print(f"The number this binary translated to is {BinaryToNumber(INP)}.")
