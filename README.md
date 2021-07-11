# fastapitest
Python Version 3.9

Create environment using command below
virtualenv -p python3 venv

Activate virtual environment using command below
source venv/bin/activate

Now install dependencies using the command below
pip install -r requirements.txt

Once you've installed all the requirements please make .env file on the root directory and add following variables there (your database credentials)
DATABASE //Engine Name
USER //database username
PASSWORD //database password
HOST //host name
DBNAME //database name

Run following command for run server
uvicorn main:app
Now server is running onfollowing link
127.0.0.1:8000
