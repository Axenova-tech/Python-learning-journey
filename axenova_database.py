import sqlite3

connection = sqlite3.connect ("axenova.db")
cursor  = connection.cursor ( )
cursor.execute (""" CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT NOT NULL,
price REAL NOT NULL,
quantity INTEGER NOT NULL,
date_added TEXT)""")

while True:
	print ("\nAXENOVA  DATABASE")
	print ("1. Add Product")
	print ("2. Update Product")
	print ("3. View Products")
	print ("4. Delete Product")
	print ("5. Exit")
	print ( )
	choice = input ("Choose an option: ")
	
	if choice == "1":
		product_name = input ("Enter product name: ").strip ( )
		if product_name == "":
			print ("Product name cannot be empty! ")
			continue
		
		else:
			cursor.execute ("SELECT * FROM products WHERE LOWER (product_name) = ?", (product_name.lower ( ),) )
			product = cursor.fetchone ( )
		if product is None:
			try:
				price = float(input("Enter product price: "))
			except ValueError:
				print ("Invalid input! ")
				continue
			
			if price <= 0:
				print ("Invalid price please Enter a positive number! ")
				continue
			try:
				quantity = int(input("Enter product quantity: "))
			except ValueError:
				print ("Invalid input! ")
				continue
				
			if quantity < 0:
				print ("Invalid quantity please Enter zero or positive number! ")
				continue
			

			date_added = input ("Enter date added: ")
			cursor.execute (""" INSERT INTO products(product_name, price, quantity, date_added)
VALUES (?, ?, ?, ?)""", (product_name, price,quantity, date_added))
			connection.commit ( )
			print ("Product added successfully! ")
	
		else:
			print ("Product already exist! ")
			
	
	elif choice == "3":
		cursor.execute ("SELECT * FROM products")
		products = cursor.fetchall ( )
		for product in products:
			print ("Product ID:", product [0])
			print ("Product name:", product [1])
			print ("Price:", product [2])
			print ("Quantity:", product [3])
			print ("Date added:", product [4])
			print ( )
	
	elif choice == "2":
		while True:
			print ( )
			print ("UPDATE PRODUCT DETAILS")
			print ("1. Update Price")
			print ("2. Update Quantity")
			print ("3. Update Both")
			print ("4. Back to Main Menu")
			print ( )
			
			update_choice = input ("Choose an option: ")
			if not update_choice.isdigit ( ):
				print ("Invalid input! ")
				continue
			
			if update_choice == "1":
				try:
					product_id = int(input("Enter product ID: "))
				except ValueError:
					print ("Invalid product ID! ")
					continue
					
				cursor.execute ("SELECT * FROM products WHERE product_id = ?", (product_id,) )
				product = cursor.fetchone ( )
				if product is None:
					print ("Product ID does not exist! ")
				else:
					try:
						new_price = float(input ("Enter price to update: "))
					except ValueError :
						print ("Invalid input! ")
						continue
					if new_price <= 0 :
						print ("Price must be greater than zero! ")
						continue
						
					cursor.execute ("UPDATE products SET price = ? WHERE product_id = ? ", (new_price, product_id) )
					connection.commit ( )
					print ("Product price updated successfully! ")
			
			elif update_choice == "2":
				try:
					product_id = int(input("Enter product ID: "))
				except ValueError:
					print ("Invalid product ID! ")
					continue
					
				cursor.execute ("SELECT * FROM products WHERE product_id = ?", (product_id,))
				product = cursor.fetchone ( )
				
				if product is None:
					print ("Product ID does not exist! ")
				else:
					try:
						new_quantity = int(input("Enter new product quantity: "))
					except ValueError :
						print ("Invalid input! ")
						continue
					if new_quantity < 0 :
						print ("Quantity cannot be negative! ")
						continue
						
					cursor.execute ("UPDATE products SET quantity = ? WHERE product_id = ?", (new_quantity, product_id))
					
					connection.commit ( )
					print ("New quantity updated successfully! ")
			
			elif update_choice == "3":
				try:
					product_id = int(input("Enter product ID: "))
				except ValueError:
					print ("Invalid product ID! ")
					continue
					
				cursor.execute ("SELECT * FROM products WHERE product_id = ?", (product_id, ))
				product = cursor.fetchone ( )
				
				if product is None:
					print ("Product ID does not exist! ")
				else:
					try:
						new_price = float(input("Enter new price: "))
					except ValueError:
						print ("Invalid input! ")
						continue
					if new_price <= 0 :
						print ("Price must be greater than zero! ")
						continue
					
					try:
						new_quantity = int(input("Enter new quantity: "))
					except ValueError:
						print ("Invalid input! ")
						continue
					if new_quantity < 0 :
						print ("Quantity cannot be negative! ")
						continue
					
					cursor.execute ("UPDATE products SET price = ?, quantity = ? WHERE product_id = ?", (new_price, new_quantity, product_id))
					
					connection.commit ( )
					print ("New price and quantity updated successfully! ")
			
			elif update_choice == "4":
				break
			
			else:
				print ("Please choose an option from 1 to 4! ")
			
	
	elif choice == "4":
		try:
			product_id = int(input("Enter product ID: "))
		except ValueError:
			print ("Invalid product ID! ")
			continue
			
		cursor.execute ("SELECT * FROM products WHERE product_id = ? ", (product_id, ))
		product = cursor.fetchone ( )
		
		if product is None:
			print ("Product does not exist! ")
		else:
			confirm = input ("Do you want to delete this product (yes/no): ").strip ( ).lower ( )
			if confirm == "yes":
				cursor.execute ("DELETE FROM products WHERE product_id = ?", (product_id, ))
				connection.commit ( )
				print ("Product deleted successfully! ")
			
			elif confirm == "no":
				print ("Deletion cancelled! ")
			
			else:
				print ("Invalid confirmation! ")
				
													
	
	elif choice == "5":
		connection.close ( )
		break
			
	else:
		print ("Please choose an option from 1 to 5! ")
		continue

      
