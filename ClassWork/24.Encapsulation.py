#Encapsulaation
#intilized in constructor
# __is defined as private 
# _is defined as protected
import random


class Login:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._otp = 1234

    def getpassword(self):         
        return self.__password
    
    #modify
    def updatepassword(self,newpwd):
        self.__password = newpwd

    #In protected first we define property like that
    @property
    def publicotp(self):
        return self._otp
    
    #modify
    @publicotp.setter
    def publicotp(self,new_otp):
        self._otp = new_otp


log = Login("manikanta","mani123")


#public
print("Assign in public:",log.username)

log.username = "_mani_"
print("New Username: ",log.username)

#private Assign in private
print("Original Password: ",log.getpassword())

log.updatepassword("mani8978")                          #update like this
print("New Password: ",log.getpassword())               #call like this

#protected
print("OTP: ",log.publicotp)

log.publicotp = 9346                                    #update like this 
print("New OTP: ",log.publicotp)                        #call like this
