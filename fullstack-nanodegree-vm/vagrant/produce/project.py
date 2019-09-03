from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Produce, ProduceItem

app = Flask(__name__)

engine = create_engine('sqlite:///producemenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

@app.route('/')
@app.route('/produce/<int:produce_id>/')
def getProduce(produce_id):
	produce = session.query(Produce).filter_by(id=produce_id).one()
	items = session.query(ProduceItem).filter_by(produce_id=produce_id)
	return render_template('menu.html',produce=produce, items=items)

	
@app.route('/produce/<int:produce_id>/new/', methods=['GET','POST'])
def newMenuItem(produce_id):
	if request.method == 'POST':
		newItem = ProduceItem(name=request.form['name'],id=request.form['name'],produce_id = produce_id)
		session.add(newItem)
		session.commit()
		return redirect(url_for('getProduce', produce_id=produce_id))		
	else:
		return render_template('newmenuitem.html',produce_id=produce_id)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
	app.debug = True