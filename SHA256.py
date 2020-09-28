from hashlib import sha256

print("The username is \"user\", try to guess the widely used password (Hint: only 4 numbers)\n")
user = input("Enter your username: \n")
password = input("Enter password: \n")

if user == "user" and sha256(password.encode()).hexdigest() == "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4":
    print("Login successful")
else:
    print("Incorrect username or password")
