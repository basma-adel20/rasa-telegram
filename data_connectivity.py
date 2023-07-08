
"""mydatabase = mysql.connector.connect(
  host="containers-us-west-136.railway.app",
  user="root",
  password="YqHSeTjXRJrh1OMaL4An",
  port=6290,
  database="railway",
  auth_plugin='mysql_native_password'
)"""

#mycrursor = mydatabase.cursor()

import mysql.connector
from datetime import date , datetime
import calendar
import pandas as pd
import numpy as np
mydatabase = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase",
  auth_plugin='mysql_native_password'
)

mycrursor = mydatabase.cursor()


################################################ table creations #######################################
# mycrursor.execute("CREATE TABLE user (id int AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100)  ,email VARCHAR(100),weight FLOAT, height FLOAT , activation_rate INT , calories FLOAT ,gender VARCHAR(100) , Age INT , goal INT , password VARCHAR(100), sender_id VARCHAR(300))")
# mycrursor.execute("CREATE TABLE weight_info (id int AUTO_INCREMENT PRIMARY KEY, user_id int NOT NULL, time_taken DATETIME NOT NULL , weight DOUBLE NOT NULL, constraint FK1 FOREIGN KEY (user_id) REFERENCES user(id))")
#mycrursor.execute("CREATE TABLE Login_table (id int AUTO_INCREMENT PRIMARY KEY, user_id int NOT NULL, login_time DATETIME NOT NULL , constraint FK FOREIGN KEY (user_id) REFERENCES user(id))")
# mycrursor.execute("CREATE TABLE food_item (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) ,calory DOUBLE , carb DOUBLE , fat DOUBLE ,proten DOUBLE , size DOUBLE ,type_size VARCHAR(255))")
# mycrursor.execute("CREATE TABLE Breakfast_Meals (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),link VARCHAR(255) )")
# mycrursor.execute("CREATE TABLE breakfast_food (id int AUTO_INCREMENT PRIMARY KEY, breakfast_id int , food_id int,percentage int ,constraint FK16 FOREIGN KEY (breakfast_id) REFERENCES Breakfast_Meals(id) ,constraint FK40 FOREIGN KEY (food_id) REFERENCES food_item(id))")
# mycrursor.execute("CREATE TABLE dinner_Meals (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),link VARCHAR(255) )")
# mycrursor.execute("CREATE TABLE dinner_food (id int AUTO_INCREMENT PRIMARY KEY, dinner_id int , food_id int,percentage int ,constraint FK41 FOREIGN KEY (dinner_id) REFERENCES dinner_Meals(id) ,constraint FK42 FOREIGN KEY (food_id) REFERENCES food_item(id)  )")
# mycrursor.execute("CREATE TABLE lunch_Meals (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),link VARCHAR(1000))")
# mycrursor.execute("CREATE TABLE lunch_food (id int AUTO_INCREMENT PRIMARY KEY, lunch_id int , food_id int,percentage int ,constraint FK43 FOREIGN KEY (lunch_id) REFERENCES lunch_Meals(id) ,constraint FK44 FOREIGN KEY (food_id) REFERENCES food_item(id)  )")
# mycrursor.execute("CREATE TABLE exce (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) , link VARCHAR(300) )")
# mycrursor.execute("CREATE TABLE snack_food (id int AUTO_INCREMENT PRIMARY KEY, snack_id int)")
# mycrursor.execute("CREATE TABLE breakfast_time (send_id VARCHAR(300) , start_time DATETIME , end_time DATETIME, flag int , break_id int, constraint FK45 FOREIGN KEY (break_id) REFERENCES Breakfast_Meals(id))")
# mycrursor.execute("CREATE TABLE lunch_time (send_id VARCHAR(300) , start_time DATETIME , end_time DATETIME , flag int , lunch_id int, constraint FK47 FOREIGN KEY (lunch_id) REFERENCES lunch_Meals(id))")
# mycrursor.execute("CREATE TABLE dinner_time (send_id VARCHAR(300) , start_time DATETIME , end_time DATETIME , flag int , dinner_id int, constraint FK46 FOREIGN KEY (dinner_id) REFERENCES dinner_Meals(id))")
# mycrursor.execute("CREATE TABLE snack_time (send_id VARCHAR(300) , start_time DATETIME , end_time DATETIME , flag int , snack_id int, constraint FK48 FOREIGN KEY (snack_id) REFERENCES snack_food(id))")




