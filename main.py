import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nUse only A, B, C or D\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("An Air Liquide end user called you because they cannot enter to their Windows session. "
  "They don't remember their password. "
  "Where is the user:")
  time.sleep(1)
  print ("""  A. At Home
  B. At Office""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_home()
  elif choice in answer_B:
   print ("\nDid the user try to reset password via I Forgot My Password Tool." 
   "Y/N?")
   choice = input(">>> ")
  if choice in yes:
    option_reasons()
  if choice in no:
    print ("\nAsk user to try to use I Forgot My Password Tool. "
    "Did it work. Y/N")
    choice = input(">>> ")
    if choice in yes:
      print ("\nUse '0_EU[Pass reset Win]User led to tool' template to create your ticket" )  
      option_procedure()
    else:
       option_reasons()
  
    

def option_home(): 
  print ("\nConsult with an L2 agent regarding Out Of Office Password Reset procedure. -KB0013920- "
  "Is Level 2 colleague available and can help. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_procedure()
  else:
    option_gooffice()
  
def option_checkada(): 
  print ("Check users account on Active Directory. "
  "Is it expired. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_expiredaccount()
  else:
    print ("\nUse '0_EU[Pass reset Win - tool not present' template to create your intake. "
    "Reset user's password in Active Directory, "
       "call back the user if phone number exists in the system "
       "and close the ticket as an ADHOC after confirming with the user that issue is resolved.")
       
def option_checkadb(): 
  print ("Check users account on Active Directory. "
  "Is it expired. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_expiredaccount()
  else:
    print ("\nUse '0_EU[Pass reset Win-Chal/Resp forgot' template to create your intake. "
    "Reset user's password in Active Directory, "
       "call back the user if phone number exists in the system "
       "and close the ticket as an ADHOC after confirming with the user that issue is resolved.")       
  
def option_checkadc(): 
  print ("Check users account on Active Directory. "
  "Is it expired. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_expiredaccount()
  else:
    print ("\nUse '0_EU[Pass reset Win-Chall/Resp not set' template to create your intake." 
    "Reset user's password in Active Directory, "
       "call back the user if phone number exists in the system "
       "and close the ticket as an ADHOC after confirming with the user that issue is resolved.")
       
def option_checkadd(): 
  print ("Check users account on Active Directory. "
  "Is it expired. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    option_expiredaccount()
  else:
    print ("\nUse '0_EU[Pass reset Win]User refused pwtool' template to create your intake. "
    "Reset user's password in Active Directory, "
       "call back the user if phone number exists in the system "
       "and close the ticket as an ADHOC after confirming with the user that issue is resolved.")  
    
def option_expiredaccount(): 
  print ("\nUse 'GLOBAL - Windows Emergency reactivation' template and Advise user to contact his/her CARM approver" 
  "(or the approver of the CARM approver in case of absence) to raise the" 
  "request for the account reactivation in CARM and close the ticket as an ADHOC.")

def option_procedure():
  print ("\nAfter you confirm with the user that issue is resolved, close the ticket.")
  quit()
    
     
def option_gooffice(): 
  print ("\nInform the user that he/she needs to go to an Air Liquide office to be able to reset the password. And close the ticket")
  
  quit()
  
def option_reasons():
  print ("\nWhy it didn't work?")
  print ("""  A. Windows Password Reset Tool is not present	
  B. Challenges/Responses forgotten
  C. Challenges/Responses not set up
  D. User refused use Password Reset Tool""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_checkada()
  elif choice in answer_B:
    option_checkadb()
  elif choice in answer_C:
    option_checkadc()
  elif choice in answer_D:
    option_checkadd()  
  else:
    print (required)  
    option_reasons()
  
intro()