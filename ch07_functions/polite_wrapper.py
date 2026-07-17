# DECRIPTION: Messing with decorators

def polite_wrapper(func): 
    def wrapper (): 
        name = input ("Enter your name: ")
        print(f"Hello {name}")      # Say hello first
        func()                      # Run the specific message
        print("Have a nice day!")   # say have a nice day last
    return wrapper 

@polite_wrapper 
def morning_message():
    print("     [Hope you slept well!]")

@polite_wrapper
def evening_message(): 
    print("     [Time to pour some tea and relax!]")

# Whichever one is called with automatically wrap 
morning_message()
# evening_message()   # can uncomment to use evening_message()