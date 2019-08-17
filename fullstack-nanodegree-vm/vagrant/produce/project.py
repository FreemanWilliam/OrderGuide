from flask import Flask

app = Flask(__name__)

@app.route('/')
def Produce():
	return 'This is the Produce Function'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
	app.debug = True