import sqlite3  

conn = sqlite3.connect('wordle.db')     # variable = lang.func('name of databse') #connects to db #db creation

#db creation above

#table creation below

c = conn.cursor                            # cursor variable = connectoing and making cursor vairbale, # create a cursor

c.execute(""" CREATE TABLE wordle_list  (               

        word_list test                                   
""")                               #cursor command   #multiple ' for lines readibility , #column name and datatype


conn.commit()            # commit the command

conn.close()     #not neccesary but best practice,  # close ur connection

