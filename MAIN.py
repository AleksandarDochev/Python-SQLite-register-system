import sqlite3
# importing sql lite
##########################################################################################
connection = sqlite3.connect('MAIN_DATABASE.db')
# Създавам връзката и самата sql базаданни на име ('database name here.db')
# И създавам самия database файл 'MAIN_DATABASE.db ,
# Който естествено се появява в ляво (полето на проекта)
##########################################################################################
cursor = connection.cursor()
# прави се курсор с който ще  оперира в базата данни
# ще се правят таблици ,update на info , etc.
##########################################################################################
def USER_CHECK():
  # password_SQL_check()
  Username_input = input("ENTER Your Username:")
  #Юзера въвежда Username стойността която ще се сравни в SQL базата данни
  sql_SELECT= '''SELECT * FROM test WHERE Username=?'''
  #активира се командата в  sql която SELECTWA всички стоности в таблицата test
  #колоната Username има не определена от нас все още стоиност "=?"

  sql_SELECT_com_with_user_input = cursor.execute(sql_SELECT, (Username_input,))
  # Тук добавяме командата select , не определената  от нас стоиност като "Username_input"
  #като казваме на курсора да го използва в инпута
  #ДАвм това име на този ред "sql_SELECT_com_with_user_input"

  for row_from_SQL in sql_SELECT_com_with_user_input:
      #за реда които се връща от командата "sql_SELECT_com_with_user_input"
      #на когото сме дали име "row_from_SQL"
      User_x_sql = (row_from_SQL[len(row_from_SQL) - 8])    #взимаме осмия елемент от края към началото
      PASS_X = (row_from_SQL[len(row_from_SQL) - 3])        #взимаме третия елемент от края към началото
      #взимаме стойността от резултата на осмото мясти броено отзад напред в стринга и го наричаме "x"
      #така всеки път изтеглената информация от колоната едно на изтегления ред от таблицата test проверен

      print("HELLO user", User_x_sql)
      #Правим проверка на стойността от sql за да разберем точно как изглежда за Юзера
      if User_x_sql == Username_input:    #тук вече сравнявам стоиноста на юзера с sql резултата
          print("This Username exists!")
                        # И следователно се връщаме вече към съществената функция
      Password_input = input("Your Password here:")
      if PASS_X == Password_input:        #сраявняваме зададената по рано парола от юзера с третя елемент от
          print("Correct")                #края към началото на "row_from_SQL"

          # ТУК ИДВА ЛОГИН МЕНЮТО НА ЮЗЕРА

      elif PASS_X != Password_input:
          print("WRONG PASSWORD")
          USER_CHECK()
  # password_SQL_check()

def creating_TABLE():

    cursor.execute ('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT,' 
                    #"CREATE TABLE IF NOT EXISTS " e sqlite команда за създаване на таблица 
                    #АКО не съществува таблица с такова име вече
                    'Username TEXT, Name text, Surname text, Age real, Email text,'
                    'Password BLOB, Secret_q text , Secret_a text)')
    #ИЗполвама курсора за да направя таблица на име test с всички колони дадени по условие
    # Като всеки рес има уникално id  за разпознаване наречени INTEGER PRIMARY KEY
    #колоната с това ид съм го къстил просто "id"
    #всяко id има Username/Name/Surname/Age/Email/Password/Secret_q/Secret_a/Numoflogins
    #като всичките за text type данни без Age, Password & numoflogins
    #REAL - се използва за числа
    #TEXT - се използва за текст
    #BLOB - за text+числа
    #connection.commit()
    #datatest_massive = ('ADMIN', 'Alexander','Dochev','22','aleks@abv.bg','ehbe','koi e?','Toi e ')
    #sql = '''INSERT INTO test (Username, Name,Surname,Age,Email,Password,Secret_q,Secret_a)
    #                   VALUES (    ?   ,   ? ,   ?   , ? , ?   ,     ?  , ?      ,     ?  )
    #      '''
    # siwkow prai sql Integer s tezi vazmmojnosti
    # (first_name, last_name) са имената на колоните кадето ше отидат данните
    # VALUES(?,?)  са самите места на данните които ше се въведът

    #cursor.execute(sql, datatest_massive)  # Sivkow zwikwa sql i slaga test massiva ''test = ('John', 'Doe')'' koito  e po gore
    #connection.commit()  # Създава и вкарва информацията от него в  VALUES(?,?)
    #IPORTIRAM пробни данни

    #cursor.execute(
     #              'INSERT INTO test (  Username , Name , Surname , Age , Email , Password , Secret_q , Secret_a ,) ',
      #             'VALUES           (  "SAT2  , "azi"  , "purd"  , "1"  , "кuz@abv.bg"  , "23" , "a"  , "e"  )'
       #            )
    # IPORTIRAM probni danni
    #connection.commit()
    #за да могат промените в базата данни да се запаметят
############################################################################################


creating_TABLE()

