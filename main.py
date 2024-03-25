import uuid

print("Welcome to the Demo Marketplace")

# Database for storing user credentials
user_db = {
    "user1": "pass1", 
    "user2": "pass2"
}

# Database for storing admin credentials
admin_db = {
    "admin1": "pass1", 
    "admin2": "pass2"
}

# Dictionary to store session IDs and associated carts
session_carts = {}
session_id = None


product_catalog = [
    {"ID": 1, "Name": "Boots", "Category": 1, "Price": 100,},
    {"ID": 2, "Name": "Coats", "Category": 2, "Price": 200},
    {"ID": 3, "Name": "Jackets", "Category": 3, "Price": 150},
    {"ID": 4, "Name": "Caps", "Category": 4, "Price": 300}
]


def user_login(username, password):
    if username in user_db:
        if user_db[username] == password:
            session_id = str(uuid.uuid4())
            session_carts[session_id] = []
            return session_id
        else:
            print("Invalid password. Please try again.")
            return None
    else:
        user_db[username] = password
        session_id = str(uuid.uuid4())
        session_carts[session_id] = []
        print("User registration successful!")
        return session_id


def admin_login(admin, password):
    if admin in admin_db:
        if admin_db[admin] == password:
            session_id = str(uuid.uuid4())
            session_carts[session_id] = []
            return session_id
        else:
            print("Invalid password. Please try again.")
            return None
    else:
        print("Admin username not found.")
        return None


def view_cart(session_id):
    if session_id in session_carts:
        print("Cart contents:")
        for item in session_carts[session_id]:
            print(item)
    else:
        print("Session ID not found.")


def add_to_cart(session_id, product_id, quantity):
    pro = [p for p in product_catalog if p['ID'] == product_id]
    if pro:
        pro = pro[0]
        session_carts[session_id].append({"Product": pro, "Quantity": quantity})
        print(f"{quantity} pieces of {pro['Name']} added to the cart.")
    else:
        print("Product ID not found.")


def remove_from_cart(session_id, product_id):
    for item in session_carts[session_id]:
        if item["Product"]["ID"] == product_id:
            session_carts[session_id].remove(item)
            print("Item removed from cart successfully.")
            return
    print("Product ID not found in the cart.")


def payment(session_id, p):
    total = 0
    for i in session_carts[session_id]:
        total += i["Product"]["Price"] * i["Quantity"]

    print("Your order is successfully placed with {'p'} total price: ", total)


def product():
        for item in product_catalog:
            for key, value in item.items():
                print(f"{key}: {value}")
            print()  # Empty line between products
   
        



def add_product(session_id , product_id, name ,category, price):
    
    product_catalog.append( {"ID":product_id , "Name": name, "Category": category, "Price": price })



def mod_product(session_id,aproduct_id):
    for product in product_catalog:
        if product["ID"] == product_id:
            field_to_modify = input("Enter the field you want to modify (Name, Category, Price): ").strip().capitalize()
            new_value = input(f"Enter the new value for {field_to_modify}: ")
            if field_to_modify in product:
                product[field_to_modify] = new_value
                print("Product modified successfully.")
                return
            else:
                print("Invalid field. Please try again.")
                return
    print("Product ID not found.")


def remove_product(session_id, product_id):

    for product in product_catalog:
        if product["ID"] == product_id:
            product_catalog.remove(product)
            print("Product removed from catalog successfully.")
            return
    print("Product ID not found in the catalog.")



def number_choice(c):
    session_id = None
   
    
   
    if c == "1":
        u = input("Enter username: ")
        p = input("Enter password: ")
        session_id = user_login(u, p)
        if session_id:
      
        
         while True:
          action = input("What would you like to do? (view catalog, view cart, add to cart, remove from cart, payment ,exit): ")
          if action == "view cart":
               view_cart(session_id)

          elif action == "add to cart":
               product_id = int(input("Enter product ID: "))
               quantity = int(input("Enter quantity: "))
               add_to_cart(session_id, product_id, quantity)

          elif action == "remove from cart":
               product_id = int(input("Enter product ID: "))
               remove_from_cart(session_id, product_id)

          elif action == "payment":
               p = input("enter your choice form payment : Net banking, PayPal, UPI")
               payment(session_id, p)

          elif action =="view catalog":
               product()

          elif action == "exit":
               break
          else:
               print("Invalid action. Please try again.")
        

    elif c == "2":
        a = input("Enter admin name: ")
        p = input("Enter password: ")
        session_id = admin_login(a, p)
        if session_id:
      
        
         while True:
          action = input("What would you like to do? (view catalog:1, add product:2, modify product:3, remove product:4, exit:5): ")

          if action == "2":
               product_id = input("enter product id: ")
               name = input("enter product name: ")
               category = input("enter category: ")
               price = input ("enter price of product: ")
               add_product(session_id , product_id, name ,category, price)

          elif action == "3":
               product_id = int(input("Enter product ID: "))
               mod_product(session_id,product_id)

          elif action == "4":
               product_id = int(input("Enter product ID: "))
               remove_product(session_id, product_id)

          elif action =="1":
              product()

          elif action == "5":
               break
          else:
               print("Invalid action. Please try again.")
        
    else:
        print("Invalid choice")
    return session_id



j = input("If you're a user, enter 1. If you're an admin, enter 2: ")
session_id = number_choice(j)