################################################### add data to table ########################################
def add_food_database():
    dataframe1 = pd.read_excel('food_table.xlsx')
    data = np.array(dataframe1)
    m = len(data)
    for i in range(m):
      string = "INSERT INTO food_item(name,calory,carb,fat,proten,size,type_size) VALUES ('"
      for j in range(7):
        string +=str(data[i][j])
        if j<6:
           string+="','"
        else:
           string+="')"
      mycrursor.execute(string)     

def add_breakfast_Meals():
    dataframe2 = pd.read_excel('Breakfast_Meals.xlsx')
    dataframe1 = pd.read_excel('Breakfast_food.xlsx')
    data = np.array(dataframe1)
    data2 = np.array(dataframe2)
    m2 = len(data2)
    for i in range(m2):
        string = 'INSERT INTO Breakfast_Meals(name,link) VALUES ("{0}","{1}")'.format(data2[i][0],data2[i][1])
        mycrursor.execute(string) 
    m = len(data)
    for i in range(m):
      string = 'INSERT INTO breakfast_food(breakfast_id,food_id,percentage) VALUES ("{0}","{1}","{2}")'.format(data[i][0],data[i][1],data[i][2])
      mycrursor.execute(string)  

def add_dinner_Meals():
    dataframe2 = pd.read_excel('dinner_meals_link.xlsx')
    dataframe1 = pd.read_excel('dinner_meals.xlsx')
    data = np.array(dataframe1)
    data2 = np.array(dataframe2)
    m2 = len(data2)
    for i in range(m2):
        string = 'INSERT INTO dinner_Meals(name,link) VALUES ("{0}","{1}")'.format(data2[i][0],data2[i][1])
        mycrursor.execute(string) 
    m = len(data)
    for i in range(m):
      string = 'INSERT INTO dinner_food(dinner_id,food_id,percentage) VALUES ("{0}","{1}","{2}")'.format(data[i][0],data[i][1],data[i][2])
      mycrursor.execute(string)  

def add_lunch_Meals():
    dataframe2 = pd.read_excel('lunch_meals.xlsx')
    dataframe1 = pd.read_excel('lunch_food.xlsx')
    data = np.array(dataframe1)
    data2 = np.array(dataframe2)
    m2 = len(data2)
    for i in range(m2):
        string = 'INSERT INTO lunch_Meals(name,link) VALUES ("{0}","{1}")'.format(data2[i][0],data2[i][1])
        mycrursor.execute(string) 
    m = len(data)
    for i in range(m):
      string = 'INSERT INTO lunch_food(lunch_id,food_id,percentage) VALUES ("{0}","{1}","{2}")'.format(data[i][0],data[i][1],data[i][2])
      mycrursor.execute(string) 
     
def add_excersice():
    dataframe2 = pd.read_excel('exec.xlsx')
    data2 = np.array(dataframe2)
    m2 = len(data2)
    for i in range(m2):
        string = 'INSERT INTO exce(name,link) VALUES ("{0}","{1}")'.format(data2[i][1],data2[i][2])
        mycrursor.execute(string)

def add_snack():
    dataframe2 = pd.read_excel('snacks.xlsx')
    data2 = np.array(dataframe2)
    m2 = len(data2)
    for i in range(m2):
        string = 'INSERT INTO snack_food(snack_id) VALUES ("{0}")'.format(data2[i][0])
        mycrursor.execute(string)
#################################################function call to excute ######################################
# add_food_database()
# add_lunch_Meals()
# add_dinner_Meals()
# add_breakfast_Meals()
# add_excersice()
# add_snack()
###############################################################
def print_execrsices():
  mycrursor.execute("SELECT name from exce ")
  c = mycrursor.fetchall()
  return_menu = ""
  item = 0 
  for i in c :
     item+=1
     return_menu += "({}) ".format(item) + i[0] + "\n"
  return return_menu , item 
