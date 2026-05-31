def __main__():
  S = input()
  alf = "abcdefghijklmnopqrstuvwxyz"
  
  for i in alf:
    if i in S:
      continue
    else:
      print(i)
      break
if __name__ == "__main__":
  __main__()