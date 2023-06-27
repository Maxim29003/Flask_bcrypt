from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)

bcrypt = Bcrypt(app)

@app.route('/')
def index():
	password = 'password'
	hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
	is_valid = bcrypt.check_password_hash(hashed_password, password)
	return 'Password {0}, Hash password {1}, is_valid {2}'.format(password,hashed_password,is_valid)

if __name__ == '__main__':
	app.run(debug=True)
