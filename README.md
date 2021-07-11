# fastapitest
Python Version 3.9

Create environment using command below<br />
virtualenv -p python3 venv<br />

Activate virtual environment using command below<br />
source venv/bin/activate<br />

Now install dependencies using the command below<br />
pip install -r requirements.txt<br />

Once you've installed all the requirements please make .env file on the root directory and add following variables there (after create postgres database, you've to put your database credentials)<br />
DATABASE //Engine Name<br />
USER //database username<br />
PASSWORD //database password<br />
HOST //host name<br />
DBNAME //database name<br />

Run following command for run server<br />
uvicorn main:app --reload<br />
Now server is running on following link<br />
127.0.0.1:8000<br />

You can see API documentation on the link below<br />
127.0.0.1:8000/docs
