from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv("testset.csv")
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
df.to_sql("my_table", engine,if_exists='replace')
data = engine.execute('SELECT * FROM my_table').fetchall()
data = pd.DataFrame(data)
print("Commit C")
