import json
from datetime import datetime
import sys

try:
    with open("products.json", "r") as file:
        loaded_products = json.load(file)

    with open("customers.json", "r") as file:
        loaded_customers = json.load(file)

    with open("sales.json", "r") as file:
        loaded_sales = json.load(file)

except FileNotFoundError:
    print("Error: A required JSON file was not found!")
    sys.exit()

except json.JSONDecodeError:
    print("Error: A JSON file contains invalid data!")
    sys.exit()

products = loaded_products
customers = loaded_customers
sales = loaded_sales

if not isinstance(products, list):
    print("Invalid products data!")
    sys.exit()

if not isinstance(customers, list):
    print("Invalid customers data!")
    sys.exit()

if not isinstance(sales, list):
    print("Invalid sales data!")
    sys.exit()

for product in products:
    if not isinstance(product, dict):
        print("Error: Invalid product record!")
        sys.exit()

    if not all(key in product for key in ("name", "price", "quantity")):
        print("Error: Product information is incomplete!")
        sys.exit()

    if not isinstance(product["name"], str) or not product["name"].strip():
        print("Error: Invalid product name!")
        sys.exit()

    if isinstance(product["price"], bool) or not isinstance(product["price"], (int, float)) or product["price"] <= 0:
        print("Error: Invalid product price!")
        sys.exit()

    if isinstance(product["quantity"], bool) or not isinstance(product["quantity"], int) or product["quantity"] < 0:
        print("Error: Invalid product quantity!")
        sys.exit()
        

for customer in customers:
    if not isinstance(customer, dict):
        print("Error: Invalid customer record!")
        sys.exit()

    if not all(key in customer for key in ("cust_id", "name", "phone")):
        print("Error: Customer information is incomplete!")
        sys.exit()

    if not isinstance(customer["cust_id"], str) or not customer["cust_id"].strip():
        print("Error: Invalid customer ID!")
        sys.exit()

    if not isinstance(customer["name"], str) or not customer["name"].strip():
        print("Error: Invalid customer name!")
        sys.exit()

    if not isinstance(customer["phone"], str) or not customer["phone"].strip():
        print("Error: Invalid customer phone number!")
        sys.exit()

for sale in sales:
    if not isinstance(sale, dict):
        print("Error: Invalid sales record!")
        sys.exit()

    if not all(key in sale for key in ("product name", "quantity_s", "total_p")):
        print("Error: Sales information is incomplete!")
        sys.exit()

    if not isinstance(sale["product name"], str) or not sale["product name"].strip():
        print("Error: Invalid product name in sales record!")
        sys.exit()

    if isinstance(sale["quantity_s"], bool) or not isinstance(sale["quantity_s"], int) or sale["quantity_s"] <= 0:
        print("Error: Invalid sales quantity!")
        sys.exit()

    if isinstance(sale["total_p"], bool) or not isinstance(sale["total_p"], (int, float)) or sale["total_p"] <= 0:
        print("Error: Invalid sales total!")
        sys.exit()
 



print ("\033[92m=================================")
print ("========")
print ("  AXENOVA TECHNOLOGIES")
print ("BUSINESS MANAGEMENT SYSTEM")
print ("=================================")
print ("========\033[0m")
print ( )
print ("\033[93m Welcome To AXENOVA TECH!\033[0m")



 
 
def view_inventory():
    print("\n\033[96m========== AXENOVA INVENTORY ==========\033[0m")

    if not products:
        print("\033[93mNo products available!\033[0m")
        return

    for product in products:
        if not all(key in product for key in ("name", "price", "quantity")):
            print("\033[91mError: Incomplete product information!\033[0m")
            continue

        if product["quantity"] == 0:
            print("\033[91mOUT OF STOCK!\033[0m")
        elif product["quantity"] <= 5:
            print("\033[91mLOW STOCK!\033[0m")

        print(f"\033[94mProduct: {product['name']}\033[0m")
        print(f"\033[92mPrice: ₦{product['price']:,}\033[0m")
        print(f"\033[96mQuantity: {product['quantity']}\033[0m")
        print("\033[90m----------------------------------------\033[0m")
  
  
 
   
