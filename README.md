# Chatsity: The Financial Chatroom
Chatroom API that allows multiple users to communicate in multiple chatrooms and request stock quotes from an external API.

# Features implemented
- :sparkle: Multiple chatroom Support.
- :sparkle: Bot error handling requests.
- :sparkle: Signup users
- :white_check_mark: Allow registered users to log in and talk with other users
- :white_check_mark: Allow users to post messages as commands into the chatroom with the following format /stock=stock_code
- :white_check_mark: Decoupled bot that handles stock quote requests (parses CSV and retrieves information).
- :white_check_mark: Secure chat that allow users to send messages in separated chatrooms.
- :white_check_mark: Ability to switch between chatrooms.
- :white_check_mark: List the last 50 messages from a particular chatroom.
- :white_check_mark: Incremental database Migrations.

# Tools and technologies

- Python 3.8.
- Flask-RESTful.
- MySQL Database, SQLAlchemy ORM.
- HTTP Basic Auth authentication.
- RabbitMQ AMQP messaging handler.
- Amazon Web Services

# Instructions

This project is deployed on an web server on the cloud. To access to the signup form, please go to:

54.83.145.92:9997/api/signup and follow the instructions.

Then, you can login to a chatroom with the id (currently, there are 3 chatrooms created):

- 54.83.145.92:9997/api/chat?id_chatroom=1
- 54.83.145.92:9997/api/chat?id_chatroom=2
- 54.83.145.92:9997/api/chat?id_chatroom=3

The instructions for the API are well documented on code.