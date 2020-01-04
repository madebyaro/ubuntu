# tool to parse out the package names from top-pypi-packages

import json
from pprint import pprint
outfile = open('pkgnames.txt',"w")

with open('top-pypi-packages-365-days.json') as f:
	data = json.load(f)
	rows = data['rows']
	for info in rows:
		print(info["project"])
		outfile.write(info["project"] + '\n')

outfile.close()
