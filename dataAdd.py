import psycopg2

def main():
    try:
        # Connect to the database
        conn = psycopg2.connect(
            host="localhost",
            database="cs623",
            user="steele",
            password="tor"
        )

        # For atomicity
        conn.autocommit = False

        # For isolation
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE)

        cursor = conn.cursor()

        # Delete rows with "p1" as #prod from Stock table
        # Must be done first to satisfy foreign key constraint on Stock table (for consistency)
        cursor.execute("DELETE FROM Stock WHERE \"#prod\" = 'p1';")

        # Delete row with "p1" as #prod from Product table
        cursor.execute("DELETE FROM Product WHERE \"#prod\" = 'p1';")

        # Insert data into Product table
        cursor.execute("INSERT INTO Product (\"#prod\", name, quantity) VALUES ('p1', 'tape', 2.5);")
        cursor.execute("INSERT INTO Product (\"#prod\", name, quantity) VALUES ('p2', 'tv', 250);")
        cursor.execute("INSERT INTO Product (\"#prod\", name, quantity) VALUES ('p3', 'vcr', 80);")

        # Insert data into Depot table
        cursor.execute("INSERT INTO Depot (\"#dep\", name, capacity) VALUES ('d1', 'New York', 9000);")
        cursor.execute("INSERT INTO Depot (\"#dep\", name, capacity) VALUES ('d2', 'Syracuse', 6000);")
        cursor.execute("INSERT INTO Depot (\"#dep\", name, capacity) VALUES ('d4', 'New York', 2000);")

        # Insert data into Stock table
        cursor.execute("INSERT INTO Stock (\"#prod\", \"#dep\", quantity) VALUES ('p1', 'd1', 1000);")
        cursor.execute("INSERT INTO Stock (\"#prod\", \"#dep\", quantity) VALUES ('p1', 'd2', -100);")
        cursor.execute("INSERT INTO Stock (\"#prod\", \"#dep\", quantity) VALUES ('p1', 'd4', 1200);")
        cursor.execute("INSERT INTO Stock (\"#prod\", \"#dep\", quantity) VALUES ('p3', 'd1', 3000);")
        cursor.execute("INSERT INTO Stock (\"#prod\", \"#dep\", quantity) VALUES ('p3', 'd4', 2000);")
        cursor.execute("INSERT INTO Stock (\"#prod\", \"#dep\", quantity) VALUES ('p2', 'd4', 1500);")
        cursor.execute("INSERT INTO Stock (\"#prod\", \"#dep\", quantity) VALUES ('p2', 'd1', -400);")
        cursor.execute("INSERT INTO Stock (\"#prod\", \"#dep\", quantity) VALUES ('p2', 'd2', 2000);")

        conn.commit()  # For atomicity

    except psycopg2.DatabaseError as e:
        print("An error occurred:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
