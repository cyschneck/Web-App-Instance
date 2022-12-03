from flask import Flask, render_template

app = Flask(__name__)

# Render flask pages
@app.route('/')
def render_home_page():
	return render_template('home_page.html')
	
@app.route('/star-chart-spherical-projection')
def render_star_chart_page():
	return render_template('star_chart_spherical_projection.html')
	
@app.route('/muller-eot')
def render_eot_page():
	return render_template('muller_eot.html')

# flask app only runs once to avoid running more than once
if __name__ == "__main__":
	app.run()
