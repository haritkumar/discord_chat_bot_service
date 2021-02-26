# discord chat bot service
This service recives messeges sent on channels and process them as bot user's response.

## Install discord lib
```sh
python3 -m pip install -U discord.py
```

## Run program
```sh
python3 main.py
```

## DB to persist search history
We are using mysql for persistence. We can use other as well like Mongo, Elastic search for good read ops

- DB Name `discord_bot`

- Note: Use Python 3.7