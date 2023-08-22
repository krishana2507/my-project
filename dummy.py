import psycopg2

# Connection details
dbname = "postgres"
user = "krishna"
password = "shalu@25"
host = "pg-managed.postgres.database.azure.com"
port = "5432"  # Default PostgreSQL port

# Read the YAML content from the file
with open("petstore.yaml", "r") as yaml_file:
    yaml_content = yaml_file.read()
    print(type(yaml_content))
    # print(yaml_content)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

# Create a cursor
cur = conn.cursor()


# Define the table name
table_name = "yaml_spec"
# to crete table 
cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id serial PRIMARY KEY, yaml_content text);")
# Insert the YAML content into the table
cur.execute(f"INSERT INTO {table_name} (yaml_content) VALUES (%s)",(yaml_content,))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
