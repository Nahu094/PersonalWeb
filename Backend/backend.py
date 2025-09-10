from pathlib import Path
from flask import Flask, render_template
from dotenv import load_dotenv

basedir = Path().absolute()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


app= Flask(__name__,
	static_folder=f'{basedir}/Docs/static',
	template_folder=f'{basedir}/Docs/templates')

app.config['SERVER_NAME'] = os.getenv('SERVER_NAME')
app.secret_key = os.getenv('SERVER_SECRET')

db_config = {
    'host': os.getenv('DB_ADDR'),
    'user': os.getenv('DB_USR'),
    'password': os.getenv('DB_PWD'),
    'database': os.getenv('DB_DATABASE')
}

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')