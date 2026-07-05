t=int(input())


while t>0:
  t-=1
  X=int(input())

  game=list(input())
  carlsen=0 
  chef=0 
  
  for i in game:
      match i:
          case "C":
              carlsen+=2
          case "N":
              chef+=2
          case "D":
              carlsen+=1
              chef+=1
              
  if carlsen>chef:
      print(X*60)
  elif carlsen==chef:
      print(X*55)
  else:
      print(X*40)