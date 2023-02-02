#this is the main hosting file for the dashboard.

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit import caching
import streamlit.components.v1 as components, html
from google1 import main as mn
import plotly.express as px
import base64
from streamlit_option_menu import option_menu

from Pages import WorldMap, Disaster, Compare, CountryProfile,Information, Data_Credibility

import copy

from pathlib import Path
import seaborn as sns
import geopandas

# import plotly.express as px
from PIL import Image
import plotly.graph_objects as go


#basic functions for using streamlit for building dashboards.
# 
# st.set_page_config(layout="wide")
st.set_page_config(page_title="Food Systems Resilience Diagnostics", layout="wide")

a,b,c = st.sidebar.columns([1,5,1])
a.write('')
b.image("FSDR_1.png")
c.write('')


apps = [
    {"func": WorldMap.app, "title": "World Map", "icon": "map"},
    {"func": CountryProfile.app, "title": "Country Profile", "icon": "tools"},
    {"func": Compare.app, "title": "Compare", "icon": "graph-up-arrow"},
    {"func": Disaster.app, "title": "Disaster Vulnerability", "icon": "radioactive"},
    {"func": Data_Credibility.app, "title": "Data Check", "icon": "file-check"},
    {"func": Information.app, "title": "Information", "icon": "info-circle"}
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()
print("Params: "+str(params))

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index =0


selected = option_menu(
        "Navigation",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
        orientation = "horizontal"
    )
if(selected!="About"):
    st.sidebar.title("Control Center")

st.title("Food Systems Resilience Diagnostics (FSRD) Tool")
st.markdown('The FSRD gives the scores for several food system resilience indicators based on the performance of the countries.')
st.markdown('This Dashboard is the preliminary version of a diagnostic tool for rapidly scanning food stresses and shocks.')

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
   
my_html1 = """<h3>Please share your experience of using this tool 
    <a href="https://forms.gle/JpgirdYtypVdiLC27" target="_blank">HERE</a> </h3>
    """

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
components.html(my_html1)

st.sidebar.subheader("PARTNERS")
st.sidebar.image('partners.PNG')
