from fastapi import FastAPI,  HTTPException
import boto3
import csv

app = FastAPI()

bucket = 'test-files'
object_names = [
'test.csv'
]


s3 = boto3.client('s3')
for idx, elem in enumerate(object_names):
    if elem:
        object_name = elem
        file_name = 'test.csv'
        s3.download_file(bucket, object_name, file_name)

@app.get("/")
def main():
    return {
        "message": "Hello World!",
    }


@app.get("/{buff_name}")
def get_buff1(buff_name):
    print(buff_name) 
    if buff_name == 'error':
         raise HTTPException(status_code=404, detail="Buffer not found")
    this_buff_file_name = 'test.csv'
    print(this_buff_file_name) 

    out_data = []
    with open(this_buff_file_name, 'r') as data:  
        reader = csv.reader(data)
        header = None
        for row in reader:
            if not header:
                header = row
                continue
            print(row)
            this_row = {}
            for idx, col in enumerate(header):
                this_row[col] = row[idx]
            out_data.append(this_row)

    return  out_data

