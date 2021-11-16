from flask import Flask, render_template, request, redirect
import sqlite3
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

	# When a search is submitted.
	if request.method == 'POST':

		# Getting content.
		search_ack = request.form['ack']

		try: 
			# redirecting to Ack page.
			return redirect('/' + search_ack)
		except:
			pass

	# Show the initial page when the bottom in not press.
	else:

		return render_template('index.html')



@app.route('/<ack>')

def search_ack(ack):

	# Connection to database.
	connection = sqlite3.connect("X:/Santi/Donut/Donut 2.0/dist/donut_database.db")
	cursor = connection.cursor()

	status = 'start'
	
	# Searching for ack in Database.
	search_query = cursor.execute("SELECT DISTINCT style FROM timetrack_table WHERE ack = ? AND status = ?", (ack, status)).fetchall()

	style_list = []

	for i in search_query:

		style_list.append(i[0])

	# Displaying 
	return render_template('style.html', ack = ack, style_list = style_list )

	# Close db connection.
	connection.close()


@app.route('/<ack>/<style>')

def search_style(ack, style):

	# Connection to database.
	connection = sqlite3.connect("X:/Santi/Donut/Donut 2.0/dist/donut_database.db")
	cursor = connection.cursor()

	status = 'start'
	
	# Searching for ack in Database.
	search_query = cursor.execute("SELECT DISTINCT piece_number FROM timetrack_table WHERE ack = ? AND status = ? AND style = ?", (ack, status, style)).fetchall()

	item_list = []

	for i in search_query:

		item_list.append(i[0])

	# Displaying 
	return render_template('style_details.html', ack = ack, style = style, item_list = item_list )

	# Close db connection.
	connection.close()


@app.route('/<ack>/<style>/<item>')

def item_details(ack, style, item):

	# Connection to database.
	connection = sqlite3.connect("X:/Santi/Donut/Donut 2.0/dist/donut_database.db")
	cursor = connection.cursor()

	status = 'start'
	
	# Searching for ack in Database.
	search_query = cursor.execute("SELECT department, employee, date_scanned,time_scanned FROM timetrack_table WHERE ack = ? AND status = ? AND style = ? AND piece_number = ?", (ack, status, style, item)).fetchall()

	details_list = []

	for i in search_query:

		details_list.append(i)

	# Displaying 
	return render_template('item_details.html', ack = ack, style = style, item = item, details_list = details_list ) 

	# Close db connection.
	connection.close()






if __name__ == '__main__':

	app.run(debug = True)

