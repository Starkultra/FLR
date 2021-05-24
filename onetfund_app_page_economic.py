# -*- coding: utf-8 -*-
"""
Created on Wed May 19 09:22:29 2021

@author: fluec
"""

import streamlit as st

# define your app content
def main():

  st.header("ECONOMIC: CONSOLIDATED STATEMENT OF VALUE")


  col1, col2, col3 = st.beta_columns([2,1,1])
  with col1:
      st.text('')
  with col2:
      st.error('Current')
  with col3:
      st.error('With Mitigation Pathways')
  
  colA1,colA2, colA3 = st.beta_columns([2,1,1])
  with colA1:
    st.error("Annual International Tourist Arrivals")   
  with colA2:
    st.text(' ')
    st.write("Here are the results") 
  with colA3:
    st.text(' ')
    st.write("Here are the results")

      
  colB1,colB2, colB3 = st.beta_columns([2,1,1])
  with colB1:
    st.error("International Tourist Arrivals, Annual Growth (%)									")
    st.error("Tourism Sector Size (USD)	")
    st.error("Tourism Sector as % of GDP")
    st.error("Total Number of Jobs in Forestry & Ecotourism Sectors")
    st.error("Total Earned Income of Jobs in Forestry & Ecotourism Sectors")
    st.error("Average Job Losses due to Natural Disasters")
    st.error("Total Income from Job Losses due to Natural Disasters")
    st.error("Cost of Business Disruptions due to Natural Disasters")
    st.error("National Labor Productivity (GDP per hour worked)")
    st.error("Annual Fossil Fuel Subsidies Expenditure")							
      
  with colB2:
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results") 
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results") 
      
  with colB3:
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results") 
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results")
      st.text('')
      st.write("Here are the results") 
      
      
  colF1, colF2, colF3 = st.beta_columns([2,1,1])
  with colF1:
    st.error('TOTAL ECONOMIC VALUE')
  with colF2:
    st.error('$')
  with colF3:
    st.error('$')
    
      
     
# execute the main function  	
if __name__ == '__main__':
	main()