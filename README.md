# Web-App-Instance
Web app instance of Python code running on Flask

## Run on Localhost

127.0.0.1:5000 --> Localhost
```
python3 flask_app.py
```

## PyPi Packages as Web Apps

Generate a star chart: [star-chart-spherical-projection](https://pypi.org/project/star-chart-spherical-projection/)

Options:
-Select Hemisphere (North centered on +90°, South centered on -90): North or South
-Year Difference from 2000 (i.e. -31 = 1969): -31
-Display Star Names: True or False
-Display Declination Numbers: True or False
-Include Precession of the Equinoxes: True or False
-Increment Declination by: 1°, 5°, 10°

Example Output:
![star_chart](https://raw.githubusercontent.com/cyschneck/Web-App-Instance/main/static/star_chart_output.png)

Generate Graphs for the Equation of Time: [muller-eot](https://pypi.org/project/muller-eot/)

Options:
-Eccentricity: 0.01671022
-Obliquity (Degrees): 23.4367
-Orbital Period (AU): 1.0000001124

Example Output:
Generate a EOT graph with arbitrary eccentricity, obliquity, orbital period
![effect_eot](https://raw.githubusercontent.com/cyschneck/Web-App-Instance/main/static/eot_chart_output.png)