def add_product():
    name = input("Enter product name: ").strip()

    if not name:
        print("Product name cannot be empty!")
        return

    try:
        price = int(input("Enter product price: "))
        if price <= 0:
            print("Price must be greater than zero!")
            return

        quantity = int(input("Enter product quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

    except ValueError:
        print("Invalid input! Enter whole numbers for price and quantity.")
        return

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    products.append(product)
    if save_files ( ):
    	print("\033[92mProduct added and saved successfully!\033[0m")
    else:
    	print ("\033[91mProduct added, but saving failed!\033[0m")
  


def manage_customers ( ):
	while True:
		name = input ("What is your name? ").strip ( )
		if not name:
			print ("\033[91mName cannot be empty!\033[0m] ")
			continue
		print ("\033[92mCustomer name accepted!\033[0m ")
		break
		
	while True:
		phone = input ("What is your phone number? ").strip ( )
		if not phone:
			print ("\033[91mPhone number cannot be empty!\033[0m ")
			continue
		print ("\033[92mCustomer phone number accepted!\033[0m ")
		break
		
	customer_id = f"CUST{len(customers) + 1 :03d}"
	
	customer = {"cust_id": customer_id, "name": name, "phone": phone }
	customers.append (customer)
	if save_files ( ):
		print ("\033[92mName and contact info added and saved successfully!\033[0m ")
	else:
		print ("\033[91mCustomer registered, but saving failed! \033[0m")
	
		
		
		
def view_customers ( ):
	print ( )
	print ("\033[92m ========== CUSTOMERS ========== \033[0m")
	if not customers:
		print ("\033[91mNo customer recorded yet!\033[0m ")
	else:
		for customer in customers:
			print ("Customer ID:", "\033[94m",customer["cust_id"], "\033[0m")
			print ("Name:", "\033[93m",customer["name"], "\033[0m")
			print ("Phone:", "\033[95m",customer["phone"], "\033[0m")


def record_sales ( ):
	if not products:
	   print("No products available for sale!")
	   return
	print ( )
	print ("\033[92m========== PRODUCT & PRICE ==========")
	for number, product  in enumerate (products, start = 1) :
		print ( )
		print ("\033[94m", number, "Name:", product["name"], "\033[0m")
		print (f"\033[96mPrice: ₦{product['price']}\033[0m")
		print ("Quantity:", product["quantity"])
		print ("--------------------")
	while True:
		print ( )
		try:
			choice = int(input("Select a product from the list: "))
		except ValueError:
			print ("\033[91mplease Enter a number!\033[0m ")
			continue
	
		if choice < 1 or choice > len(products) :
			print ("\033[91mPlease choose from the avaliable product!\033[0m")
			continue
		
		else:
			selected_product = products [choice - 1]
			print (f"\033[92m{selected_product['name']} selected\033[0m")
			print (f"\033[96mPrice: ₦{selected_product['price']}\033[0m")
			print (f"Quantity: {selected_product['quantity']}")
		
		try:
			quant = int(input(f"How many {selected_product['name']} are you buying: "))
		except ValueError:
			print ("\033[91mPlease Enter a number!\033[0m ")
			continue
		
		if not quant:
			print ("\033[91mQuantity required!\033[0m")
			continue
		
		elif quant < 1 :
			print ("\033[91mQuantity must be at least 1!\033[0m")
			continue
			
		elif quant > selected_product["quantity"]:
			print ("\033[91mInsufficient stock!\033[0m")
			continue
		
		else:
			old_quantity = selected_product["quantity"]
			selected_product["quantity"] = selected_product["quantity"] - quant
			total = selected_product["price"] * quant
			if selected_product["quantity"] == 0 :
				print ("\033[91mOUT OF STOCK\033[0m")
			elif selected_product["quantity"] <= 5 :
				print ("\033[91mLOW STOCK! \033[0m")
			
			print ( )
			print (f"\033[92mPurchasing of {selected_product['name']} was successful!\033[0m ")
			
			print ("---------------")
			print (f"₦{selected_product['price']} x {quant} ")
			print (f"\033[96mTotal price: ₦{total}\033[0m")
			print ("Date & Time:", "\033[96m", datetime.now ( ).strftime("%Y-%m-%d %H:%M"), "\033[0m")
			
			break
	sale ={"product name":selected_product["name"], "quantity_s": quant, "total_p": total, "date_time": datetime.now ( ).strftime("%Y-%m-%d %H:%M") }
	sales.append(sale)
	
	if save_files ( ):
		print ("\033[92mSale recorded and saved successfully!\033[0m ")
	else:
		selected_product["quantity"] = old_quantity
		sales.pop ( )
		print ("\033[91mSale recorded, but saving failed!\033[0m")
	


def view_sales ( ):
	if not sales:
			print ("\033[91mNo sales record yet!\033[0m ")
	else:
		print ( )
		print ("\033[92m============= SALES =============\033[0m")
		for sale in sales:
			print ("\033[94m", "Product name:", sale["product name"], "\033[0m")
			print ("\033[93m", "Quantity sold:", sale["quantity_s"], "\033[0m")
			print (f"\033[92m Total price: ₦{sale['total_p']}\033[0m")
			if "date_time" in sale:
				print(f"Date & Time: \033[96m {sale['date_time']}\033[0m")
			else:
				print("Date & Time: \033[91mDate unavailable\033[0m")
			print ("-------------------------")



def view_business_reports ( ):
	if not sales:
	   print("No sales recorded yet!")
	   return
	total_rev = 0
	total_quant = 0
	for sale in sales:
		total_rev += sale["total_p"]
		total_quant += (sale["quantity_s"])
	total_sal = len(sales)
	
	print ( )
	print ("\033[92m========== BUSINESS REPORTS ==========\033[0m")
	print ("\033[94m", "Total sales:", total_sal, "\033[0m")
	print ("\033[93m", "Total product sold:", total_quant, "\033[0m")
	print (f"Total revenue: \033[92m₦{total_rev} \033[0m")
	report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(f"Report Date & Time: \033[96m{report_time}\033[0m")
	print ()
	print ("-----------------------------------")
		


def save_files( ):
    try:
        with open("products.json", "w") as file:
        	json.dump(products, file, indent=4)
        
        with open("customers.json", "w") as file:
        	json.dump(customers, file, indent=4)
        
        with open("sales.json", "w") as file:
        	json.dump(sales, file, indent=4)
    
    except OSError as error:
    	print (f"Error saving files: {error}")
    	return False
    return True

    
       
        
			

while True:
 print ( )
 print ("1.\033[94mView Products and Inventory\033[0m")
 print ("2.\033[94mManage Customers\033[0m")
 print ("3.\033[94mRecord Sales\033[0m")
 print ("4.\033[94mView Business Reports\033[0m")
 print ("5.\033[94mAdd Product\033[0m")
 print ("6.\033[94mView Customers\033[0m")
 print ("7.\033[94mView Sales\033[0m")
 print ("8.\033[91m Exit\033[0m")
 
 choice = input ("Select an option from 1 to 8:")
 if choice == "1":
  view_inventory ( )
 
 elif choice == "2":
  manage_customers ( )
  
 elif choice == "3":
  record_sales ( )
 
 elif choice == "4":
  view_business_reports ( )
 
 elif choice == "8":
  print ("\033[92mThank you for using Axenova Technologies!\033[0m")
  break
 
 elif choice == "5":
  add_product ( )
 
 elif choice == "6":
  view_customers ( )
 
 elif choice == "7":
  view_sales ( )
  
  
 else:
  print ("Invalid option! ")
  

