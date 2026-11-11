import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
  print("Not a quadatic equation")
else:
  d = b**2 - 4*a*c
  if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Two Real Roots:", root1, "and", root2)
  elif d == 0:
    root = -b / (2*a)
    print("One Real Root:", root)
  else:
    realPart = -b / (2*a)
    imagPart = math.sqrt(-d) / (2*a)
    print("Complex Roots:", realPart, "+", imagPart, "i and",
          realPart, "-", imagPart, "i")
