from mysql.connector import MySQLConnection
from mySqlDbConfig import readDbConfig


def insertGrade(firstName, lastName, province, grade):
    dbconfig = readDbConfig()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    sql = "INSERT INTO Grades (FName, LName, Province, Grade) VALUES (%s, %s, %s, %s)"
    values = (firstName, lastName, province, grade)
    cursor.execute(sql, values)
    # x = "SELECT * from Grades where FName = 'Hosna'"
    # cursor.execute(x)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
    conn.commit()
    print("Added to the table!!")


# insertGrade('Hosna', 'Kalantar', 'ON', 'A')


def deleteGrade(firstName, lastName, province, grade):
    dbconfig = readDbConfig()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    sql = "DELETE FROM grades where ( FName = %s AND LName = %s  AND Grade = %s AND Province = %s)"
    values = (firstName, lastName, province, grade)
    cursor.execute(sql, values)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
    print("Removed from the table!")


# deleteGrade('Francoise','Rautenstrauch','ON','E')


def displayGrade(firstName, lastName, province):
    dbconfig = readDbConfig()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    sql = "SELECT * from grades where (lName LIKE %s AND fName LIKE %s AND province LIKE %s)"
    values = (firstName, lastName, province)
    cursor.execute(sql, values)
    row = cursor.fetchone()
    while row is not None:
        print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(row[0], row[1], row[2], row[3]))
        row = cursor.fetchone()
        print("</table>")


# displayGrade('Hosna','Kalantar', 'ON')

while True:
    try:
        Option = int(input("choose an option: \n"
                           "1- Enter a grade \n"
                           "2- Display a grade \n"
                           "3-Delete a grade \n"
                           "4-EXIT \n"))
    except:
        print("Please choose an option!")
        break
    if Option == 1:
        first_name = input("Enter the first name> ")
        last_name = input("Enter the last name> ")
        pro_vince = input("Enter the province> ")
        gr_ade = input("Enter the grade> ")
        insertGrade(first_name, last_name, pro_vince, gr_ade)
        break
    elif Option == 2:
        first_name = input("Enter the first name> ")
        last_name = input("Enter the last name> ")
        pro_vince = input("Enter the province> ")
        displayGrade(first_name, last_name, pro_vince)
        break

    elif Option == 3:
        first_name = input("Enter the first name> ")
        last_name = input("Enter the last name> ")
        pro_vince = input("Enter the province> ")
        gr_ade = input("Enter the grade> ")
        deleteGrade(first_name, last_name, pro_vince, gr_ade)
        break

    elif Option == 4:
        print("SEE YOU LATER!")
        break
