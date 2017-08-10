import turtle
import math

class User:
    # Define the fields and methods for your object here.
    def __init__(self, name, password = None):
        self.user_name = name
        self.password = password
        self.friends = []

    def change_user_name(self, name):
        self.user_name = name

    def change_password(self, password):
        self.password = password

    def add_friends(self, friend):
        self.friends.append(friend)

    def delete_friends(self, enemy):
        self.friends.remove(enemy)

class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.all_users = []

    def print_Network(self):
        counter = 0
        for user in self.all_users:
            print("This is the network: ")
            print(counter,": ", user ,"->", user.friends)
            counter = counter + 1
    def add_user(self, user):
         if user is not Network:
             self.all_users.append(user)
         else:
             print("this user name is already taken")

    def add_connection(self, user1, user2):
        user1.add_friends(user2)
        user2.add_friends(user1)

    def get_users (self, user):
        return self.all_users


def main():
    # Define the program flow for your user interface here.
    print("------------------------------------------")
    input("press 'y' if you want to make an account")
    print("------------------------------------------")
    name = input("username:")
    password  = input("password:")
    print("welcome", name, "!")

    user1 = User(name, password)
    friends = Network()



    print("-----------------------------------------")
    input("press 'y' if you want to add connections")
    print("-----------------------------------------")
    user2 = User(input("1st friend:"))
    user3 = User(input("2nd friend:"))
    friends.add_connection(user1, user2)
    friends.add_connection(user1, user3)


    print("congratulations! you just became friends with", user2.user_name, "and", user3.user_name, "!!")
    print("-----------------------------")
    input("press 'y' to unfriend someone")
    print("-----------------------------")
    print("who do you want to unfollow?")
    user1 = input("unfollow:")
    user2 = input("unfollow:")

    print("you just blocked", user1, "and", user2, ":(")
    friends.print_Network()


if __name__ == '__main__':
    main()
