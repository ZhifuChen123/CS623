import psycopg2

# Function to execute SQL queries
def execute_query(query):
    connection = psycopg2.connect(
        host="localhost",
        database="cs623",
        user="steele",
        password="tor"
        )
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# Create the tables
def create_tables():
    create_product_query = """
        CREATE TABLE Product (
            "#prod" VARCHAR(10) PRIMARY KEY,
            name VARCHAR(50),
            quantity INTEGER
        );
    """
    execute_query(create_product_query)

    create_depot_query = """
        CREATE TABLE Depot (
            "#dep" VARCHAR(10) PRIMARY KEY,
            name VARCHAR(50),
            capacity INTEGER
        );
    """
    execute_query(create_depot_query)

    create_stock_query = """
        CREATE TABLE Stock (
            "#prod" VARCHAR(10) REFERENCES Product("#prod"),
            "#dep" VARCHAR(10) REFERENCES Depot("#dep"),
            quantity INTEGER,
            PRIMARY KEY ("#prod", "#dep")
        );
    """
    execute_query(create_stock_query)

# Execute the database creation
create_tables()