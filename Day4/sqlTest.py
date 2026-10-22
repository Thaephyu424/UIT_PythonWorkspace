import pymysql

def db_connection():
    print("Attempting PyMySQL connection...")
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="demo",
            port=3306,
            connect_timeout=5
        )
        print("Connection Successful.")
        return conn
    except Exception as e:
        print("Connection failed :", e)
        return None

# Establish connection safely
conn = db_connection()

if conn is not None:
    cursor = conn.cursor()

    # Fixed: Make option() return the choice
    def option():
        return input(
            "Enter 1 for insert\n"
            "Enter 2 for select\n"
            "Enter 3 for update\n"
            "Enter 4 for delete\n"
            "Your choice: "
        )

    def select():
        sql = """SELECT * FROM doctor"""
        cursor.execute(sql)
        results = cursor.fetchall()
        
        print("\n--- Selected successfully ---")
        for row in results:
            print(row)
        print("-----------------------------\n")

    def insert():
        sql = """INSERT INTO doctor(name, specialization, contact_number, salary) VALUES (%s, %s, %s, %s)"""

        name = input("Enter your name: ")
        specialization = input("Enter your specialization: ")
        contact_number = input("Enter your contact number: ")
        salary = input("Enter your salary: ")

        values = (name, specialization, contact_number, salary)
        cursor.execute(sql, values)
        conn.commit()

        print("\n[Success] Record inserted successfully!\n")

    def update(): 
     
        name = input("Enter name that you want to update .")
        print("This is menu for thae you want to update column\n" \
        "1 for name\n" \
        "2 for specialization\n" \
        "4 for salary\n" \
        "3 for contact number\n")
        updateColumn = input("Enter column name that you want to update")
        column_map={
            "1":"name",
            "2":"specialization",
            "3":"contact_number",
            "4":"salary"
        }
        columnName = column_map[updateColumn]
        updateValue = input(f"Enter value for {columnName} that you want to update")
        sql=f"UPDATE doctor SET {columnName}= %s WHERE name = %s"
        values=(updateValue,name)
        cursor.execute(sql, values)
        conn.commit()
        print("\n [Success]Record Updated Successfully\n")

    def delete():
        name = input("Enter name that you want to delete::")
        sql = "DELETE FROM doctor WHERE name = %s"
        values = (name)
        cursor.execute(sql,values)
        conn.commit()
        print("\n [Success] Record Deleted Successfully\n")

    # --- Main Loop ---
    while True:
        choice = option()  # Capture the returned choice from the function
        
        if choice == "1":
            insert()
        elif choice == "2":
            select()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        else:
            print("\n[Invalid choice] Please enter 1, 2, 3, or 4.\n")
        
        text = input("Do you want to end program? (yes/no): ").strip().lower()
        if text == "yes":
            break

    # Clean up
    cursor.close()
    conn.close()
    print("Program ended and database connection closed.")

else:
    print("Cannot run program because database connection failed.")