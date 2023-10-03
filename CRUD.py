import csv
import pymysql
from prettytable import prettytable

# start the database connection
conn = pymysql.connect(host='localhost', user='root', password='', db='mydb')
cur = conn.cursor(pymysql.cursors.DictCursor)


def showData():
    try:
        # Define the SQL query to get data
        sql = "SELECT * FROM mytable"

        # Execute the SQL query
        cur.execute(sql)

        # Fetch all records
        records = cur.fetchall()

        if not records:
            print("No data found.")
            return

        # Create a PrettyTable for displaying the data
        t = prettytable.PrettyTable(records[0].keys())  # Use keys as column headers

        for record in records:
            t.add_row([record[key] for key in record.keys()])  # Extract values

        # Print the table
        print(t)
    except Exception as e:
        print(f"Error fetching data: {str(e)}")



def exportData():
    to_csv = showData()
    if to_csv:
        keys = to_csv[0].keys()
        file_path = 'users.csv'
        with open(file_path, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(to_csv)
        print(f"Data exported in {file_path}")
    else:
        print("No data to export")


def updateData():
    try:
        user_id = int(input("Enter id: "))
        user_name = input("Enter name: ")
        user_age = int(input("Enter age: "))

        sql = f"UPDATE `users` SET `name` = %s, `age` = %s WHERE `mytable`.`id` = %s"
        cur.execute(sql, (user_name, user_age, user_id))
        conn.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating data: {str(e)}")


def insertData():
    try:
        user_name = input("Enter name: ")
        user_age = int(input("Enter age: "))

        sql = f"INSERT INTO `mytable` (`id`, `name`, `age`) VALUES (NULL, %s, %s)"
        cur.execute(sql, (user_name, user_age))
        conn.commit()
        print("Insertion successful")
    except Exception as e:
        print(f"Error inserting data: {str(e)}")

def exportData():
    to_csv = showData()
    if to_csv:
        keys = to_csv[0].keys()
        file_path = 'users.csv'
        try:
            with open(file_path, 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(to_csv)
            print(f"Data exported in {file_path}")
        except Exception as e:
            print(f"Error exporting data: {str(e)}")
    else:
        print("No data to export")

def deleteData():
    try:
        user_id = int(input("Enter ID to delete record: "))
        sql = f"DELETE FROM mytable WHERE id = %s"
        cur.execute(sql, (user_id,))
        conn.commit()
        print("Deletion successful")
    except Exception as e:
        print(f"Error deleting data: {str(e)}")


# Add similar try-except blocks for deleteData and showData functions

option = None

while option != 0:
    print("\n================\n")
    print("1. Show Data")
    print("2. Delete data")
    print("3. Insert data")
    print("4. Update data")
    print("5. Export data")
    print("0. Exit")

    option = int(input("Choose Option: "))

    if option == 1:
        showData()

    if option == 2:
        deleteData()

    if option == 3:
        insertData()

    if option == 4:
        updateData()

    if option == 5:
        exportData()

    if option == 0:
        print("Thank you for using our software")
