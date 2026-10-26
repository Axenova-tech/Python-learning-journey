from datetime import datetime
import pickle 
games = [ ]
cart = { }
purchases = [ ]


try:
  file = open("Purchases.pkl", "rb")
  purchases = pickle.load( file)
  file.close( )
except FileNotFoundError:
	purchases = [ ]


game = {"title":  "GTA V",  "price":  15000}
games.append(game)

game = {"title":  "Minecraft",  "price":  10000}
games.append(game)

game = {"title": "FIFA 26",  "price": 12000}
games.append(game)

def view_games( ):   
    for game in games :
      print (f"{game[ 'title' ]}  -  ₦{game[ 'price' ]}")
      
      
def buy_game( ):
  game_name =  input("Which game do you want to buy? ").lower().strip()
  
  found = False
  quantity = 0
    
    
  if  game_name in cart:
      quantity  = cart [game_name]
      
  for game in games:
    if game["title"].lower() == game_name:    
      found = True
    	  
      if quantity > 0:
        cart[game["title"].lower()] += 1
        print (f"You now have {cart[game['title'].lower()]} copies of {game['title']}")
        
      else:
    	   	    
    	  cart[ game["title"].lower()] = 1
    	  print(f"You bought {game['title']} for: ₦{game['price']}")
   
  if found is False:
      print ("Game not found!")
      

def   view_cart():   
  total = 0
  for game_name in cart:
    for game in games :
      if game["title"].lower() == game_name:
            
        print (f" {game ['title']} -  ₦{game['price']} x {cart[game_name]}")
        total += game ["price"] * cart[ game_name]
  print (f"Total: ₦{total}") 
  
    
def search_game():
  game_name = input("Which game do you want to search? ").lower().strip()
  found = False
  for game in games:
    if game['title'].lower() == game_name:
      found = True
      print (f"{game['title']} - ₦{game['price']}")
  if found is False:
    print ("Game not found! ")
     

def remove_game():
  game_name = input("Which game do you want to remove? ").lower().strip()
  if game_name in cart:
    del cart[game_name]
    print (f"{game_name} removed from cart! ")
  else:
    print ("Game is not in your cart! ")
    
def view_purchases( ):
  print("-------History Purchase-------")
  if not purchases:
    print ("No purchases yet! ")
    return
  
  for number, purchase in enumerate(purchases, start = 1):
    print (f"Purchase ID: {number}")
    print(f"Date: {purchase['date'].strftime('%Y-%m-%d %H:%M')} ")
    total = 0
    for game_name in purchase["items"]:
      for game in games:
        if game["title"].lower() == game_name:
          total += game["price"] * purchase ["items"] [game_name]
        	
          print(f"{game ['title']} -  ₦{game ['price']} x {purchase[ 'items' ] [game_name]}")
    print(f"Purchase Total:  ₦{total}")
    print("--------------------------------------------")
def checkout():
  print ("-------Checkout-------") 
  if not cart:
    print ("Your cart is empty! ")
    return
    
  total = 0
  for game_name in cart:
    for game in games:
    	if game["title"].lower() == game_name:
    	  total += game["price"] * cart[game_name]
  print(f"Total: {total}")
  confirm = input("Do you want to checkout?  yes/no:").lower().strip()
  if confirm == "yes":
    purchase_date = datetime.now()
    print ("Purchase successful ! ")
    purchases.append({"items": cart.copy(),  "date": purchase_date})
    cart.clear()
  else: print ("Checkout cancelled ! ")
    	
    
    
while True:
	
  print ("------Game Store------")
  print ("1. View Game")
  print ("2. Buy Game")
  print ("3. View cart")
  print ("4. Search Game")
  print ("5. Remove Game")
  print ("6. Exit")
  print ("7. Checkout")
  print ("8. Purchase History")
  
  try:
    choice = int(input("choose an option: "))
  except ValueError:
    print("Please enter a number")
    continue

  if choice == 1:
    view_games( )

  elif choice == 2:
    buy_game()
    
  elif  choice == 3:
     view_cart()   
      
  elif choice == 4:
    search_game()   
      
  elif choice == 5:
    remove_game()
   
  elif choice == 6:
    print ("Goodbye! ")
    break
    
  elif choice == 7:
    checkout()
    
  elif choice == 8:
    view_purchases()
  
  else:
    print ("Invalid option! ")
    
    
file = open ("Purchases.pkl", "wb")
pickle.dump(purchases, file)
file.close( )           
