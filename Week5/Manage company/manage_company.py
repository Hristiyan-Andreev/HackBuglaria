import sqlite3


def list_employees(db):
    cursor = db.cursor()
    result = cursor.execute("SELECT name,position FROM employees")

    for row in result:
        print("{} - {}".format(row["name"], row["position"]))


def monthly_spending(db):
    cursor = db.cursor()
    result = cursor.execute("SELECT SUM(monthly_salary) as sum FROM employees").fetchone()
    print("Monthly spendings: %d" % (result['sum'],))


def yearly_spending(db):
    cursor = db.cursor()
    result = cursor.execute("SELECT SUM(monthly_salary) as sum FROM employees").fetchone()
    result2 = cursor.execute("SELECT SUM(yearly_bonus) as sum FROM employees").fetchone()
    print("Annual spendings: %d" % (result['sum'] * 12 + result2['sum'],))


def add_employee(db):
    cursor = db.cursor()
    name = input("Enter name: ")
    monthly_salary = input("Enter salary: ")
    yearly_bonus = input("Enter yearly bonus: ")
    position = input("Enter position: ")
    someid = 0

    cursor.execute("INSERT INTO employees(id, name, monthly_salary, yearly_bonus, position) \
    VALUES(?,?,?,?,?)", (someid, name, monthly_salary, yearly_bonus, position))

    db.commit()


def delete_employee(db):
    cursor = db.cursor()
    delete_id = input("Who do you want to delete? ")
    cursor.execute("DELETE FROM employees WHERE id = ?", (delete_id))
    deleted = cursor.execute("SELECT name FROM employees WHERE id = ?", (delete_id)).fetchone()
    db.commit()
    print(deleted + "was removed")


def main():
    db = sqlite3.connect("company_data")
    db.row_factory = sqlite3.Row

    while True:
        print("Available commands:\n 1) List employees\n2) List monthly spendings\
        \n3) List yearly spending\n4) add_employee\n5) Exit")
        while True:
            command = int(input("Enter a command: "))
            if 1 <= command <= 7:
                break

            if command == 1:
                list_employees(db)
            elif command == 2:
                monthly_spending(db)
            elif command == 3:
                yearly_spending(db),
            '4': add_employee(db),
            '5': delete_employee(db)
            }
        result[command]

if __name__ == '__main__':
    main()
