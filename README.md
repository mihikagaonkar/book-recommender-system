## *Setup*

1. Download Python 3.
2. Clone the repository.
3. Run 
`python3 -m pip install venv`

4. Now run 
`python3 -m venv recommend`

5. Type `recommend\Scripts\activate` to activate the virtual environment.

6. Run 
`python3 -m pip install -r requirements.txt`

7. Download elasticsearch from [here](https://www.elastic.co/)

8. Download logstash from [here](https://www.elastic.co/downloads/logstash)
   
9.  Navigate to the logstash folder and type `bin/logstash -f [path_to_project_directory]/logstash.conf`

10. Navigate to the elasticsearch folder and run `bin\activate`

11. Open another cmd window and run `python database.py`

12. Download cos_sim.csv from [here](https://www.kaggle.com/mihikagaonkar/cosine-similarity-csv)
13.  Run `python app.py` to start the application.


