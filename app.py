import streamlit as st
import datetime as dt
import pandas as pd
import numpy as np

st.title("ONCF App")

minDate = dt.date(2022,1,1)
maxDate = dt.date(2022, 3, 31)
date1=st.date_input('Entrez La date', minDate , min_value=minDate, max_value=maxDate)
options=np.array(["6:00","7:00","8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00"])
heure =st.selectbox("Entrez votre heure de voyage", options)


