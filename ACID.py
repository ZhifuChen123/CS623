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

# Transaction 1: Delete product p1 from Product and Stock
def delete_product():
    product_id = "p1"

    # Delete from Stock table
    delete_stock_query = f"DELETE FROM Stock WHERE \"#prod\" = '{product_id}';"
    execute_query(delete_stock_query)

    # Delete from Product table
    delete_product_query = f"DELETE FROM Product WHERE \"#prod\" = '{product_id}';"
    execute_query(delete_product_query)

# Transaction 2: Delete depot d1 from Depot and Stock
def delete_depot():
    depot_id = "d1"

    # Delete from Stock table
    delete_stock_query = f"DELETE FROM Stock WHERE \"#dep\" = '{depot_id}';"
    execute_query(delete_stock_query)

    # Delete from Depot table
    delete_depot_query = f"DELETE FROM Depot WHERE \"#dep\" = '{depot_id}';"
    execute_query(delete_depot_query)

# Transaction 3: Change the name of product p1 to pp1 in Product and Stock
def change_product_name():
    product_id = "p1"
    new_name = "pp1"

    # Update Product table
    update_product_query = f"UPDATE Product SET name = '{new_name}' WHERE \"#prod\" = '{product_id}';"
    execute_query(update_product_query)

    # Update Stock table
    update_stock_query = f"UPDATE Stock SET \"#prod\" = '{new_name}' WHERE \"#prod\" = '{product_id}';"
    execute_query(update_stock_query)

# Transaction 4: Change the name of depot d1 to dd1 in Depot and Stock
def change_depot_name():
    depot_id = "d1"
    new_name = "dd1"

    # Update Depot table
    update_depot_query = f"UPDATE Depot SET name = '{new_name}' WHERE \"#dep\" = '{depot_id}';"
    execute_query(update_depot_query)

    # Update Stock table
    update_stock_query = f"UPDATE Stock SET \"#dep\" = '{new_name}' WHERE \"#dep\" = '{depot_id}';"
    execute_query(update_stock_query)

# Transaction 5: Add a new product (p100, cd, 5) to Product and (p100, d2, 50) to Stock
def add_new_product():
    product_id = "p100"
    product_name = "cd"
    product_quantity = 5
    depot_id = "d2"
    stock_quantity = 50

    # Insert into Product table
    insert_product_query = f"INSERT INTO Product (\"#prod\", name, quantity) VALUES ('{product_id}', '{product_name}', {product_quantity});"
    execute_query(insert_product_query)

    # Insert into Stock table
    insert_stock_query = f"INSERT INTO Stock (\"#prod\", \"#dep\", quantity) VALUES ('{product_id}', '{depot_id}', {stock_quantity});"
    execute_query(insert_stock_query)

# Transaction 6: Add a new depot (d100, Chicago, 100) to Depot and (p1, d100, 100) to Stock
def add_new_depot():
    depot_id = "d100"
    depot_name = "Chicago"
    depot_capacity = 100
    product_id = "p1"
    stock_quantity = 100

    # Insert into Depot table
    insert_depot_query = f"INSERT INTO Depot (\"#dep\", name, capacity) VALUES ('{depot_id}', '{depot_name}', {depot_capacity});"
    execute_query(insert_depot_query)

    # Insert into Stock table
    insert_stock_query = f"INSERT INTO Stock (\"#prod\", \"#dep\", quantity) VALUES ('{product_id}', '{depot_id}', {stock_quantity});"
    execute_query(insert_stock_query)

# Execute the transactions
delete_product()
delete_depot()
change_product_name()
change_depot_name()
add_new_product()
add_new_depot()
