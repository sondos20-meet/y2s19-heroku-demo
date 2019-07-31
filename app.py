from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	favoritefood = ['everythig','everysing','everydrink']
	return render_template(
		"index.html",
		favoritefood=favoritefood,
		opposite_day=True)

if __name__ == '__main__':
   app.run(debug = True)

