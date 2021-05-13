import time
start = time.time()
import pandas as pd

from tableauhyperapi import HyperProcess, Connection, TableDefinition, SqlType, Telemetry, Inserter, CreateMode, TableName
from tableauhyperapi import escape_string_literal


PATH_TO_CSV = r'C:\Users\lokeshk\Desktop\HyperApplication\Dummy_data.csv'
PATH_TO_HYPER = r'C:\Users\lokeshk\Desktop\HyperApplication\Dummy_data.hyper'


my_df = pd.read_csv(PATH_TO_CSV)
#my_df['date'] = my_df['date'].apply(pd.to_datetime)  # only include this line if your CSV file has a date column named 'date'


# Step 1: Start Hyper instance
with HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
    #step 2: Start hyper process 
    with Connection(endpoint=hyper.endpoint, create_mode=CreateMode.CREATE_AND_REPLACE,database=PATH_TO_HYPER) as connection:
        print(connection.execute_scalar_query(query="SELECT'securing connections with endpoint!'"))
        
        
        #create table def with Table name 
        empdetails = TableDefinition(table_name= 
                                           TableName( 'Extract' , 'empdetails'),
                                           columns=[
                                               TableDefinition.Column('EMP_ID',SqlType.int()),
                                               TableDefinition.Column('EMP_NAME', SqlType.text()),
                                               TableDefinition.Column('MONTHY_SALARY', SqlType.int()),
                                               TableDefinition.Column('UNI_FLAG', SqlType.int())])
        
        #Create the table in the connection catalog
        connection.catalog.create_schema('Extract')
        connection.catalog.create_table(empdetails)
        
        
        print ('Validating the data...')
        cmd= f"COPY{empdetails.table_name} from {escape_string_literal(PATH_TO_CSV)}\
        with " "(format csv , NULL 'NULL', delimiter ',' , HEADER)"
        table_count = connection.execute_command(cmd)
        total_time = int((time.time()- start))
        total_time = "{:.2f}".format(total_time)
        print(f'Loaded all the {table_count} data in {total_time} seconds' )