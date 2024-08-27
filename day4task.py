import os 

counter = 0

def increment_counter():
    global counter
    counter += 1
    print (f"global counter{counter}")

def reset_counter():
    counter = 0
    print (f"local counter{counter}")

increment_counter()
increment_counter()  
increment_counter()

reset_counter()

print(f"Global counter : {counter}")

print(f"Current working directory: {os.getcwd()}")
print("Files and directories in the current directory:")
for item in os.listdir():
    print(item)

os.makedirs('test_dir', exist_ok=True)
print("Created directory 'test_dir'")

os.chdir('test_dir')
print(f"Changed working directory to: {os.getcwd()}")

with open('test_file.txt', 'w') as file:
    file.write("This is a test file.")
print("Created file 'test_file.txt'")

os.remove('test_file.txt')
print("Deleted file 'test_file.txt'")

os.chdir('..')  
os.rmdir('test_dir')
print("Deleted directory 'test_dir'")

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    finally:
        print("Division operation completed.")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = divide_numbers(num1, num2)
    if result is not None:
        print(f"Result of division: {result}")
except ValueError:
    print("Invalid input. Please enter numerical values.")





