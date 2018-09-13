class User():

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.last_name = last_name
        self.Age = 43
        self.Location = 'Glanmire'
        self.Weight = '80kg'
        self.login_attempts = 0

    def describe_user(self):
        print('Users first name is ' + self.name.title())
        print('User last name is ' + self.last_name.title())
        print('Age is ' + str(self.Age))
        print('Location is ' + self.Location.title())
        print('Weight is ' + self.Weight.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        print("How's it going " + self.name.title() + ' ' + self.last_name.title())


user1 = User('colin', 'paul')

user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(user1.login_attempts)

user1.reset_login_attempts()

print(user1.login_attempts)

