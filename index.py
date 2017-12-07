## ../testproject

import os
import time

print(os.environ)
from skafossdk import * #DataEngine, DataSourceType

print(DataSourceType.Cassandra)

skafos = Skafos() #project_token = "83ec411086f4eb7cd168c6eb5f231299")
results = None



# schema =  {
# 			"table_name": "my_table",
# 		    "options": {
# 				"primary_key": [
# 					"column1", 
# 					"column3"
# 				],
# 				"order_by": [
# 					"column3 desc"
# 				]
# 			},
# 			"columns" : [
# 				{
# 					"column1": "varint"
# 				},
# 				{
# 					"column2": "varchar"
# 				},
# 				{
# 					"column3": "varchar"
# 				},
# 				{
# 					"column4": "varchar"
# 				}
# 			]
# 		}

# {
# 	"request_id": "9aceb461-6310-49cd-8dee-3fda78693a0e",
# 	"timestamp": 1511210750902,
# 	"ref_type": "save",
# 	"ref": {
# 		"schema": {
# 			"type": "cassandra",
# 			"table_name": "my_table",
# 		    "options": {
# 				"primary_key": [
# 					"column1", 
# 					"column3"
# 				],
# 				"order_by": [
# 					"column3 desc"
# 				]
# 			},
# 			"columns" : [
# 				{
# 					"column1": "data_type"
# 				},
# 				{
# 					"column2": "data_type"
# 				},
# 				{
# 					"column3": "data_type"
# 				},
# 				{
# 					"column4": "data_type"
# 				}
# 			]
# 		},
# 		"data": [
# 			["id1", "my", "data", "values"],
# 			["id2", "my", "other data", "values"]
# 		]
# 	}
# }
# data = [[1, "113", "123", "133"], [2, "213", "223", "233"]]



# def hello():
#     print("hello, world")
#     print(threading.current_thread())

# t = Timer(5.0, hello)
# t.start() 

# print("AFTER START")

# def delayed_func(self):
#     time.sleep(2.3)
#     print(threading.current_thread())
#     print(self)
#     return "hello"

# e = futurist.ThreadPoolExecutor()
# fut = e.submit(delayed_func, t)
# print(fut)
# print("BEFORE RESULT")
# print(fut.result())
# print("AFTER RESULT")
# e.shutdown()


# create = "create table target_creators"
# res = skafos.engine.create_view("target_creators", {"keyspace": "83ec411086f4eb7cd168c6eb5f231299", "table": "target_creators"}, DataSourceType.Cassandra)
# print("CREATED VIEW")
# print(res)
# print(res.result())




# result2 = None
res = skafos.engine.create_view("my_table", {"keyspace": "weather", "table": "weather_forecast"}, DataSourceType.Cassandra)
print("CREATED VIEW")
print(res.result())
results = skafos.engine.query("SELECT * from my_table LIMIT 5").result()
print("SELECTING FROM TABLE")
print(results)


# schema =  {
# 			"table_name": "my_weather_table",
# 		    "options": {
# 				"primary_key": [
# 					"column1", 
# 					"column3"
# 				],
# 				"order_by": [
# 					"column3 desc"
# 				]
# 			},
#             'columns': results['columns']

# 'columns': [{'date': 'date'}, {'date_fetched': 'timestamp'}, {'zipcode': 'string'}, {'source': 'string'}, {'cloud_cover': 'float'}, {'heat_index': 'float'}, {'humidity': 'float'}, {'latitude': 'float'}, {'longitude': 'float'}, {'precip_prob': 'float'}, {'precip_total': 'float'}, {'pressure': 'float'}, {'sunrise': 'timestamp'}, {'sunset': 'timestamp'}, {'tmax': 'float'}, {'tmin': 'float'}, {'wind_speed': 'float'}]}
# data = results['data']
# dataresult = skafos.engine.save(schema, data)
# print("GETTING DATA RESULT")
# print(dataresult)
# print(dataresult.result())

# query_string = "select * from target_creators"
# res1 = de.query(query_string, callback=t.handle_response)
# # res1 = de.query(query_string, lambda x: (
# #     print("{}".format(x)),
# #     print("INSIDE BLAH")),
# #     print(threading.current_thread())

# # )
# print("AFTER ASYNC QUERY 1")
# print(res1)


# result = de.query(query_string).result()
# print("INSIDE CLI")
# print(result)

# print("THE FIRST ASYNC QUERY RESULT= ")
# print(res1.result())

# print(t.outerresponse)
time.sleep(6)
print("PROGRAM TERMINATED")