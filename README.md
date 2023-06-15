# Web-App-Instance
Web app instance of PyPi packages star-chart-spherical-projection and muller-eot running on Flask

## Run on Localhost

127.0.0.1:5000 --> Localhost
```
python3 flask_app.py
```

## PythonAnywhere Hosting

[cyschneck.pythonanywhere.com](http://cyschneck.pythonanywhere.com/)

## PyPi Packages as Web Apps

### Generate a Star Chart

[star-chart-spherical-projection](https://pypi.org/project/star-chart-spherical-projection/)

Options:
- Select Hemisphere (North centered on +90°, South centered on -90): North or South
- Year Difference from 2000 (i.e. -31 = 1969): -31
- Display Star Names: True or False
- Display Declination Numbers: True or False
- Include Precession of the Equinoxes: True or False
- Increment Declination by: 1°, 5°, 10°
- Select Stars to be included from a List of Avaliable Stars: ['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 'Alioth', 'Alkaid', 'Almach', 'Alnilam', 'Alnitak', 'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 'Beta Phoenicis', 'Betelgeuse', 'Canopus', 'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Deneb', 'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 'Gienah', 'Hadar', 'Hamal', 'Kochab', 'Kornephoros', 'Lesath', 'Markab', 'Megrez', 'Meissa', 'Menkalinan', 'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 'Pollux', 'Procyon', 'Rasalhague', 'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 'Scheat', 'Schedar', 'Segin', 'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Unukalhai', 'Vega', 'Wezen', 'Zosma', 'Zubeneschamali']

**Example Output**
Output includes: A star chart and a list of all the final positions of stars (declination, right ascension)
![star_chart](https://raw.githubusercontent.com/cyschneck/Web-App-Instance/main/static/img/star_chart_output.png)

### Generate Graphs for the Equation of Time

[muller-eot](https://pypi.org/project/muller-eot/)

Options:
- Eccentricity: 0.01671022
- Obliquity (Degrees): 23.4367
- Orbital Period (AU): 1.0000001124

**Example Output**
Output includes: A EOT graph with a list of the difference in time for each day in the year
![effect_eot](https://raw.githubusercontent.com/cyschneck/Web-App-Instance/main/static/img/eot_chart_output.png)

## TODO
Fix absolute path link for png files being generated locally vs. pythonanywhere
