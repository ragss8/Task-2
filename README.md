#Task-2
method 1:Here we create a db, read data from the file and create each row of the CSV as record(document) in the db(say a MongoDB on the desktop or the MongoDB[Atlas]).


method 2:we read data from the python file by using the post method of the fastapi to upload the file and when uploaded the file is stored on mongodb as jsonable content , so inorder to check uniqueness of the uploaded file we use hashlib and Path to read the contents from the file uploaded and over that we also check the uniqueness of the data contents in the file so that no same existing document/data is uploaded.

