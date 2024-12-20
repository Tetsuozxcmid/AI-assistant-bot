Overview
----------------------
Telegram bot using GigaChat API to generate responses to user requests. The aiogram library is used for the bot's operation, and the SQLite database is used for user <-> bot data storage.

  - History could be deleted from database with command
    ```python
      /clear
    ```
                            

### Installation
  ```python 
      python -m venv venv  #creating venv 
      venv/scripts/activate
      pip install -r requirements.txt  #installing packages
      create .env file with .env-example
        -> creating tg-bot with botfather
        -> creating gigachat token
        -> inserting with .env-example
      py main.py  #running app and creating db
      
  ```
  
    
----------------------

### Project Structure
```python
  main.py: main file with bot logic
```
```python
  config.py: Configuration module for reading environment variables such as tokens etc
```
```python
  requirements.txt: Project dependencies
```
```python
  .env-example:  .env file "create .env with the example and ur keys"
```
```python
  models.py: Database models
```
```python
  kb.py: Clear button for delete history
```

### Tech part
----------------------
Backend
  - <strong>Aiogram</strong>: It provides an asynchronous framework for interacting with the Telegram Bot
  - <strong>Aiohttp</strong>: Used to execute HTTP requests asynchronously. It is probably used to communicate with the GigaChat API
  - <strong>Aiosqlite</strong>: For working with SQLite databases in asynchronous mode. It is used to store bot data.
  - <strong>Httpx</strong>: Alternative library for executing HTTP requests that also supports asynchrony
    
Database
  - SQLite: Replaceable with any SQL-supported database
