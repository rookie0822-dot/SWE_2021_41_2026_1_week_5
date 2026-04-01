def isHappy(n):
  a = set()
  while n != 1:
    if n in a:
      return False
    a.add(n)

    N = 0
    while n > 0:
      digit = n % 10
      N += digit*digit
      n = n//10

    n = N


  return True

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
    
    print("Results saved to /app/bind_mount/output.txt")