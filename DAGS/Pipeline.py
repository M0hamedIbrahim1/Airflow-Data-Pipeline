from datetime import date, datetime
from airflow.models import DAG 
from pandas import DataFrame
from astro import sql as aql
from astro.files import File 
from astro.sql.table import Table

S3_FILE_PATH = "s3://orders-products/orders_data_header.csv"

@aql.transform
def filter_orders(input_table:Table):
    return "SELECT * FROM {{input_table}} WHERE amount >150"

@aql.transform
def join_orders_customers(filtered_orders_table: Table, customers_table: Table):
    return 
        """
            SELECT c.customer_id , customer_name , order_id, purchase_date, amount, type
            FROM {{ filtered_orders_table }} f JOIN {{ customers_table }} c 
            ON f.customer_id = c.customer_id
        """


with DAG(
    dag_id='astro_orders',
    start_date=datetime(2023, 11, 7),
    schedule='@daily',
    catchup=False
):
orders_data = aql.load_file(
input_file = File(
                path = S3_FILE_PATH + "/orders_data_header.csv", 
                conn_id=S3_CONN_ID
                output_table = Table(conn_id=SNOWFLAKE_CONN_ID)
                )
)
    
customer_table = Table(
    name="customers_table",
    conn_id=SNOWFLAKE_CONN_ID,
)  
    

joined_data = join_orders_customers(filter_orders(orders_data), customer_table)

reporting_table = aql.merge(
    target_table=Table(
        name="reporting_table",
        conn_id=SNOWFLAKE_CONN_ID,
    ),
    source_table=joined_data,
    target_conflict_columns=["order_id"],
    if_conflicts="update",
    columns=["customer_id", "customer_name"],
)

