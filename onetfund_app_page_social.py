# -*- coding: utf-8 -*-
"""
Created on Wed May 19 08:51:41 2021

@author: fluec
"""

import streamlit as st

# defining app content
def main():

  st.header('SOCIAL: CONSOLIDATED STATEMENT OF VALUE')
  st.text('')


  col1, col2, col3 = st.beta_columns(3)
  with col1:
      st.text('')
  with col2:
      st.markdown('### Current')
      st.text('')
  with col3:
      st.markdown('### With Mitigation Pathways')
 
    
  cola1, cola2, cola3 = st.beta_columns(3)
  with cola1:
    st.warning('Social Cost of Carbon (SCC)')
  with cola2:
    st.write('SCC per ton')
    st.text(0)
    st.write('Total Current SCC')
    st.text(0)
  with cola3: 
    st.write('SCC per ton')
    st.text(0)
    st.write('Total Current SCC')
    st.text(0)

    
  colb1, colb2, colb3 = st.beta_columns(3) 
  with colb1:
    st.warning('Vulnerability')
  with colb2:  
    st.write('Food Vulnerability')
    st.text(0)
    st.write('Public Health Vulnerability')
    st.text(0)
  with colb3:
    st.write('Food Vulnerability')
    st.text(0)
    st.write('Public Health Vulnerability')
    st.text(0)
    
    
  colC1, colC2, colC3 = st.beta_columns(3) 
  with colC1:
    st.warning('Health (Annual Expenditure)')
  with colC2:  
    st.write('Noncommunicable diseases(NCDs)')
    st.text(0)
    st.write('Respiratory diseases')
    st.text(0)
    st.write('Mental Health')
    st.text(0)
  with colC3:
    st.write('Noncommunicable diseases(NCDs)')
    st.text(0)
    st.write('Respiratory diseases')
    st.text(0)
    st.write('Mental Health')
    st.text(0)


  colD1, colD2, colD3 = st.beta_columns(3) 
  with colD1:
    st.warning('Annual no. of Deaths')
  with colD2:
    st.write('Attributable to NCDs, Respiratory Diseases, Pollution, Mental Health')
    st.text(0)
    st.write('Attributable to Unsafe Water, Sanitation, Hygeine (per capita)')
    st.text(0)
  with colD3:
    st.write('Attributable to NCDs, Respiratory Diseases, Pollution, Mental Health')
    st.text(0)
    st.write('Attributable to Unsafe Water, Sanitation, Hygeine (per capita)')
    st.text(0)

    
  colE1, colE2, colE3 = st.beta_columns(3)
  with colE1:
    st.warning('Others')
  with colE2:
    st.write('Average Life Expectancy')
    st.text(0)
    st.write('National Health Related Productivity Loss (Annual)')
    st.text(0)
    st.write('Annual Academic Average')
    st.text(0)
    st.write('Zoonotic Disease Probability')
    st.text(0)
  with colE3:
    st.write('Average Life Expectancy')
    st.text(0)
    st.write('National Health Related Productivity Loss (Annual)')
    st.text(0)
    st.write('Annual Academic Average')
    st.text(0)
    st.write('Zoonotic Disease Probability')
    st.text(0)
    
    
  colF1, colF2, colF3 = st.beta_columns(3)
  with colF1:
    st.warning('TOTAL SOCIAL VALUE')
  with colF2:
    st.warning('$')
  with colF3:
    st.warning('$')
    
    


# executing the main function
if __name__ == '__main__':
  main()