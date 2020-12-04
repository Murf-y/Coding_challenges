def two_sum(numbers, target):
      for i in numbers:
          for j in numbers:
              if j + i == target:
                  a = numbers.index(i)
                  b = numbers.index(j) 
                  if a != b:
                      return (a, b)
                  else:
                      c = b + 1
                      return (a, c)
