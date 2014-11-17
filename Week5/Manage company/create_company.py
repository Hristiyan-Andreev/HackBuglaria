import sqlite3

db = sqlite3.connect("company_data")
cursor = db.cursor()
cursor.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER, \
                                                             yearly_bonus INTEGER, position TEXT)")
db.commit()

cursor = db.cursor()

id1 = 1
name1 = "Ivan Ivanov"
salary1 = 5000
bonus1 = 1000
position1 = "Software Developer"

id2 = 2
name2 = "Rado Rado"
salary2 = 500
bonus2 = 0
position2 = "Technical Support Intern"

id3 = 3
name3 = "Ivo Ivo"
salary3 = 10000
bonus3 = 10000
position3 = "CEO"

id4 = 4
name4 = "Petar Petrov"
salary4 = 3000
bonus4 = 1000
position4 = "Marketing Manager"

id5 = 5
name5 = "Maria Georgieva"
salary5 = 8000
bonus5 = 10000
position5 = "COO"

cursor.execute("INSERT INTO employees(id, name, monthly_salary, yearly_bonus, position) \
    VALUES(?,?,?,?,?)", (id1, name1, salary1, bonus1, position1))
cursor.execute("INSERT INTO employees(id, name, monthly_salary, yearly_bonus, position) \
    VALUES(?,?,?,?,?)", (id2, name2, salary2, bonus2, position2))
cursor.execute("INSERT INTO employees(id, name, monthly_salary, yearly_bonus, position) \
    VALUES(?,?,?,?,?)", (id3, name3, salary3, bonus3, position3))
cursor.execute("INSERT INTO employees(id, name, monthly_salary, yearly_bonus, position) \
    VALUES(?,?,?,?,?)", (id4, name4, salary4, bonus4, position4))
cursor.execute("INSERT INTO employees(id, name, monthly_salary, yearly_bonus, position) \
    VALUES(?,?,?,?,?)", (id5, name5, salary5, bonus5, position5))

db.commit()
