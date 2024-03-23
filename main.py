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


def product(p):
    if p.lower() == "yes":
        for item in product_catalog:
            for key, value in item.items():
                print(f"{key}: {value}")
            print()  # Empty line between products
    else:
        print("What can I serve you?")


def number_choice(c):
    session_id = None
    i = input("Do you want to show the catalog? (yes or no): ")
    product(i)
   
    if c == "1":
        u = input("Enter username: ")
        p = input("Enter password: ")
        session_id = user_login(u, p)
        if session_id:
      
        
         while True:
          action = input("What would you like to do? (view cart, add to cart, remove from cart, payment ,exit): ")
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
          elif action == "exit":
               break
          else:
               print("Invalid action. Please try again.")
        

    elif c == "2":
        a = input("Enter admin name: ")
        p = input("Enter password: ")
        session_id = admin_login(a, p)
        
    else:
        print("Invalid choice")
    return session_id



j = input("If you're a user, enter 1. If you're an admin, enter 2: ")
session_id = number_choice(j)






