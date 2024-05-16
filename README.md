STEP 1: Install python 2.9 or 2.8 because RASA is not available on a later version of python

Step 2: Create a virtual environment by running ```python -m venv myenv``` in your terminal(replace venv with what you want to name your virtual environment)

Step 3: Activate the virtual environment by running ```venv/Scripts/Activate``` in your terminal. 

NOTE: You might encounter a problem of scripts not being enabled on your system. to solve that, go to the following link --> https://stackoverflow.com/questions/64633727/how-to-fix-running-scripts-is-disabled-on-this-system

Step 4: Install rasa by running ```pip install rasa``` on your terminal with the virtual env activated

step 5: Install Flask by running ```pip install Flask`` on your terminal with the virtual env activated

Step 6: to train the chatbot after making changes to it, run ```rasa train``` in your terminal

Step 7: to run the chatbot, open 2 terminals with the virtual env activated on bot. on the first terminal, run ```rasa run``` and on the second terminal, run ```rasa run actions```

step 8: to open the website, open the app.py file and run it on a third terminal with the virtual environment activated