from fastapi import FastAPI, File, UploadFile
import requests
import pymongo
import csv
import hashlib
from pathlib import Path



app=FastAPI()

client = pymongo.MongoClient("mongodb+srv://raghugaikwad8641:Raghugaikwad8@cluster0.awyei4w.mongodb.net/?retryWrites=true&w=majority")
db=client["sales_info"]
collection=db["req_data"]

@app.get("/")
def read_root():
    return {"Hello": "World"}

unique_filenames = set()
unique_hashes = set()

@app.post("/uploadfile/")
async def upload_file(file:UploadFile=File(...)):
    filename = Path(file.filename).name
    if filename in unique_filenames:
        return {
            "message":f"File '{filename}' has already been uploaded."
        }
    contents=await file.read()
    file_hash=hashlib.sha256(contents).hexdigest()
    if file_hash in unique_hashes:
        return{
            "message":"file with identical contents are existing."
        }
    lines=contents.decode().splitlines()
    reader=csv.DictReader(lines)
    rows=[]
    for row in reader:
        rows.append(row)
    result=collection.insert_many(rows)
    print(result)
    unique_filenames.add(filename)
    unique_hashes.add(file_hash)
    return {"message": f"{result.inserted_ids} rows inserted."}
    #return "success"
    """ return{"inserted_ids":result.inserted_ids} """


""" def main():
    filename="sales_report.csv"
    url="http://localhost:8000/uploadfile"
    files={"file":open(filename,"rb")}
    response=requests.post(url,files=files)
    print(response) """




""" import pymongo
import pandas as pd
import csv
client = pymongo.MongoClient("mongodb+srv://raghugaikwad8641:Raghugaikwad8@cluster0.awyei4w.mongodb.net/?retryWrites=true&w=majority")
df =pd.read_csv("sales_report.csv")
data=df.to_dict(orient="records")
print(data)
db=client["sales_report"]
print(db)
db.sales_info.insert_many(data) """

