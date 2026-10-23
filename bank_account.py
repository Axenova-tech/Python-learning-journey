import random
from datetime import datetime
accounts = []
  
def create_account():
  name = input("What is your name? ")
  while True:
    PIN = input("Create a 4 digits PIN: ")
    if len (PIN) == 4 and PIN.isdigit ( ):
      break
    print ("PIN must be exactly 4 digits! ")
  while True:
    account_number = random.randint(100000, 999999)
    if not any(account["account_number"] == 
    account_number for account in accounts ):
      break
       
  account = {
        "name": name,
        "PIN": PIN,
        "balance": 0,
        "account_number": account_number,
        "created_at": datetime.now(),
        "transactions": [] }          
  accounts.append(account)
  print (f"Your account number is: {account_number}")
  
def login():
  try:  
    account_number = int(input("Enter your account number: "))
  except ValueError:
    print ("Please enter a valid number! ")
    return           
  current_account = None
  for account in accounts:
    if account["account_number"] == account_number:
      current_account = account 
      break 
  if current_account is None:
    print ("Account not found! ")
    return
    
  attempt = 0
  while attempt < 3:
    pin = input("Enter your PIN: ")
    if pin == current_account["PIN"]:
      print ("Access granted!")
      print (f"Welcome {current_account['name']}!")
      print (f"Account number: {current_account['account_number']}")
      break
    else:
      attempt += 1
      print ("Incorrect PIN! ")
    if attempt == 3:
      print ("Too many incorrect password! ")
      print ("Access denied! ")
      return
      
  while True:
    print ("\n----MyBank----")
    print ("1. Check balance")
    print ("2. Deposit")
    print ("3. withdrawl")
    print ("4. view transactions")
    print ("5. Exit")
    print ("6. change PIN")
    print ("7. Account Information")
    print ("8. Transfer")
            
    try:
      choice = int(input("choose an option: "))
    except ValueError:
      print ("Please enter a number from 1-8.")
      continue
    if choice == 5:
      print ("Thank you for using MyBank!")
      break
    elif choice == 1:
      print (f"Your balance is : ${current_account['balance']}")
    elif choice == 2:
      try:
        deposit = int(input("How much do you want to Deposit?  "))
      except ValueError:
        print ("Please enter a valid number")
        continue
      if deposit <= 0:
        print ("Amount must be greater than 0")
      elif deposit > 5000:
        print ("Maximum deposit is $5000")
      else:
        current_account["balance"] += deposit
        current_account["transactions"].append(f"Deposited: ${deposit}")
        print (f"Deposit successful:  ${deposit}- {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    elif choice == 3:
      try:
        withdraw = int(input("How much do you want to withdraw?  "))

      except ValueError:
        print ("Please enter a valid number")
        continue

      if withdraw <= 0:
        print ("withdraw must be greater than 0")

      elif withdraw > current_account["balance"]:
        print ("Insufficient funds!")

      elif withdraw > 3000:
        print ("Maximum withdraw is $3000")

      else:
        current_account["balance"] -= withdraw
        current_account["transactions"].append(f"withdrawn:  ${withdraw}")
        print (f"Withdraw successful: ${withdraw} - {datetime.now().strftime('%Y-%m-%d %H:%M')} ")

    elif choice == 4:
      print("\n-----Transaction History-----")

      for transaction in current_account["transactions"]:
        print (transaction)

    elif choice == 6:
      current_pin = input("Enter your current PIN: ")

      if current_pin == current_account["PIN"]:
        new_pin = input("Enter your new PIN:")
        if len(new_pin) == 4 and new_pin.isdigit():
          if new_pin == current_account["PIN"]:
            print ("New PIN must be different from your current PIN! ")
          else:
            current_account["PIN"] = new_pin
            current_account["transactions"].append("PIN change")
            print ("PIN changed successfully!")
        else:
          print ("PIN must be exactly 4 digits! ")
      else:
        print ("Incorrect PIN")
        
    elif choice == 7:
      print ("\n-----Account Information-----")
      print (f"Name: {current_account['name']}")
      print (f"Account Number: {current_account['account_number']}")
      print (f"Balance:  ${current_account['balance']}")
      print (f"Created At: {current_account['created_at'].strftime('%Y-%m-%d %H:%M')}")
      
    elif choice == 8:
      try:      
        target_number = int(input("Enter account  number to tranfer to:  "))
      except ValueError:
        print ("Please enter a valid number! ")
        continue        
      target_account = None
      for acc in accounts:
        if acc["account_number"] == target_number:
          target_account = acc 
          break
      if target_account is None:
          print ("Account not found! ")                    
          continue
      try:          
        amount = int(input("How much do you want to transfer?  "))
      except ValueError:
        print ("Please enter a valid number! ")
        continue        
      if amount <= 0:
        print ("Amount must be greater than 0! ")
        continue
      if amount > current_account["balance"]: 
        print ("Insufficient balance! ")
        continue  
      current_account["balance"] -= amount
      target_account["balance"] += amount 
      print ("Transfer successful!")
      print (f"Transferred: ${amount} to {target_account['name']}")
      current_account["transactions"].append(f"Transferred: {amount} to {target_account['account_number']} - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
      target_account["transactions"].append(f"Received: {amount} from {current_account['account_number']} - {datetime.now().strftime('%Y-%m-%d %H:%M')}")  
                                                                            
    else:      
      print("Invald option. Please choose from 1-8.")
                                   
while True:      
  print ("\n------MyBank------")
  print ("1. Create Account")
  print ("2. Login")
  print ("3. Exit")
  
  choice = input("choose an option: ")
  if choice == "1":
    create_account()                                                     
  elif choice == "2":
    login()
  elif choice == "3":
    print("Thank you for using MyBank! ")
    break
    
