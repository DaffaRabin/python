close="no"
while close !="yes":
  print("Welcome to area calculator")
  print("menu")
  print("1.Calculate triange area")
  print("2.Calculate estimated circle area")
  print("3.Calculate paralellogram area")
  choice=input("your choice:")
  if choice ==1:
    base=input("input base:")
    height=input("height:")
    print("area of triangle")
    print(base*height/2)
  if choice ==3:
    base=input("input base:")
    height=input("input height:")
    print("area of paralellogram:")
    print(base*height)
  if choice ==2:
     base=input("input base:")
     print("area of circle:")
     print(base/2*base/2*3.14159)
  close=raw_input("close?(yes/no):")
    
