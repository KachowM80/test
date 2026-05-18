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
    print(f"name                          speed    max_g climb range payload")
    for fighter in result:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop done
    db.close()


#main code
while True:
    user_input = input(
"""
What would you like to do.
1. Print all aircraft
2. Print all aircraft sorted by speed
7. Exit
""")
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        print_all_aircraft_by_speed()
    elif user_input == "3":
        print_all_aircraft_by_climb()
    elif user_input == "4":
        print_all_aircraft_by_range()
    elif user_input == "5":
        print_all_aircraft_by_climb()
    elif user_input == "6":
        print_all_aircraft_by_payload()
    elif user_input == "7":
        break
    else:
        print('That was not an option\n')