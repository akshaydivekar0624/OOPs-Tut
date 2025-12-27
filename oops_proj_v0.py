class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
    def menu(self):
        user_input = input(""""Welcome to Chatbook !! How would you like to proceed?)
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("enter your email here -> ")
        pwd = input("setup your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("You need to signup first before signing in !!")
        else:
            uname = input("enter your username -> ")
            pwd = input("enter your password -> ")
            if uname == self.username and pwd == self.password:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Invalid credentials !! Please try again.")
        print("\n")
        self.menu()

    def my_post(self): 
        if self.loggedin == True:
            post_content = input("Write your post here -> ")
            print("Your post has been published successfully !!")
        else:
            print("Please signin to write a post.")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            friend = input("Enter your friend's name -> ")
            message = input("Enter your message -> ")
            print(f"Your message to {friend} has been sent successfully !!")
        else:
            print("Please signin to send messages.")
        print("\n")
        self.menu()

# obj = chatbook()