# IMPORT ALL NECESSARY PACKAGES HERE
####################################
import streamlit as st
st.set_page_config(layout="wide") # this makes the streamlit use the full width of the page
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from skimage import io

####################################

# ADD ALL FUNCTIONS FROM YOUR JUPYTER NOTEBOOKS HERE ONCE TESTED
# EACH FUNCTION MUST BE SELF CONTAINED, TO TEST THAT THEY ARE RUN THEM IN A JUPYTER NOTEBOOK FOR TESTING (see function_testing_notebook)
######################################################################
######################################################################
# this function returns our two dataframes we need for everything else
# make sure that the file paths are right

forest_fires = pd.read_csv('forestfires.csv')
CO2_emissions = pd.read_csv('CO2Emission_LifeExp.csv')
cleaned_df = pd.read_csv("Year_Country_AvgTemp.csv")
Emission = CO2_emissions
city = pd.read_csv("GlobalWarming_InterestBy_City.csv")
grouped_countries = pd.read_pickle('countries.pkl')


def show_temp_map():
    fig = px.choropleth(grouped_countries, locations="Country", color="AvgTemperature", animation_frame="Year", locationmode = "country names", height = 750, range_color=[15,95], title='Yearly Average Temperature Around the World')
    return fig

def show_global_warming_city():
    fig = px.scatter(city, x='City', y='Global Warming: (1/1/04 - 9/27/21)')
    return fig

def show_scatter_with_background(forest_fires):
    # Create figure
    figs = go.Figure()

    # Add trace
    figs.add_trace(
        go.Scatter(x=forest_fires['temp'], y=forest_fires['wind'], mode='markers')
    )

    # Add images
    figs.add_layout_image(
            dict(
                source="https://static.scientificamerican.com/sciam/cache/file/C1CBDCD7-0471-4C47-846607ADAF8585F4_source.jpg",
                xref="x",
                yref="y",
                x=15,
                y=5,
                sizex=50,
                sizey=10,
                sizing="fill",
                opacity=0.5,
                xanchor = 'center',
                yanchor = 'middle',
                layer="below")
    )
    figs.update_layout(template="plotly_white")
    return figs

def CO2EmissionsScatter():
    graph = px.scatter(CO2_emissions, x="CO2Emissions", y='LifeExpectancy', title='Global warming', color='Code')
    return graph

def CO2EmissionsChoro():
    fig = px.choropleth(CO2_emissions, locations='Code', locationmode = "ISO-3", color='LifeExpectancy')
    return fig

def ForestFiresScatter():
    grapp = px.scatter(forest_fires, x='temp', y='wind', title='Forest Fires', color='FFMC', hover_data=['DMC','DC','ISI','temp','RH'])
    return grapp


