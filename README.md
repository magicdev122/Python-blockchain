# Python React Blockchain Cryptocurrency

Blockchain & Cryptocurrency built using Python. The backend will consist of a Flask API, with a React frontend to display wallet information.

## Requirements

Dependencies are listed in the included requirements.txt file. Install all required dependencies by running this command:

```
pip install -r requirements.txt
```

## Starting Flask server

Run the python script command in terminal to start the Flask server

```
python -m backend.app
```

## Run a peer instance

Run the python script command in terminal to run a peer instance

(This is mainly used for testing. Allows you to create a peer instance and test blockchain updates)

```
export PEER=True && python -m backend.app
```

## Seed the backend with data

Run the python script command in terminal to seed transaction data

```
export SEED_DATA=True && python -m backend.app
```

## Run the frontend

Run the npm script command in terminal to start the frontend

```
npm run start
```

Navigate to http://localhost:3000/ to view the app

### Unit Tests

Unit tests are created using Pytest

1. Run backend tests using this command

```
python -m pytest backend/tests
```

## Built With

Backend

- Python 3.7
- Flask 1.1
- Pytest 5.4.1

Frontend

- React
- React BootStrap

## APIs Used

- PubNub - https://www.pubnub.com/

## Screenshots

![Coming Soon](https://upload.wikimedia.org/wikipedia/commons/8/80/Comingsoon.png "Coming Soon")
