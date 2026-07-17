# DECRIPTION: using nesting functions with decorator password is: admin123 


# defining logger first
def logger(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Attempting to access a secure function...")
        func(*args, **kwargs)
        print("[LOG] Action completed.")

    return wrapper

# defining the admin checker second
def requires_admin(func):
    password = "admin123"
    def wrapper(*args, **kwargs):
        user_input = input("Whats the password?: ") 
        if user_input == password: 
            func(*args, **kwargs)
        else: 
            print("❌ Access Denied! Wrong password.")

    return wrapper

# applying them to function 
@logger
@requires_admin
def delete_database():
    print("   💥 BOOM! Database deleted.")

delete_database()