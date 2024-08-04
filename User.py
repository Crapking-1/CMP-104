from myproject.user import User

class User:
    def register(self, name, phone, email, password):
        return name
    def login(self, email, password):
        if email =="test@mail.com" and password=="abc123" :

            return True
        else:
            return False
print(User.login("self", "email", "password"))
user = User()
user.register("Ezras",111, "test@mail.com", "abc123")
email = input("Enter Your Email")
password = input("Enter Your Password")

print(User.login(email, "password"))
