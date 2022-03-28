# COMP4461_Rasa_Chatbot


step 1:
- cd to chatroom-Bot
- conda create --name [your environment name] python=3.8
- conda activate [your environment name] (should be in the virtual environment)
- pip install -r requirments.txt
- cd my_project
- python manage.py runserver
- go to http://127.0.0.1:8000/my_app/
- go back to terminal (chatroom-Bot)
- rasa train (if modified yml file)