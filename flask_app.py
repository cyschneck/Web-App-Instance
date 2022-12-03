from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

# Render flask pages
@app.route('/')
def render_home_page():
	return render_template('home_page.html')
	
@app.route('/star-chart-spherical-projection')
def render_star_chart_page():
	return render_template('star_chart_spherical_projection.html')

def run_star_chart_spherical_projection(hemisphere, yearProperMotion, displayStarName, displayDeclinationNum, includePrecession, incrementValue):
	import star_chart_spherical_projection
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth=hemisphere,
																yearSince2000=yearProperMotion,
																displayStarNamesLabels=displayStarName,
																displayDeclinationNumbers=displayDeclinationNum,
																isPrecessionIncluded=includePrecession,
																incrementBy=incrementValue)

@app.route('/star-chart-spherical-projection-results')
def render_star_chart_results():
	return render_template('star_chart_spherical_projection_results.html')

@app.route('/muller-eot')
def render_eot_page():
	return render_template('muller_eot.html')

def run_muller_eot(eccentricity, obliquity, orbitalPeriod):
	import muller_eot
	# Combined Effect of Obliquity and Eccentricity
	eot_combined_y = muller_eot.calculateDifferenceEOTMinutes(eccentricity=eccentricity,
															obliquity_deg=obliquity,
															orbit_period=orbitalPeriod)
	muller_eot.plotEOT(planet_name="Earth",
						orbital_period=orbitalPeriod,
						eot_y=eot_combined_y,
						effect_title_str="Eccentricity ({0}) and Obliquity ({1})".format(earthEccentricity, earthObliquity))

@app.route('/muller-eot-results')
def render_eot_results():
	return render_template('muller_eot_results.html')

# flask app only runs once to avoid running more than once
if __name__ == "__main__":
	app.run()