##################################################################
def get_id(username,password):
    a = mycrursor.execute("SELECT id from user where username = '"+str(username)+"'")
    c = mycrursor.fetchall() 
    if c:
        p = c[0][0]
        for i in c :
          d = mycrursor.execute("SELECT password from user where id = "+str(i[0]))
          dd = mycrursor.fetchall()[0][0]
          if dd == str(password) :
            return i[0]
    return -1


def create_user(username , email , weight , hieght , gender , age , activationrate , calories , goal,password , send_id):
   
    txt= "INSERT INTO user(username,email,weight,height, activation_rate , Age , gender , calories , goal,password , sender_id)  VALUES('"
    txt+=str(username)
    txt+="','"
    txt+=str(email)
    txt+="',"
    txt+=str(weight)
    txt+=","
    txt+=str(hieght)
    txt+=","
    txt+=str(activationrate)
    txt+=","
    txt+=str(age)
    txt+=",'"
    txt+=str(gender)
    txt+="',"
    txt+=str(calories)
    txt+=","
    txt+=str(goal)
    txt+=",'"
    txt+=str(password)
    txt+="','"
    txt+=str(send_id)
    txt+="')"
    print(txt)
    mycrursor.execute(txt)
    mydatabase.commit()
  
 
###### return weight of a user ######
def get_weight(id):
    a = mycrursor.execute("SELECT weight from user where Id = '"+str(id)+"'")
    p = mycrursor.fetchall()[0][0]
    return p


###### return calories of a user ######
def get_calories(id):
    a = mycrursor.execute("SELECT calories from user where Id = '"+str(id)+"'")
    p = mycrursor.fetchall()[0][0]
    return p


############################ update calories #######################
def update_colries(id):
  mycrursor.execute("SELECT gender,weight,height,Age,activation_rate from user where Id = '"+str(id)+"'")
  a = mycrursor.fetchall()
  if a[0][0] == 'men':
    bmr = 10*float(a[0][1]) # weight
    bmr+= (6.25*float(a[0][2])) # height
    bmr-= (5*float(a[0][3])) # age
    bmr+=5
    bmr = (bmr * float(a[0][4])) # activationRate
    bmr = int(bmr)
    mycrursor.execute("UPDATE user SET calories= '"+str(bmr)+"' WHERE Id = '"+str(id)+"'")
  else:
    bmr = (10*float(a[0][1])) # weight
    bmr+= (6.25*float(a[0][2])) # height
    bmr-= (5*float(a[0][3])) # age
    bmr-=161
    bmr = (bmr * float(a[0][4])) # activationRate
    bmr = int(bmr)
    mycrursor.execute("UPDATE user SET calories= '"+str(bmr)+"' WHERE Id = '"+str(id)+"'")
  mydatabase.commit()
  
#### return food by its id #######
def get_food(id):
   mycrursor.execute("SELECT * FROM food_item where id = '"+str(id)+"'")
   return mycrursor.fetchall()

##### return a breakfast meal randomly #####
def get_breakfast_meal():
  mycrursor.execute("SELECT * FROM Breakfast_Meals ORDER BY RAND() LIMIT 1")
  return mycrursor.fetchall()

##### return food id and percent by breakfast_id #####
def get_food_breakast_id(id):
  mycrursor.execute("SELECT food_id,percentage FROM breakfast_food where breakfast_id = '"+str(id)+"'")
  return mycrursor.fetchall()

##### return a dinner meal randomly #####
def get_dinner_meal():
  mycrursor.execute("SELECT * FROM dinner_Meals ORDER BY RAND() LIMIT 1")
  return mycrursor.fetchall()

##### return a snack meal randomly #####
def get_snack_meal():
  mycrursor.execute("SELECT * FROM snack_food ORDER BY RAND() LIMIT 1")
  return mycrursor.fetchall()

##### return food id and percent by dinner_id #####
def get_food_dinner_id(id):
  mycrursor.execute("SELECT food_id,percentage FROM dinner_food where dinner_id = '"+str(id)+"'")
  return mycrursor.fetchall()

##### return a lunch meal randomly #####
def get_lunch_meal():
  mycrursor.execute("SELECT * FROM lunch_Meals ORDER BY RAND() LIMIT 1")
  return mycrursor.fetchall()

