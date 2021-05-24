

#from sklearn.linear_model import LinearRegression
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from matplotlib.ticker import FuncFormatter



# define your app content
def main():
      
  st.header("Environmental: Consolidated Statement of Value")
  st.text('')
  st.text('')
  st.text('')
  path = os.path.dirname(os.path.abspath(__file__))
  file = 'lineraregression.pickle'
  #pickle_in = open(path+"\\"+file, 'rb')
  pickle_in = open('lineraregression.pickle', 'rb')
  pickle_model = pickle.load(pickle_in)


  trees_amount = 500
  investment_amount = 100000
  model_input = np.array([[trees_amount, investment_amount]]).astype(np.float64)

  
  col1, col2, col3 = st.beta_columns(3)
  with col1:
      st.text('')
  with col2:
      st.success('**Current**')
  with col3:
      st.success('**With Mitigation Pathways**')


  colb1, colb2, colb3 =st.beta_columns(3)
  
  with colb1:
      st.write("Carbon Emissions in tonnes")
      st.write("Waste and Water Filtration Value")
      st.write("Water Vulnerability")
      st.write("Ecosystem Services Vulnerability")
      st.write("Mean Estimated Soil Erosion Rate")
  
      
  with colb2:
      st.write(" ")
      # Load the Pickle file in memory for Carbon Emission in Tonnes
      #pickle_in = open('lineraregression.pickle', 'rb')
      #pickle_model = pickle.load(pickle_in)
      carbon_emission = pickle_model.predict(model_input)
      st.write('%d GT' % carbon_emission)
      
      # Load the Pickle file in memory for Waste and Water Filtration Value 
      #pickle_in = open('lineraregression.pickle', 'rb')
      #pickle_model = pickle.load(pickle_in)
      waste_water_filtration = pickle_model.predict(model_input)
      st.write('%d' % waste_water_filtration)
      
      # Load the Pickle file in memory for Water Vulnerability 
      #pickle_in = open('lineraregression.pickle', 'rb')
      #pickle_model = pickle.load(pickle_in)
      water_vulnerability = pickle_model.predict(model_input)
      st.write('%d' % water_vulnerability)
      
      # Load the Pickle file in memory for Ecosystem Services Vulnerability
      #pickle_in = open('lineraregression.pickle', 'rb')
      #pickle_model = pickle.load(pickle_in)
      ecosystem_services_vulnerability = pickle_model.predict(model_input)
      st.write('%d' % ecosystem_services_vulnerability)
      
      # Load the Pickle file in memory for Mean Estimated Soil Erosion Rate
      #pickle_in = open('lineraregression.pickle', 'rb')
      #pickle_model = pickle.load(pickle_in)
      mean_estimated_soil_erosion_rate = pickle_model.predict(model_input)
      st.write('%d' % mean_estimated_soil_erosion_rate)
    
  with colb3:
      st.write(" ")
      st.write('%d GT' % carbon_emission)
      st.write('%d GT' % waste_water_filtration)
      st.write('%d' % water_vulnerability)
      st.write('%d' % ecosystem_services_vulnerability)
      st.write('%d' % mean_estimated_soil_erosion_rate)


  colF1, colF2, colF3 = st.beta_columns(3)
  with colF1:
    st.success('**Total Environmental Value**')
  with colF2:
    st.success('$')
  with colF3:
    st.success('$')


  colG1, colG2, colG3 = st.beta_columns(3)
  with colG1:
       st.write("")
  with colG2:
    df_carbon = pd.DataFrame({ 
                       'Price per Ton/Carbon - USD': range(0,150,10),
                       'USD': range (100,15000000,1000000)})    
    st.write("### Total Value of Carbon Sequestration - USD")
    fig, ax = plt.subplots()
    ax=sns.lineplot(x='Price per Ton/Carbon - USD', y='USD', data=df_carbon, color='red',linewidth=2.5)
    ax.set_ylabel("USD")
    ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    ax.set_xlabel("Price per Ton/Carbon - USD")
    st.pyplot(fig)
	
    
    
# execute the main function  	
if __name__ == '__main__':
	main()