def ForestFiresGap():
    anim = px.data.gapminder()
    ani = px.scatter(forest_fires, x='day', y='temp', animation_frame='month',animation_group='ISI', size='DMC', color='FFMC', category_orders={'month':['jan', 'feb', "mar", 'apr', "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],'day':['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']}, )
    ani.update_yaxes(range=[1, 34])
    return ani

def ForestFiresCon():
    figster = px.density_contour(forest_fires, x="month", y="temp", marginal_x="histogram", marginal_y="histogram", hover_data=["FFMC", "DMC", "DC", "ISI", "RH", "wind", "rain", "area"], category_orders={'month':['jan', 'feb', "mar", 'apr', "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],'day':['mon', 'tue', 'wed', 'thu', 'fri', 'sad']})
    return figster

def ForestFiresPhoto():
    figi = px.scatter_3d(forest_fires, x="wind", y="temp", z="month", color="RH", size="DMC",hover_name="temp", color_discrete_map = {"area": "month", "day": "ISI", "RH":"DC"})
    return figi

def ImgScatter():
    img = io.imread('https://magazine.columbia.edu/sites/default/files/styles/facebook_sharing_1200x630/public/2018-09/Wild-fires.jpg?itok=EB1o8SLf')
    imagee = px.imshow(img)
    return imagee

def show_scatter():
    scatter = px.scatter(cleaned_df, x='Year', y = 'Average Temp', color = 'Country')
    return scatter

def show_line():
    line = px.line(cleaned_df, x='Year', y = 'Average Temp', color = 'Country')
    return line

def show_Emissions():
    Emissions = px.choropleth(Emission, locations="Code", color="CO2Emissions", hover_name="Country", range_color=[0,5000000000])
    return Emissions

def show_Percapita():
    Percapita = px.choropleth(Emission, locations="Code", color="Percapita", hover_name="Country", range_color=[0,25])
    return Percapita


######################################################################
######################################################################


# NOW ALL WE NEED TO FOCUS ON IS DESIGNING OUR STREAMLIT PAGE WITH OUR VISUALS 
######################################################################
######################################################################
######################################################################

# BEFORE DOING ANYTHING, LETS IMPORT OUR DATA USING THE MASTER FUNCTION SO IT CAN BE USED LATER
# ADD A TITLE AND SUBTITLE AT THE TOP
st.title("Global Warming and Its Effects")
st.subheader("BY: AI-Camp")

st.markdown("<h4>This dataset is dedicated to explaining how global warming has affected multiple areas of life; including devastating forest fires, horrible CO2 emissions, and horrifiying temperature increases. Please view with consideration. </h4>", unsafe_allow_html=True)
# THIS SECTION SHOWS HOW YOU CAN HAVE TWO COLUMNS SIDE BY SIDE, THE RATIO DEFINES HOW MUCH SPACE EACH COLUMN TAKES UP
# IN THIS CASE 3,2 MEANS row0_1 WILL BE 3X WIDE AND row0_2 WILL BE 2X WIDE
# YOU WILL LIKELY HAVE TO MANUALLY SET THE WIDTH AND HEIGHT OF VISUALS

st.markdown("""
<style>
@font-face {
    font-family: LuxuriousRoman;
    src: url(LuxuriousRoman-Regular.ttf);
}
  
p {
    font-family: LuxuriousRoman;
}

h1 {
    font-family: LuxuriousRoman;
}
h2 {
    font-family: LuxuriousRoman;
}
h3 {
    font-family: LuxuriousRoman;
}
h4 {
    font-family: LuxuriousRoman;
}
</style>
""", unsafe_allow_html=True)

fig1 = show_scatter_with_background(forest_fires)
fig2 = CO2EmissionsScatter()
fig3 = CO2EmissionsChoro()
fig4 = ForestFiresScatter()
fig6 = ForestFiresGap()
fig7 = ForestFiresCon()
fig8 = ForestFiresPhoto()
fig9 = ImgScatter()

fig10 = show_scatter()
fig11 = show_line()
fig12 = show_Emissions()
fig13 = show_Percapita()

fig14 = show_global_warming_city()
fig15 = show_temp_map()


row0_1, row0_2 = st.columns((1,1))
with row0_1:
    st.plotly_chart(fig1, use_container_width=True)
with row0_2:
    st.write('')
    st.write("If a dot is yellow, it signifies a high FFMC, which stands for Fine Fuel Moisture Code. When you have a high FFMC, that means that there is a likely chance of a wildfire to occur in that area due to the fact that it is very dry. This is becoming a big factor in climate change.")
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

# button = st.button("Click me if you want a surprise")
# if button:
#     st.text("I'm the surprise")

# THIS SECTION SHOWS HOW YOU CAN HAVE TWO VISUALS SIDE BY SIDE, THE RATIO DEFINES HOW MUCH SPACE EACH COLUMN TAKES UP
# IN THIS CASE 2,2 MEANS row1_1 AND row1_2 WILL BE THE SAME WIDTH
# HERE WE SHOW HOW TO SET WIDTH AND HEIGHT OF VISUALS, YOU WILL HAVE TO TEST WHAT WORKS FOR YOU
row1_1, row1_2 = st.columns((1,1))

with row1_1:
    st.plotly_chart(fig2, use_container_width=True)
    st.write('Global CO2 emissions by country.')
with row1_2:
    st.plotly_chart(fig3, use_container_width=True)
    st.write('Global life expectancy because of CO2 emissions.')

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

st.plotly_chart(fig4, use_container_width=True)
st.write('Global forest fires because of the wind and temp. FFMC(Fine Fuel Moisture Code).')

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

row3_1, row3_2 = st.columns((1,1))

with row1_1:
    st.plotly_chart(fig6, use_container_width=True)
    st.write('Global forest fires by month, day, and temperature.')
with row1_2:
    st.plotly_chart(fig7, use_container_width=True)
    st.write('A chart that has multiple layers to explain how many fires have begun to occur.')

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
row4_1, row4_2 = st.columns((1,1))

with row1_1:
    st.plotly_chart(fig8, use_container_width=True)
    st.write('A 3d chart explaining how any fires have occurred with data for months, temperature, and wind.')
with row1_2:
    st.plotly_chart(fig9, use_container_width=True)
    st.write("A symbolic photo of our world's state today.🔥 ")


st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

row5_1, row5_2 = st.columns((3, 2))

with row5_1:
    st.plotly_chart(fig14, use_container_width=True)
with row5_2:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('Global warming in the city.')


st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

row6_1, row6_2 = st.columns((1, 1))
with row6_1:
    st.plotly_chart(fig10, use_container_width=True)
    st.write('Scatter Plot of Average Temperature Change of Countries.')

with row6_2:
    st.plotly_chart(fig11, use_container_width=True)
    st.write('Line Graph of Average Temperature Change of Countries.')
st.write('')
st.write('')
st.write('')
st.write('These graphs show the temperature change from one year to another. In the past twenty years, we can see that the temperature change has been mostly positive which shows that the average temperature of the world is rising.')

row7_1, row7_2 = st.columns((1, 1))

with row7_1:
    st.plotly_chart(fig12, use_container_width=True)
    st.write('World Map with CO2 Emissions from every Country.')
with row7_2:
    st.plotly_chart(fig13, use_container_width=True)
    st.write('World Map with CO2 Emissions per Capital for Each Country.')

st.write('')
st.write('')
st.write('The first graph shows the CO2 Emissions emitted by a Country while the second graph takes the CO2 Emissions of a country and divides it by the population of the country. The second graph which shows the CO2 Emissions per capita takes the CO2 emissions in relation to every person in that country.')


st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

st.plotly_chart(fig15, use_container_width=True)