##### return food id and percent by lunch_id #####
def get_food_lunch_id(id):
  mycrursor.execute("SELECT food_id,percentage FROM lunch_food where lunch_id = '"+str(id)+"'")
  return mycrursor.fetchall()

########## return goalweight of user ###########
def get_goalweight(id):
  st = "SELECT goal FROM user WHERE Id = "+str(id)
  mycrursor.execute(st)
  return mycrursor.fetchall()[0][0]

##### update weight for specific user ######
def update_weightt(id,weight):
  st = "UPDATE user SET weight= "+str(weight)+" WHERE Id = "+str(id)
  print(st)
  mycrursor.execute(st)
  mydatabase.commit()

##### update goal weight for specific user ######
def update_goalweightt(id,weight):
  mycrursor.execute("UPDATE user SET goal= '"+str(weight)+"' WHERE Id = '"+str(id)+"'")
  mydatabase.commit()
################### return exce link #####################
def get_exce_link(id):
  st = "SELECT link FROM exce WHERE Id = "+str(id)
  mycrursor.execute(st)
  return mycrursor.fetchall()[0][0]

#################### check #################################
def get_id_by_sender(send_id):
  st = "SELECT id FROM user WHERE sender_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     return res[0][0]
  else :
     return -1 
  
####################################################################
def check_take_breakfast(send_id):
  st = "SELECT * FROM breakfast_time WHERE send_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     res1 = res[0]
     if datetime.now() >= res1[2]:
        txt= "DELETE FROM breakfast_time WHERE send_id = " + str(send_id)
        mycrursor.execute(txt)
        mydatabase.commit()
        return -1 
     res1 = res1[len(res1)-2]   
     if res1 == 0  or res1==1:
        return res1
  else :
     return -1
    
################################################################
def add_breakfast_time(send_id , timestart , timeend , flag , break_id):
   use = check_take_breakfast(send_id) 
   if use == -1 :
      txt= "INSERT INTO breakfast_time(send_id , start_time, end_time , flag , break_id)  VALUES('"
      txt+=str(send_id)
      txt+="','"
      txt+=str(timestart)
      txt+="','"
      txt+=str(timeend)
      txt+="',"
      txt+=str(flag)
      txt+= ","
      txt+= str(break_id)
      txt+=")"
      print(txt)
      mycrursor.execute(txt)
      mydatabase.commit()
   elif use == 0 :
      st = "UPDATE breakfast_time SET start_time= '"+str(timestart)+"' WHERE send_id = "+str(send_id)
      mycrursor.execute(st)
      st = "UPDATE breakfast_time SET end_time= '"+str(timeend)+"' WHERE send_id = "+str(send_id)
      mycrursor.execute(st)
      mydatabase.commit()
   else :
      return -1
      
def get_last_breakfast(send_id):
  st = "SELECT break_id FROM breakfast_time WHERE send_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     return res 
  else:
     return 1 
  
def get_breakfast_time(send_id):
  st = "SELECT start_time FROM breakfast_time WHERE send_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     return res[0][0] 
  else:
     return 1  
  
############################################################################
def check_take_lunch(send_id):
  st = "SELECT * FROM lunch_time WHERE send_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     res1 = res[0]
     if datetime.now() >= res1[2]:
        txt= "DELETE FROM lunch_time WHERE send_id = " + str(send_id)
        mycrursor.execute(txt)
        mydatabase.commit()
        return -1 
     res1 = res1[len(res1)-2]   
     if res1 == 0 or res1==1:
        return res1 
  else :
     return -1
    
################################################################
def add_lunch_time(send_id , timestart , timeend , flag , lunch_id):
   use = check_take_lunch(send_id) 
   if use == -1 :
      txt= "INSERT INTO lunch_time(send_id , start_time, end_time , flag , lunch_id)  VALUES('"
      txt+=str(send_id)
      txt+="','"
      txt+=str(timestart)
      txt+="','"
      txt+=str(timeend)
      txt+="',"
      txt+=str(flag)
      txt+= ","
      txt+= str(lunch_id)
      txt+=")"
      print(txt)
      mycrursor.execute(txt)
      mydatabase.commit()
   elif use == 0 :
      st = "UPDATE lunch_time SET start_time= '"+str(timestart)+"' WHERE send_id = "+str(send_id)
      mycrursor.execute(st)
      st = "UPDATE lunch_time SET end_time= '"+str(timeend)+"' WHERE send_id = "+str(send_id)
      mycrursor.execute(st)
      mydatabase.commit()
   else :
      return -1
      
