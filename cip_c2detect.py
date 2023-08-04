import requests
from datetime import datetime
import time
import csv
import json
####
CriminalIP_API_KEY = "<paste_your_criminalip_api_key>"
####
now = datetime.now()
date = now.strftime("%Y-%m-%d")
file_name = rf"c2detect_{date}.csv"
query_file_name = "cip_c2detect_query.json"

with open(query_file_name, "r") as query_file:
    queries = json.load(query_file) #Loading queries stored in .json
    
scv_format = ["Target C2", "Query", "IP address", "detected port", "now status", "hostname", "tags"]

with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(scv_format)

ip_data = []
exists_flag = False
    
for query in queries["data"]: # Using queries sequentially for each C2
    for now_query in queries["data"][query]:
        print("Target C2 : " + query)
        print("useing query : " + now_query)
        payload={}
        params = {
            "query" : now_query,
            "offset" : 0
        }
        headers = {
            "x-api-key": CriminalIP_API_KEY
        }
        url = "https://api.criminalip.io/v1/banner/search"
        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        time.sleep(1)
        if response.json()["status"]==200:
            #since only 100 items can be extracted in one API call, adjusting the offset in increments of 100
            data = response.json()["data"]
            offset_count = int(data["count"]/100) +1
            
            for i in range (offset_count):  
                now_offset = i*100
                params = {
                    "query" :  now_query, 
                    "offset" : now_offset
                }

                response2 = requests.request("GET", url, headers=headers, data=payload, params=params)
                time.sleep(1)
                if response2.json()["status"]==200:
                    response2_data=response2.json()["data"]
                    
                    results2 = response2_data["result"]
                    for result in results2:
                        tmp_result = [str(query), str(now_query), result["ip_address"], str(result["open_port_no"]), str(result["status_code"]), str(result["hostname"])]
                        for tag in result["tags"]:
                            tmp_result.append(tag)
                        
                        if result["ip_address"] not in ip_data:
                            ip_data.append(result["ip_address"])
                            with open(file_name, 'a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow(tmp_result)
                                          
                else:
                    print("inner request failed!")
                    print(response2.json()["status"])
                    print(response2.json()["message"]) #something wrong in offset
        else:
            print("outer request failed!")
            print(response.json()["status"])
            print(response.json()["message"]) #something wrong in query or API payload

# sorting
with open(file_name, "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
column_to_sort = 0

sorted_data = sorted(data, key=lambda x: x[column_to_sort])

with open(file_name, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(sorted_data)

print("C2 detect finish")
print("save result as " +file_name)
