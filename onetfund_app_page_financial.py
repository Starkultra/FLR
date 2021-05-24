# -*- coding: utf-8 -*-
"""
Created on Wed May 19 09:43:41 2021

@author: fluec
"""


import streamlit as st


def main():

    st.header("FINANCIAL: CONSOLIDATED STATEMENT OF VALUE")
    col1,col2 = st.beta_columns(2)
    with col1:
      st.info("Damages")
      st.write("Current: $600M")
      st.write("With Mitigation Pathways: $200M")

      st.info("Expected Insured Losses")
      st.write("Current")
      st.write("With Mitigation Pathways")
    
      st.info("Cost of Business Disruption")
      st.write("Current")
      st.write("With Mitigation Pathways")

      st.info("Property Value(RENT)")
      st.write("Current")
      st.write("With Mitigation Pathways")

      st.info("Annual Tourism Revenues")
      st.write("Current")
      st.write("With Mitigation Pathways")

      
    with col2:
      st.info("Value at Risk")
      st.write("Current: $1BN")
      st.write("With Mitigation Pathways: $100M")

      st.info("Expected Credit Losses")
      st.write("Current")
      st.write("With Mitigation Pathways")

      st.info("Annual Utility Costs")
      st.write("Current")
      st.write("With Mitigation Pathways")

      st.info("Property Value(SALE)")
      st.write("Current")
      st.write("With Mitigation Pathways")

      st.info("Tax Benefits")
      st.write("Current")
      st.write("With Mitigation Pathways") 
      

     
      
if __name__ == '__main__':
	main()   

      
