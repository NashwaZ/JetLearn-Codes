import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

titanic_df = pd.read_csv('titanic.csv')

#Creating graphs

hist = px.histogram(
    titanic_df,
    x = 'Survived',
    title = 'Survival Count',
    template = 'plotly_white',
    width = 700,
    height = 500,
    nbins = 2,
    opacity = 0.7,
    color = 'Sex',
    marginal = 'rug'
)

hist.write_html('Survival_Count.html',auto_open=True)



#Displaying multiple graphs in one window

figure = make_subplots(
    rows = 2,
    cols = 3,
    subplot_titles=['Line Plot','Line Plot 2', 'Grades Bar Chart','Pie Chart','Scatter Plot']
)

#figure.add_trace()