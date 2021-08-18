# Winnipeg climate Backend

I am interested in looking at the climate in Winnipeg, so I used Python and MongoDB to build up the backend system.

![](https://i.imgur.com/7ZD0bsG.png)

## How to start this project?

Install the dependencies first.

```shell
pip3 install -r requirements.txt
```

And then run the following command in the root directory:

```shell
uvicorn main:app --port 8080 --host 0.0.0.0 --reload
```

The server will run on `http://0.0.0.0:8080`, and the documentation is available in `http://0.0.0.0:8080/docs`

## FAQ

If you cannot open `http://0.0.0.0:8080`, please open `localhost:8080`.

## .env file

Don't forget to add the environment variable in the .env file.

```
MONGO_DETAILS=
```

## Data Source

https://winnipeg.weatherstats.ca/download.html

## Deployment

Deploy to [Deta](https://deta.sh)

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy)

## TODO

- Query from weatherstats directly and store in the database
- Add Security Token

## Stack

Python
MongoDB
FastAPI
