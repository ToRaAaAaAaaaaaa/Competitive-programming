def __main__():
  N = int(input())
  
  S = [input() for _ in range(N)]
  T = [input() for _ in range(N)]
  
  def rotate_quarter(S):
    return list(zip(*S[::-1])) # 90度回転
    
  
  def count_diff(S, T):
    return sum([1 for si, ti in zip(S, T) for sij, tij in zip(si, ti) if sij != tij])
    
  ans = 10**9
  for rot_count in range(4):
    ans = min(ans, count_diff(S, T)+rot_count)
    S = rotate_quarter(S)

  print(ans)
if __name__ == "__main__":
  __main__()