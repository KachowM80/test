import sqlite3

#constants and variables
DATABASE = 'fighter.db'


#functions
def print_all_aircraft():
    '''print all them tuffly'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter;"
    cursor.execute(sql)
    result = cursor.fetchall()
    #loop
    for fighter in result:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop done
    db.close()


#main code
print_all_aircraft()
