Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #player card finder 
#first code is finding out if you have a membership and runing the code if true 
class player:
  membership = True
  def __init__(self,name,age,username,power):
    if (player.membership):
     self.name = name
     self.age = age
     self.username = username 
     self.power = power

  
  def run(self):
    print('run')
    return 'done'
#both player cards and whaat there Name,Age,Username and class is 
p1 = player("Maurice", 17, "crash","wizard")
p2 = player("tyler", 18, "pengion","heavy")
#code to print out the plyers card chanege the p1 ot p2 for a difrint player card 
print(p1.membership)
print(p1.name)
print(p1.age)
print(p1.username)
print(p1.power)

is_magician = True
is_expert = False

#input if or a magician/expert or not, here
if is_magician and is_expert:
 print ('your a master') 
elif is_magician and not is_expert:
 print ("your almost there")  
elif is_expert and not is_magician:
 print ('your smart but you need powers')
elif not is_magician:
 print("you need powers")
#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition
#You can have if statements inside if statements, this is called nested if statements
 # ------------------------------------------------------------------------------------  
  

  # ------------------------------------------------------------------------------------ 
#basic datatime clock that tells the tim eof when the code was run 
import datetime
x = datetime.datetime.now()
print(x)