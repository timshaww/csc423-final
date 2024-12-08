import sqlite3

def create_database():
    conn = sqlite3.connect('pawsome_pets.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE Clinic (
        clinicNo INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT,
        telephone TEXT,
        managerStaffNo INTEGER UNIQUE,
        FOREIGN KEY (managerStaffNo) REFERENCES Staff(staffNo)
    )
    ''')

    cursor.execute('''
    CREATE TABLE Staff (
        staffNo INTEGER PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        address TEXT,
        telephone TEXT,
        DOB TEXT NOT NULL,
        position TEXT NOT NULL,
        salary REAL CHECK(salary > 0)
    )
    ''')

    cursor.execute('''
    CREATE TABLE Owner (
        ownerNo INTEGER PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        address TEXT,
        telephone TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE Pet (
        petNo INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        DOB TEXT NOT NULL,
        species TEXT NOT NULL,
        breed TEXT,
        color TEXT,
        ownerNo INTEGER NOT NULL,
        clinicNo INTEGER NOT NULL,
        FOREIGN KEY (ownerNo) REFERENCES Owner(ownerNo),
        FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    )
    ''')

    cursor.execute('''
    CREATE TABLE Examination (
        examNo INTEGER PRIMARY KEY,
        chiefComplaint TEXT NOT NULL,
        description TEXT,
        dateSeen TEXT NOT NULL,
        actionsTaken TEXT,
        petNo INTEGER NOT NULL,
        staffNo INTEGER NOT NULL,
        FOREIGN KEY (petNo) REFERENCES Pet(petNo),
        FOREIGN KEY (staffNo) REFERENCES Staff(staffNo)
    )
    ''')

    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect('pawsome_pets.db')
    cursor = conn.cursor()

    clinics = [
        (1, 'Vet Clinic', '123 Main St, Miami, FL', '305-123-4567', None),
        (2, 'Pet Care', '456 1st St, Miami, FL', '305-987-6543', None),
        (3, 'Animal Center', '789 2st St, Miami, FL', '305-123-1234', None),
        (4, 'Pet Clinic', '111 3rd St, Miami, FL', '305-987-9876', None),
        (5, 'Veterinary Hospital', '222 4th St, Miami, FL', '305-999-9999', None)
    ]

    cursor.executemany('INSERT INTO Clinic VALUES (?, ?, ?, ?, ?)', clinics)

    staff = [
        (101, 'Alice Johnson', '987 Oak St, Miami, FL', '305-111-2233', '1985-05-14', 'Veterinarian', 85000.00, 1),
        (102, 'Bob Smith', '321 Pine St, Miami, FL', '305-444-5566', '1978-11-23', 'Manager', 60000.00, 2),
        (103, 'Eve Adams', '654 Cedar St, Miami, FL', '305-777-8899', '1990-02-18', 'Vet Tech', 45000.00, 1),
        (104, 'Danielle Green', '123 Birch St, Miami, FL', '305-333-3333', '1982-04-10', 'Receptionist', 30000.00, 3),
        (105, 'Frank White', '456 Spruce St, Miami, FL', '305-888-8888', '1975-09-01', 'Veterinary Assistant', 35000.00, 4)
    ]
    cursor.executemany('INSERT INTO Staff VALUES (?, ?, ?, ?, ?, ?, ?, ?)', staff)

    owners = [
        (201, 'John', 'Doe', '890 Birch St, Miami, FL', '305-222-3333'),
        (202, 'Jane', 'Smith', '567 Maple St, Miami, FL', '305-555-6666'),
        (203, 'Sam', 'Taylor', '345 Pine St, Miami, FL', '305-444-1111'),
        (204, 'Emily', 'Brown', '678 Elm St, Miami, FL', '305-333-4444'),
        (205, 'Chris', 'Green', '789 Oak St, Miami, FL', '305-777-9999')
    ]
    cursor.executemany('INSERT INTO Owner VALUES (?, ?, ?, ?, ?)', owners)

    pets = [
        (301, 'Buddy', '2020-04-05', 'Dog', 'Golden Retriever', 'Golden', 201, 1),
        (302, 'Whiskers', '2018-09-15', 'Cat', 'Siamese', 'Gray', 202, 2),
        (303, 'Daisy', '2019-06-10', 'Dog', 'Labrador', 'Black', 203, 3),
        (304, 'Coco', '2021-02-11', 'Bird', 'Parrot', 'Green', 204, 4),
        (305, 'Max', '2017-07-07', 'Dog', 'Bulldog', 'Brown', 205, 5)
    ]
    cursor.executemany('INSERT INTO Pet VALUES (?, ?, ?, ?, ?, ?, ?, ?)', pets)

    examinations = [
        (401, 'Limping', 'Checked for injuries, X-ray taken', '2024-11-01', 'Prescribed medication', 301, 101),
        (402, 'Vomiting', 'Physical exam and blood tests', '2024-11-02', 'Dietary changes', 302, 103),
        (403, 'Coughing', 'Examined lungs, prescribed antibiotics', '2024-11-03', 'Antibiotics prescribed', 303, 104),
        (404, 'Feather loss', 'Skin exam, tested for mites', '2024-11-04', 'Mite treatment given', 304, 105),
        (405, 'Ear infection', 'Ear cleaning, drops administered', '2024-11-05', 'Medication prescribed', 305, 101)
    ]
    cursor.executemany('INSERT INTO Examination VALUES (?, ?, ?, ?, ?, ?, ?)', examinations)

    conn.commit()
    conn.close()


def print_all_data():
    conn = sqlite3.connect('pawsome_pets.db')
    cursor = conn.cursor()

    tables = ['Clinic', 'Staff', 'Owner', 'Pet', 'Examination']
    for table in tables:
        print(f"\n{table} Table:")
        cursor.execute(f'SELECT * FROM {table}')
        for row in cursor.fetchall():
            print(row)

    conn.close()


def execute_queries():
    conn = sqlite3.connect('pawsome_pets.db')
    cursor = conn.cursor()

    print("\nRegistering a new pet:")
    try:
        cursor.execute('''
        INSERT INTO PET (petNo, name, DOB, species, breed, color, ownerNo, clinicNo)
        VALUES (306, 'Buddy', '2024-10-06', 'Dog', 'Labrador Retriever', 'Black', 101, 10)
        ''')
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error registering pet: {e}")

    print("\nScheduling an examination:")
    try:
        cursor.execute('''
        INSERT INTO EXAMINATION (examNo, dateSeen, chiefComplaint, description, actionsTaken, petNo, staffNo)
        VALUES (406, '2024-11-24', 'Routine Checkup', 'Annual health checkup for Buddy', 'Vaccination and general examination', 1, 201)
        ''')
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error scheduling examination: {e}")

    print("\nUpdating clinic manager:")
    try:
        cursor.execute('''
        UPDATE CLINIC
        SET managerStaffNo = 202
        WHERE clinicNo = 10
        ''')
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error updating clinic manager: {e}")

    print("\nRetrieving examinations for pet 1:")
    cursor.execute('''
    SELECT *
    FROM EXAMINATION
    WHERE petNo = 1
    ''')
    print(cursor.fetchall())

    print("\nFinding pets registered at clinic 10:")
    cursor.execute('''
    SELECT *
    FROM PET
    WHERE clinicNo = 10
    ''')
    print(cursor.fetchall())

    conn.close()

if __name__ == '__main__':
    # 3A: Create the database schema.
    create_database()
    # 3B: Insert 5 tuples into each relation.
    insert_data()
    print('\nTables after tuples inserted:')
    print_all_data()

    # 3C: Develop 5 SQL queries from 2C.
    execute_queries()
    print('\nTables after queries executed:')
    print_all_data()
