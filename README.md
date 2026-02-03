# MultiCat

### About

MultiCat is an interactive visualisation technique for analysing multidimensional categorical data. Our prototype has been implemented in [Svelte](https://svelte.dev/) and can handle up to 20 nominal and ordinal variables. The starting point for this project was a template created by [Connor Rothschild](https://www.connorrothschild.com/) for his *newline* course, [Better Data Visualizations with Svelte](https://www.newline.co/courses/better-data-visualizations-with-svelte/welcome).

### Demo

A demo instance of the prototype, featuring the [Titanic data](https://www.datavis.ca/papers/titanic/data/Dawson_JSE_1995.pdf), is available at [https://dgt12.github.io/multicat/](https://dgt12.github.io/multicat/). You can also upload your own CSV files by clicking on the "Load Dataset..." button. Each file should have one row per item (as well as a header row at the top) and one column per variable. Ordinal categories should begin with a number denoting their order, followed by a space (e.g. "1 low", "2 medium", "3 high"). In the header, add the prefix "id_" to any non-categorical variables in order to exclude them from the visualisation.

![The MultiCat interface, including a spreadsheet view on the left and a sidebar on the right](/titanic.png)

### Contact

If you have any questions, feel free to contact [David Trye](mailto:davidtrye@gmail.com).
