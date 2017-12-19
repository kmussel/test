## myproj

import os


from skafossdk import *


print("BEFORE INIT")

skafos = Skafos()

print("12312 Begin Hello, world!")

res = skafos.engine.create_view("my_table", {"keyspace": "weather", "table": "weather_forecast"}, DataSourceType.Cassandra)
print("CREATED VIEW")
print(res.result())
results = skafos.engine.query("SELECT * from my_table LIMIT 5").result()
print("SELECTING FROM TABLE")
print(results)


print("ENV OF PROGRAM")