def get_last_lunch(send_id):
  st = "SELECT lunch_id FROM lunch_time WHERE send_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     return res 
  else:
     return 1
  
def get_lunch_time(send_id):
  st = "SELECT start_time FROM lunch_time WHERE send_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     return res[0][0] 
  else:
     return 1  
  
############################################################################
def check_take_dinner(send_id):
  st = "SELECT * FROM dinner_time WHERE send_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     res1 = res[0]
     if datetime.now() >= res1[2]:
        txt= "DELETE FROM dinner_time WHERE send_id = " + str(send_id)
        mycrursor.execute(txt)
        mydatabase.commit()
        return -1 
     res1 = res1[len(res1)-2]   
     if res1 == 0 or res1==1 :
        return res1 
  else :
     return -1
    
################################################################
def add_dinner_time(send_id , timestart , timeend , flag , dinner_id):
   use = check_take_dinner(send_id) 
   if use == -1 :
      txt= "INSERT INTO dinner_time(send_id , start_time, end_time , flag , dinner_id)  VALUES('"
      txt+=str(send_id)
      txt+="','"
      txt+=str(timestart)
      txt+="','"
      txt+=str(timeend)
      txt+="',"
      txt+=str(flag)
      txt+= ","
      txt+= str(dinner_id)
      txt+=")"
      print(txt)
      mycrursor.execute(txt)
      mydatabase.commit()
   elif use == 0 :
      st = "UPDATE dinner_time SET start_time= '"+str(timestart)+"' WHERE send_id = "+str(send_id)
      mycrursor.execute(st)
      st = "UPDATE dinner_time SET end_time= '"+str(timeend)+"' WHERE send_id = "+str(send_id)
      mycrursor.execute(st)
      mydatabase.commit()
   else :
      return -1
      
def get_last_dinner(send_id):
  st = "SELECT dinner_id FROM dinner_time WHERE send_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     return res 
  else:
     return 1
############################################################################
def check_take_snack(send_id):
  st = "SELECT * FROM snack_time WHERE send_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     res1 = res[0]
     if datetime.now() >= res1[2] and res1[len(res1)-2]==2: ##if u can take new snacks and you alredy took 2 snacks before 
        txt= "DELETE FROM snack_time WHERE send_id = " + str(send_id)
        mycrursor.execute(txt)
        mydatabase.commit()
        return -1 
     res1 = res1[len(res1)-2]   
     if res1 == 0 or res1==1:
        return res1 
  else :
     return -1
################################## snack ##############################################
def add_snack_time(send_id , timestart , timeend , flag , snack_id):
   use = check_take_snack(send_id) 
   if use == -1 :
      txt= "INSERT INTO snack_time(send_id , start_time, end_time , flag , snack_id)  VALUES('"
      txt+=str(send_id)
      txt+="','"
      txt+=str(timestart)
      txt+="','"
      txt+=str(timeend)
      txt+="',"
      txt+=str(flag)
      txt+= ","
      txt+= str(snack_id)
      txt+=")"
      print(txt)
      mycrursor.execute(txt)
      mydatabase.commit()
   elif use == 0 or use == 1 :
      st = "UPDATE snack_time SET start_time= '"+str(timestart)+"' WHERE send_id = "+str(send_id)
      mycrursor.execute(st)
      st = "UPDATE snack_time SET end_time= '"+str(timeend)+"' WHERE send_id = "+str(send_id)
      mycrursor.execute(st)
      mydatabase.commit()
   else :
      return -1 ########## can't take more snack !
      
def get_last_snack(send_id): #### to didn't take the same snack
  st = "SELECT snack_id FROM snack_time WHERE send_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     return res 
  else:
     return 1
  
def get_snack_time(send_id): ####### to know when will be the next snack 
  st = "SELECT start_time FROM snack_time WHERE send_id = "+str(send_id)
  mycrursor.execute(st)
  res = mycrursor.fetchall()
  if res :
     return res[0][0] 
  else:
     return 1  
  
mydatabase.commit()