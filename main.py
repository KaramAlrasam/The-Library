import os
mainDic={}
def clear():
  os.system("cls" if os.name=="nt" else "clear")
while True:
  print("\nMenu:\n")
  print("1- Add book.")
  print("2- Chick out book.")
  print("3- Chick in  book.")
  print("4- List books.")
  print("5- Exit.")
  user = input("Enter your choice (1-5): ") 
  clear()
  if user=="1":
    
    while True :
      innerDic={}
      user=input("Enter the ISBN: ")
      if user.isdigit():
         innerDic['ISBN']=user
        
      else:
        raise ValueError ("You must add integer")
      user=input("Enter Tital: ")
      innerDic['tital']=user
      user =input("Enter auther: ")
      innerDic['auther']=user
      innerDic['available']=True
      mainDic[len(mainDic)+1]=innerDic
      print(f"Book {innerDic['tital']} by {innerDic['auther']} added to the catalog with ISBN {innerDic['ISBN']}")
      user=input("Do you want add another book (y,n): ").lower()
      if user== "y":
         clear()  
      else:
         clear()
         break 
  elif user=="2":
    while True:
      user=input("Enter ISBN to check out: ")
      if user.isdigit():
        for key in mainDic:
          if mainDic[key]['ISBN']==user and mainDic[key]['available']==True:
            print(f"Book {mainDic[key]['tital']} checked out successfully.")
            mainDic[key]['available']=False
          elif mainDic[key]['ISBN']==user and mainDic[key]['available']==False:
            print("Sorry this book has been checked out.")
      else:
        print("We don't have this book!!!")
      user=input("Do you want ckick out another book (y, n): ").lower()
      if user=="n":
        break            
  elif user=="3":
    user=input("Enter the ISBN to ckick in: ")
    for key in mainDic:
      if mainDic[key]['ISBN']==user:
         mainDic[key]['available']=True
         print("The book has been chicked in successfully.")
         
  elif user=="4":
    while True:
      print("Library Catalog:\n")
      for key in mainDic:
          print(f"ISBN:{mainDic[key]['ISBN']}, Tital: {mainDic[key]['tital']}, Author: {mainDic[key]['auther']}, Available: {mainDic[key]['available']}")

      user=input("Do you want to go back to the main menu? (y,n): ").lower()
      if user=="y":
        clear()
        break
  elif user=="5":
    print("Existing...")
    break
  else:
    print("Invaled input!!!")
    