############################################################################################
def LOGIN_MENU():
    Usernames_massive = []
    print("----------------------LOGIN MENU----------------------\n", "Choose one of the following options: ")
    # Текста за заглавието на менюто
    LoginMenuINPUT = input("1.Enter your username & passowrd\n2.Return to MAIN MENU\nYour option:")
    # обявявам името на inputa като LoginMenuINPUT
    LoginMenuINPUT = int(LoginMenuINPUT)
    # а тук обявявам въведената стойност от потребителя да се възприема като число с int
    if LoginMenuINPUT == 1:
        USER_CHECK()
    elif LoginMenuINPUT == 2:
        print("You choose to Return to MAIN MENU")
        MAIN_MENU()
    elif LoginMenuINPUT > 2:
        print("PLEASE Choose a valid Option!\n\n")
        # използвайки IF-ELSE лазвам да се инпутнат опция 1 или 2
        LOGIN_MENU()
        # Това LOGIN_MENU() го слагам за да може след въвеждане на НЕ желаната стойност да се извика
        # цялата дефиниция отново
########################################################################

def REGISTRATION_MENU():
    print("----------------------REGISTRATION MENU----------------------\n")
    print("Start entering your info")
    Username_input = input("Pick a Username:")
    print("Username:", Username_input)
    global Name_Input
    global Surname_input           #
    global Age_input                #   Всичко това се прави global само зада може да излезе от REG_AFTERPASS
    global Email_input              #   И да може да се използва в
    global Secret_q_input           # cursor.execute("INSERT INTO test VALUES и T.N.
    global Secret_a_input
    global Password_input_2

    def REG_AFTERPASS():
        global Name_Input
        Name_Input = input("Name:")
        print("Username:",Username_input , "Name:",Name_Input,)
        global Surname_input
        Surname_input = input("Surname:")
        print("Username:", Username_input, "Name:", Name_Input,"Surname:",Surname_input )
        global Age_input
        Age_input = input("Age:")
        Age_input = int(Age_input)
        print("Username:", Username_input, "Name:", Name_Input, "Surname:", Surname_input,"Age:",Age_input,)
        global Email_input
        Email_input =input("Email:")
        print("Username:", Username_input, "Name:", Name_Input, "Surname:", Surname_input, "Age:", Age_input,
                "Email:",Email_input)
        global Secret_q_input
        Secret_q_input = input("Your secret question:")
        print("Username:", Username_input, "Name:", Name_Input, "Surname:", Surname_input, "Age:", Age_input,
              "Email:", Email_input,"Secret_q:",Secret_q_input)
        global Secret_a_input
        Secret_a_input = input("Your secret answer:")
        print("Username:", Username_input, "Name:", Name_Input, "Surname:", Surname_input, "Age:", Age_input,
              "Email:", Email_input, "Secret_q:", Secret_q_input,"Secret_a:",Secret_a_input)

    def Password():
        global Password_input_2
        Password_input_1 = input("Your Password:")    #въвеждане на 1вата парола
        Password_input_2 = input("Please retype your Password:")  #пише я пак
        if Password_input_2 == Password_input_1:                    #Ако вторият път e = на първия отиваме н reg_afterpass
            print("Your passwords Match,please continue!")
            REG_AFTERPASS()
        elif Password_input_2 != Password_input_1:                  #ako 2-ri pass ne e rawen na 1 izwikwame
            print("YOUR PASS DOESN'T MATCH")                        #Функцията трябва да започне наново
            Password()
    Password() #викам си функцията да започне доло защото парво трябва да я има

    REG_input_data_massive = (Username_input,Name_Input,Surname_input,Age_input,Email_input,Password_input_2,Secret_q_input,Secret_a_input)
    sql_REG_input_command = '''INSERT INTO test (Username, Name,Surname,Age,Email,Password,Secret_q,Secret_a)
                                         VALUES (    ?   ,   ? ,   ?   , ? , ?   ,     ?  , ?      ,     ?  )             
                            '''
    cursor.execute(sql_REG_input_command,REG_input_data_massive)
    connection.commit()
    print("\n\nThank you for registration1\n\n")
    MAIN_MENU()
########################################################################



########################################################################
def MAIN_MENU():
#ТОВА E MENU функцията за цялото начало (първо се прави тя , за да може  да се извика)
#ЕСтествено трява да съшествува за да се извика
   print("----------------------MAIN MENU----------------------\n", "Choose one of the following options: ")
   #Тексата за загалвието
   MainMenuINPUT = input("1.Login\n2.Register\nYour option:")
   #Обявявам името на инпута като MainMenuINPUT и дава, текс като опция
   MainMenuINPUT = int(MainMenuINPUT)
   #а тук обявявам вуведената стойност от потребителя да се възприема като число с int
   if MainMenuINPUT == 1:
        print("You choose to Login")
        LOGIN_MENU()
   elif MainMenuINPUT == 2:
        print ("You choose to Register")
        REGISTRATION_MENU()
   elif MainMenuINPUT > 2:
        print("PLEASE Choose a valid Option!\n\n")
        #използвайки IF-ELSE казвам да се инпутнат опция 1 или 2
        MAIN_MENU()
   elif MainMenuINPUT == str:
        print("PLEASE Choose a valid Option!\n\n")
        # тук IF-ELSE казва да се инпутнат опций които ако не са числа да връща в началото
        MAIN_MENU()
        #Това MAIN_MENU() го слагам за да може след въвеждане на НЕ желаната стойност да се извика
        #цялата дефиниция отново
################################################################################

MAIN_MENU()
#Това е за да почне програмата  .всичко се създава предварително за да може да се извика
#
#CURSOR EXECUTE za INSERTA  127 RED
##CURSOR EXECUTE za EXistence  64 RED