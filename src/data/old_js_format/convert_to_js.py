# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:50:11 2023
Converts a standard CSV file containing nominal and ordinal variables into a custom .js file for processing in MultiCat.
Update the FILENAME on Line 9, so that it matches your CSV file, minus the ".csv" file extension.
@author: david
"""

FILENAME = "titanic"

import pandas as pd
import json

def csv_to_js(csv_filename, js_filename):
    # Read the CSV file
    df = pd.read_csv(csv_filename)

    # Convert DataFrame to a dictionary
    data = df.to_dict(orient='records')

    # Convert to JS format
    js_data = 'export default ' + json.dumps(data, indent=4) + ';'

    # Write to a JS file
    with open(js_filename, 'w', encoding='utf-8') as js_file:
        js_file.write(js_data)

csv_to_js(FILENAME + ".csv", FILENAME + ".js")
print("Done!")