# Technical-assessment-backend

Extract information from a pdf, the application makes use of OCR recognition to extract the information from the pdf that is uploaded to the server, this application was built with pytesseract as a library to extract the information from the pdf. pytesseract returns the text to which we subsequently filter the information we need through Regular Expressions, the information to be extracted from the pdf is as follows.

* Vendor Name
* Fiscal Number
* Contract Number
* Start Date
* End Date
* Comments paragraph

After extracting the information, it is saved in the database in a table called extractions.

This project makes use of the following libraries to extract and filter the information that you want to obtain.

* [pdf2image 1.16.0](https://pypi.org/project/pdf2image/)
convert pdf to image
* [pytesseract 0.3.7](https://www.postgresql.org/)
receives an image and returns the text that is recognized in the image.
* [re](https://docs.python.org/3/library/re.html)
It is used for handling regular expressions in python, it was used to extract the desired information from the text that pytesseract returns.

## Technologies
* [Python](https://www.python.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)
* [FastApi](https://fastapi.tiangolo.com/)
* [SQLAlchemy ORM](https://www.sqlalchemy.org/)

## Installation

### Requirements
* docker
* docker-compose
* git

```bash
docker-compose -f docker/docker-compose.yml up --build -d
```
it may be required to run the command twice to avoid errors. (It is possible that the database container takes a while to start and the app container, unable to connect to the database, terminates its execution)

## Usage
To see the API documentation you must copy the following link and paste it into your browser:
http://localhost:8081/docs

In that link we can see all the endpoints that have the API enabled, we will see something like this:

<img src="https://github.com/felipevargas-bz/felipevargas-bz/blob/main/example-pdf-app.png" border="0" alt="aguila-imagen-animada-0035" />


```
/db_data
```
It returns all the data of a table passed as an argument, in v0.1.0 it returns all the information extractions that have been generated by means of pdfs uploaded to the server.

```
/extract
```
It extracts the data from the pdf whose path was passed as a parameter, then calls the create function to store that data in the database.

```
/upload-pdf
```
Save the file passed in the Body in the container that is running the application, in the path /usr/src/app/files/pdf.

```
/paths
```
Get all the paths of the uploaded documents, if and only if file_name == None, otherwise get the path of the file whose name is the value of file_name.

```
/delete-file
```
Deletes a document stored on the server by name.

### Authors :black_nib:
* __Felipe Vargas, felipevargas.bz@gmail.com__
