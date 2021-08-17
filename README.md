# Winnipeg climate Backend

I am interested in looking at the climate in Winnipeg, so I used Python and MongoDB to build up the backend system.

## How to start this project?

Install the dependencies first.

```shell
pip3 install -r requirements.txt
```

And then run the following command in the root directory:

```shell
python3 main.py
```

The server will run on `http://0.0.0.0:8080`

## .env file

Don't forget to add the environment variable in the .env file.

```
MONGO_DETAILS=
```

## Data Source

https://winnipeg.weatherstats.ca/download.html

## TODO

Query from weatherstats directly and store in the database

## Stack

Python
MongoDB
FastAPI
