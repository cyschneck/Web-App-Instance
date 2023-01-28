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
	plot_star_chart_url = "/home/cyschneck/mysite/Web-App-Instance/static/img/star_chart_output.png" # "static/img/star_chart_output.png"
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
	return plot_star_chart_url, final_position_of_stars_dict

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
	plot_eot_url = "/home/cyschneck/mysite/Web-App-Instance/static/img/eot_chart_output.png" #"static/img/eot_chart_output.png"
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
