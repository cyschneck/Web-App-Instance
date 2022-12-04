from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

# Render flask pages
@app.route('/')
@app.route('/home')
def render_home_page():
	return render_template('home_page.html')

## star-chart-spherical-projection
@app.route('/star-chart-spherical-projection', methods=["GET"])
def render_star_chart_page():
	return render_template('star_chart_spherical_projection.html')

def run_star_chart_spherical_projection(hemisphere, yearProperMotion, displayStarName, displayDeclinationNum, includePrecession, incrementValue):
	import star_chart_spherical_projection
	plot_star_chart_url = "static/star_chart_output.png"
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth=hemisphere,
																yearSince2000=yearProperMotion,
																displayStarNamesLabels=displayStarName,
																displayDeclinationNumbers=displayDeclinationNum,
																isPrecessionIncluded=includePrecession,
																incrementBy=incrementValue,
																figsize_dpi=150,
																showPlot=False,
																save_plot_name=plot_star_chart_url)
	return plot_star_chart_url

@app.route('/star-chart-spherical-projection-results', methods=["POST"])
def render_star_chart_results():
	hemisphere = str(request.form["hemisphere"])
	yearProperMotion = float(request.form["yearProperMotion"])
	displayStarName = bool(request.form.getlist("displayStarName"))
	displayDeclinationNum = bool(request.form.getlist("displayDeclinationNum"))
	includePrecession = bool(request.form.getlist("includePrecession"))
	incrementValue = int(request.form["incrementValue"])

	plot_star_chart_url = run_star_chart_spherical_projection(hemisphere, yearProperMotion, displayStarName, displayDeclinationNum, includePrecession, incrementValue)

	return render_template('star_chart_spherical_projection_results.html', plot_star_chart_url=plot_star_chart_url)

## muller-eot
@app.route('/muller-eot', methods=["GET"])
def render_eot_page():
	return render_template('muller_eot.html')

def run_muller_eot(eccentricity, obliquity, orbitalPeriod):
	import muller_eot
	plot_eot_url = "static/eot_chart_output.png"
	# Combined Effect of Obliquity and Eccentricity
	orbital_period_planet = muller_eot.calculateOrbitalPeriod(orbitalPeriod)
	eot_diff_dict = muller_eot.calculateDifferenceEOTMinutes(eccentricity=eccentricity,
															obliquity_deg=obliquity,
															orbit_period=orbital_period_planet)
	muller_eot.plotEOT(planet_name="Earth",
						eot_dict=eot_diff_dict,
						effect_title_str="Eccentricity ({0}) and Obliquity ({1})".format(eccentricity, obliquity),
						figsize_dpi=150,
						showPlot=False,
						save_plot_name=plot_eot_url)

	return plot_eot_url, eot_diff_dict

@app.route('/muller-eot-results', methods=["POST"])
def render_eot_results():
	eccentricity = float(request.form["eccentricity"])
	obliquity = float(request.form["obliquity"])
	orbitalPeriod = float(request.form["orbitalPeriod"])

	plot_eot_url, eot_dict = run_muller_eot(eccentricity, obliquity, orbitalPeriod)

	return render_template('muller_eot_results.html', plot_eot_url=plot_eot_url, eot_dict=eot_dict)

# flask app only runs once to avoid running more than once
if __name__ == "__main__":
	app.run(debug=True)
