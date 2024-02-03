# MultiCat

MultiCat is a novel visualisation technique for analysing multidimensional categorical data. This repository contains the code for a basic [Svelte](https://svelte.dev/) implementation of the MultiCat technique, which can be explored interactively at [https://dgt12.github.io/multicat/](https://dgt12.github.io/multicat/).
The starting point for this project was a template created by [Connor Rothschild](https://www.connorrothschild.com/) for his /newline course, ["Better Data Visualizations with Svelte"](https://www.newline.co/courses/better-data-visualizations-with-svelte/welcome).

## Instructions for analysing your own categorical datasets on a local server:

0. Install the following development tools on your machine: [Node.js](https://nodejs.org/en), [Visual Studio Code](https://code.visualstudio.com/) and [Python](https://www.python.org/downloads/), including the Pandas library.
1. Download or clone the entire [multicat](https://github.com/dgt12/multicat) GitHub repository.
2. Prepare a CSV file of the data you wish to analyse that contains *only* nominal and/or ordinal variables (one row per data item, one column per variable). Save this in the `multicat/src/data` folder.
3. Open the Python script `convert_to_js.py` in the same `data` folder. Update the filename on line 9 to match the name of your CSV file, minus the `.csv` file extension. 
4. Run `convert_to_js.py`. This will create a file in the same folder with the same name but with a `.js` extension. This is the format that MultiCat accepts as input.
5. Open the entire `multicat` folder in Visual Studio Code. Update line 11 of `App.svelte` to reference your new `.js` file (`import data from "$data/<filename>.js";`). 
7. Open a terminal in Visual Studio Code and enter the command `npm run dev`.
7. Open the `localhost` link in Google Chrome.
8. Start exploring the data!

If you have any questions, feel free to contact [David Trye](mailto:davidtrye@gmail.com).