from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy import inspect

import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')
#con = engine.connect()
#table_names = engine.table_names()
#print(table_names)

inspector = inspect(engine)
print(inspector.get_table_names())
