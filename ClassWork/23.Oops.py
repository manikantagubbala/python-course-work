#Object Oriented Programming Language
#Class is blueprint & used to create objects
#Object is a specific instance created from the class
#Attributes(variables), it stores the data related to the object
#Methods(functions), it defines behaviors or action the object can perform
#Instances
#Types of Instances 1.Instance, 2.Class, 3.Static


#constructor

class Instagram:
    def __init__(self,username,password):
        self.bio = ""
        self._likes = 0
        self.followers = []
        self.following = []
        self.post = []
        self.username = username
        self.__password = password
        print(f'Username : {self.username} \n ')
    
    #protected
    @property
    def like(self):
        return self._likes
    
    @like.setter
    def like(self,upd_like):
        self._likes = upd_like

    #private
    def password_private(self):
        return self.__password
    
    def update_password(self,new_pwd):
        self.__password = new_pwd

#Object creation
user_name = Instagram("mani_112", "M@ni1234")

print("Before modifying: ")
print("Bio: ",user_name.bio)
print("Followers: ",user_name.followers)
print("Following: ",user_name.following)
print("Post: ",user_name.post)
print("UserName: ",user_name.username)
#print("Password: ",user_name.password)

print("\nAfter Modifying: ")
user_name.bio = "peace"
user_name.followers.extend(['aditya','venky','eswar','surya'])
user_name.following.extend(["jntr","priyanka","mani"])
user_name.post.append("Normal.jpg")

print("Bio: ",user_name.bio)
print("Followers: ",user_name.followers)
print("Following: ",user_name.following)
print("Post: ",user_name.post)


#private
print("\nPassword: ", user_name.password_private())
user_name.update_password("mani")
print("New Password: ", user_name.password_private())

#protected
print("likes : ",user_name._likes)