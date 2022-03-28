# COMP4461_Rasa_Chatbot

## Please download Miniconda if you don't have conda installed in your computer

## Open 2 terminals, both cd to chatroom-Bot

### Terminal 1
- cd to chatroom-Bot
- conda create --name [your environment name] python=3.8
- conda activate [your environment name] (should be in the virtual environment)
- pip install -r requirments.txt (takes a while first time)
- cd my_project
- python manage.py runserver
- go to http://127.0.0.1:8000/my_app/

### Terminal 2
- cd to ./my_project/quarantineBot
- rasa train (if modified yml file)
- rasa run -m models --enable-api --cors "*"

## Back to http://127.0.0.1:8000/my_app/
- refresh webpage and the chatbot is ready to work