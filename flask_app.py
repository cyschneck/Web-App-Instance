from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder="templates")

# Render flask pages
@app.route('/')
@app.route('/home')
def render_home_page():
	return render_template('home_page.html')

## star-chart-spherical-projection
@app.route('/star-chart-spherical-projection', methods=["GET"])
def render_star_chart_page():
	all_star_options = ['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 'Alioth', 'Alkaid', 'Almach', 'Alnilam', 'Alnitak', 'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 'Beta Phoenicis', 'Betelgeuse', 'Canopus', 'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Deneb', 'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 'Gienah', 'Hadar', 'Hamal', 'Kochab', 'Kornephoros', 'Lesath', 'Markab', 'Megrez', 'Meissa', 'Menkalinan', 'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 'Pollux', 'Procyon', 'Rasalhague', 'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 'Scheat', 'Schedar', 'Segin', 'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Unukalhai', 'Vega', 'Wezen', 'Zosma', 'Zubeneschamali']
	return render_template('star_chart_spherical_projection.html', all_star_options=all_star_options)

def run_star_chart_spherical_projection(hemisphere, yearProperMotion, displayStarName, displayDeclinationNum, includePrecession, incrementValue, userListOfStars):
	import star_chart_spherical_projection
	# TODO: fix abs path, this currently works with pythonanywhere
	if "Dropbox" in os.getcwd(): # local
		plot_star_chart_url =  "static/img/star_chart_output.png"
		retrieve_url = plot_star_chart_url
	else: # pythonanywhere
		plot_star_chart_url = "/home/cyschneck/mysite/Web-App-Instance/static/img/star_chart_output.png"
		retrieve_url = "https://cyschneck.pythonanywhere.com/static/img/star_chart_output.png"
	final_position_of_stars_dict = star_chart_spherical_projection.finalPositionOfStars(userListOfStars=userListOfStars, 
																						yearSince2000=yearProperMotion,
																						isPrecessionIncluded=includePrecession)
	star_chart_spherical_projection.plotStereographicProjection(userListOfStars=userListOfStars,
																northOrSouth=hemisphere,
																yearSince2000=yearProperMotion,
																displayStarNamesLabels=displayStarName,
																displayDeclinationNumbers=displayDeclinationNum,
																isPrecessionIncluded=includePrecession,
																incrementBy=incrementValue,
																figsize_dpi=150,
																showPlot=False,
																save_plot_name=plot_star_chart_url)
	return retrieve_url, final_position_of_stars_dict

@app.route('/star-chart-spherical-projection-results', methods=["POST"])
def render_star_chart_results():
	hemisphere = str(request.form["hemisphere"])
	yearProperMotion = float(request.form["yearProperMotion"])
	displayStarName = bool(request.form.getlist("displayStarName"))
	displayDeclinationNum = bool(request.form.getlist("displayDeclinationNum"))
	includePrecession = bool(request.form.getlist("includePrecession"))
	incrementValue = int(request.form["incrementValue"])
	userStarsValue = list(request.form.getlist('userStarsValue'))

	plot_star_chart_url, final_position_of_stars_dict = run_star_chart_spherical_projection(hemisphere, yearProperMotion, displayStarName, displayDeclinationNum, includePrecession, incrementValue, userStarsValue)

	return render_template('star_chart_spherical_projection_results.html', plot_star_chart_url=plot_star_chart_url, final_position_of_stars_dict=final_position_of_stars_dict)

## muller-eot
@app.route('/muller-eot', methods=["GET"])
def render_eot_page():
	return render_template('muller_eot.html')

def run_muller_eot(eccentricity, obliquity, orbitalPeriod):
	import muller_eot
	# TODO: fix abs path, this currently works with pythonanywhere
	if "Dropbox" in os.getcwd(): # local
		plot_eot_url =  "static/img/eot_chart_output.png"
		retrieve_url = plot_eot_url
	else: # pythonanywhere
		plot_eot_url = "/home/cyschneck/mysite/Web-App-Instance/static/img/eot_chart_output.png"
		retrieve_url = "https://cyschneck.pythonanywhere.com/static/img/eot_chart_output.png"
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

	return retrieve_url, eot_diff_dict

@app.route('/muller-eot-results', methods=["POST"])
def render_eot_results():
	eccentricity = float(request.form["eccentricity"])
	obliquity = float(request.form["obliquity"])
	orbitalPeriod = float(request.form["orbitalPeriod"])

	plot_eot_url, eot_dict = run_muller_eot(eccentricity, obliquity, orbitalPeriod)

	return render_template('muller_eot_results.html', plot_eot_url=plot_eot_url, eot_dict=eot_dict)

## astrolabe
@app.route('/astrolabe', methods=["GET"])
def render_astrolabe_page():
	return render_template('astrolabe.html')

def determineApside(julian_time):
	# Define the line of apsides (longitude of aphelion and perihelion)
	apside_perihelion = 102.937348 + (1.7195269 * julian_time) + (0.00045962 * (julian_time**2)) + (0.000000499 * (julian_time**3))
	apside_aphelion = apside_perihelion + 180
	return apside_perihelion, apside_aphelion

def determineEccentrictiyOverTime(julian_time):
	# Determine the change in eccentricity over time
	eccentricityAtJulianYear = 0.01670862 - (0.000042037 * julian_time) - (0.0000001236 * (julian_time**2)) + (0.00000000004 * (julian_time**3))
	return eccentricityAtJulianYear

def determineAngularDistanceEquinox(julian_time, given_longitude, given_aphelion):
	# Mean Anomaly of January 0
	mean_anomaly_jan0 = 357.52910 + (35999.0503 * julian_time) - (0.0001559 * (julian_time**2)) - (0.00000048 * (julian_time**3))
	mean_anomaly_jan0 = mean_anomaly_jan0 % 360 # keep anomaly within 0-360

	# Angular distane from vernal equinox to January 0 (midnight of Dec 31)
	angular_distance_equinox = given_aphelion + mean_anomaly_jan0 + (given_longitude / 365)
	angular_distance_equinox = angular_distance_equinox % 360
	angular_distance_equinox -= 360 # reversed from the original position
	return angular_distance_equinox

def offsetfromCenterOfPlate(julian_time, radius_of_plate, given_perihelion):
	# offset from the center of the plate
	eccentricty = determineEccentrictiyOverTime(julian_time) # 0.01667061
	offset_eccentricity = 2 *  eccentricty * radius_of_plate
	x_delta = offset_eccentricity * math.cos(np.deg2rad(given_perihelion))
	y_delta = offset_eccentricity * math.sin(np.deg2rad(given_perihelion))
	return x_delta, y_delta

def run_astrolabe():
	# TODO: fix abs path, this currently works with pythonanywhere
	if "Dropbox" in os.getcwd(): # local
		plot_astrolabe_url =  "static/img/eot_chart_output.png"
		retrieve_url = plot_astrolabe_url
	else: # pythonanywhere
		plot_astrolabe_url = "/home/cyschneck/mysite/Web-App-Instance/static/img/eot_chart_output.png"
		retrieve_url = "https://cyschneck.pythonanywhere.com/static/img/eot_chart_output.png"

	return retrieve_url

@app.route('/astrolabe-results', methods=["POST"])
def render_astrolabe_base_plate_results():
	for form_value in request.form:
		if form_value.startswith('astrolabeBasePlate'):
			obliquity = float(request.form["obliquity"])

	plot_astrolabe_url = run_astrolabe() # TODO
	return render_template('astrolabe_results.html', plot_astrolabe_url=plot_astrolabe_url)

@app.route('/astrolabe-results', methods=["POST"])
def render_astrolabe_eccentric_calendar_results():
	for form_value in request.form:
		if form_value.startswith('astrolabeEccentricCalendar'):
			yearToCalculate = float(request.form["yearToCalculate"])
			longitude = float(request.form["longitude"])
			radiusOfPlate = float(request.form["radiusOfPlate"])

	plot_astrolabe_url = run_astrolabe() # TODO

	return render_template('astrolabe_results.html', plot_astrolabe_url=plot_astrolabe_url)

# flask app only runs once to avoid running more than once
if __name__ == "__main__":
	app.run(debug=True)
