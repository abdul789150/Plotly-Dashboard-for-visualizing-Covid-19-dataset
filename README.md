# Plotly-Dashboard-for-visualizing-Covid-19-dataset

The Dashboard for the visualization of Covid-19 dataset is built using Dash and Plotly. Dash
is a framework used for building Machine Learning and Data Science web applications. The
dataset for Covid-19 is taken from “Our World in Data” website, the dataset is last updated on 26
Oct, 2020. We have used multiple graphs to visualize the dataset. We have used Choropleth map
which are used to represent statistical data through various shading patterns or symbols on
predetermined geographic areas. We have used time series plots to visualize different features with
respect to dates, in last we have also used Box plots, they are used to visualize outliers in the
dataset. In the dashboard you will see the visualizations for the whole world and also separate
visualizations for each country.

## Type of Graphs
In this section we will look into the type of graphs we used.

### Choropleth Map
Choropleth maps are popular thematic maps used to represent statistical data through
various shading patterns or symbols on predetermined geographic areas. We have used
choropleth map for showing Covid-19 cases.

![Choropleth Map](https://github.com/abdul789150/Plotly-Dashboard-for-visualizing-Covid-19-dataset-/blob/main/images/choropleth_map.png)

**You can see the data of any specific country by hovering and selecting the country from Choropleth Map**

### Time Series Graphs
Time series graphs can be used to visualize trends in counts or numerical values over time.
Because date and time information are continuous, points are plotted along the x-axis and
connected by a continuous line.

![Time Series Graph](https://github.com/abdul789150/Plotly-Dashboard-for-visualizing-Covid-19-dataset-/blob/main/images/time_series.png)

### Box Plot Graphs
Boxplots are a standardized way of displaying the distribution of data based on a five
numbers summary (“minimum”, first quartile (Q1), median, third quartile (Q3), and
“maximum”).

![Box Plot Graph](https://github.com/abdul789150/Plotly-Dashboard-for-visualizing-Covid-19-dataset-/blob/main/images/box_plot.png)


## Libraries Required to run this dashboard
- dash
- dash-bootstrap-components
- dash-html-components
- dash-core-components
- plotly
- numpy
- pandas

## How to run this project
For running your dashboard you just need to execute the ```index.py``` file from the command line
