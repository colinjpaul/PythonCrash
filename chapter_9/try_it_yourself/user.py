class User():

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.last_name = last_name
        Age = 43
        Location = 'Glanmire'
        Weight = '80kg'

    def describe_user(self):
        print('Users first name is ' + self.name.title())
        print('User last name is ' + self.last_name.title())

    def greet_user(self):
        print("How's it going " + self.name.title() + ' ' + self.last_name.title())


user1 = User('colin', 'paul')
user1.describe_user()
user1.greet_user()



