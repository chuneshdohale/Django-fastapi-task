Setup this Repo on Local PC
In main.py comment the following line

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username,db_password, host_server, db_server_port, database_name, ssl_mode)
and uncomment the following line

DATABASE_URL = "sqlite:///./test.db"
Replace following code

engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=20, max_overflow=0
)
with

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
Windows Users
In command terminal run the following command

python -m venv env
env/Scripts/activate
python -m pip install -U pip
pip install -r requirements.txt


If you want to use sqlite then install databases module for sqlite as follows

pip install databases[sqlite]
Run this app on Local PC
In command terminal run the following command

uvicorn main:app --reload