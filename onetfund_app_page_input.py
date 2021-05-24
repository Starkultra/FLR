# -*- coding: utf-8 -*-
"""
Created on Wed May 12 10:50:17 2021

@author: fluec
"""

import streamlit as st
#from streamlit_folium import folium_static
#import folium
#from PIL import Image
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import os



# define your app content
def main(state):   
  st.header("Input Details")
  
  path = os.path.dirname(os.path.abspath(__file__))
  file = "4.4.21.Master Conservation Projects Database.xlsx"
  #db = pd.read_excel(path+"\\"+file) 
  db = pd.read_excel(file)
  
  colA1, colA2 = st.beta_columns([1,2])
  with colA1:
    st.info("Amount of Investment")
    #amount_investment_mio = st.number_input("in Million USD", step=10)
    state.amount_investment = float(st.text_input(label="in Million USD", value=state.amount_investment))
    #state.amount_investment = amount_investment_mio * 1000000
    st.markdown(" ")
    st.markdown(" ")


    st.info("Project Location")
    
    
    reforestation_project = st.selectbox("Choose one of the projects below",
                            db['Project Name'], key="reforestation_project")
    db_row = db[db['Project Name']==reforestation_project]
    lat = db_row['Latitude']
    lon = db_row['Longitude']
    
    st.markdown(" ")
    st.info("Type of Tree Species")
    st.write(db_row['Tree Species'])


  with colA2:
    map_data = pd.DataFrame({'lat': lat, 'lon': lon})
    st.map(map_data, zoom = 6)
     


  # # Tree information
  # colB1, colB2, colB3 = st.beta_columns([1,1,2])
  # colB1.info("Type of Tree Species")
  # colB2.info("Number of Trees")
  # trees1 = colB1.text_input("Tree species name", key='trees1')
  # trees1_amount = colB2.number_input("Amount", value=0, step=100, key='trees1_amount')
  # if trees1_amount > 0:
  #    trees2 = colB1.text_input("Tree species name", key='trees2')
  #    trees2_amount = colB2.number_input("Amount", value=0, step=100, key='trees2_amount')
  #    if trees2_amount > 0:
  #       trees3 = colB1.text_input("Tree species name", key='trees3')
  #       trees3_amount = colB2.number_input("Amount", value=0, step=100, key='trees3_amount') 
  #       if trees3_amount > 0:
  #          trees4 = colB1.text_input("Tree species name", key='trees4')
  #          trees4_amount = colB2.number_input("Amount", value=0, step=100, key='trees4_amount') 
  #          if trees4_amount > 0:
  #             trees5 = colB1.text_input("Tree species name", key='trees5')
  #             trees5_amount = colB2.number_input("Amount", value=0, step=100, key='trees5_amount')




  # Asset Details
  st.markdown(" ")
  st.header("Asset Details")

  colB1, colB2, colB3 = st.beta_columns(3)
  colB1.info("Physical Risk(s) Location(s)")

  colC1, colC2, colC3 = st.beta_columns(3)
  with colC1:  
    st.write("**Investor's Assets**")
    #latitude = st.text_input("Latitude / Longitude")
    street = st.text_input("Street", "377 Orange Ave", key="street_investor1")
    city = st.text_input("City", "Perris", key="city_investor1")
    province = st.text_input("Province", "CA", key="province_investor1")
    country = st.text_input("Country", "USA", key="country_investor1")
    
    geolocator = Nominatim(user_agent="GTA Lookup")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(street + ", " + city + ", " + province + ", " + country)
    
    lat = location.latitude
    lon = location.longitude
    lat_lon = [lat, lon]
    lat_lon_str = str(lat_lon) 
    latitude = st.text_input("Latitude / Longitude", lat_lon_str, key="lat_lon_investor1")
    
      


  with colC2:
    st.write("**Client's Assets**")
    #latitude = st.text_input("Latitude / Longitude")
    street = st.text_input("Street", "377 Orange Ave", key="street_client1")
    city = st.text_input("City", "Perris", key="city_client1")
    province = st.text_input("Province", "CA", key="province_client1")
    country = st.text_input("Country", "USA", key="country_client1")
    
    geolocator = Nominatim(user_agent="GTA Lookup")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(street + ", " + city + ", " + province + ", " + country)
    
    lat = location.latitude
    lon = location.longitude
    lat_lon = [lat, lon]
    lat_lon_str = str(lat_lon) 
    latitude = st.text_input("Latitude / Longitude", lat_lon_str, key="lat_lon_client1")
    client_asset_lat = lat
    client_asset_lon = lon


  with colC3:
    st.write("**Supplier's Assets**")
    #latitude = st.text_input("Latitude / Longitude")
    street = st.text_input("Street", "377 Orange Ave")
    city = st.text_input("City", "Perris")
    province = st.text_input("Province", "CA")
    country = st.text_input("Country", "USA")
    
    geolocator = Nominatim(user_agent="GTA Lookup")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(street + ", " + city + ", " + province + ", " + country)
    
    lat = location.latitude
    lon = location.longitude
    lat_lon = [lat, lon]
    lat_lon_str = str(lat_lon) 
    latitude = st.text_input("Latitude / Longitude", lat_lon_str)
    supplier_asset_lat = lat
    supplier_asset_lon = lon
    st.markdown('')




  colB1, colB2, colB3 = st.beta_columns(3)
  colB1.markdown('')
  colB1.info("Type(s) of Tangible Asset(s)")
  asset_type = colB2.selectbox('Choose one of the below', 
                  ['Buildings', 'Manufacturing Facility ', 'Agricultural', 'Energy & Utilities Infrastructure', 
                   'Transportation Infrastructure', 'Telecoms Infrastructure'], key='asset_type')
  if asset_type == 'Buildings':
      asset_type_building = colB3.selectbox('Choose a Building type', 
                  ['Residential', 'Low/High Rise', 'House of Worship', 'Industrial', 
                   'Data Centers', 'Hospital', 'Hotel', 'Retail', 'Parking'], key = 'asset_type_building')
  elif asset_type == 'Energy & Utilities Infrastructure':
      asset_type_energy = colB3.selectbox('Choose an Infrastructure type', 
                  ['Electricity', 'Water', 'Oil Pipelines', 'Solar/Wind Farms', 'Sewage'], key = 'asset_type_energy') 
  elif asset_type == 'Transportation Infrastructure':
      asset_type_transportation = colB3.selectbox('Choose an Infrastructure type', 
                  ['Roads', 'Bridges', 'Rail', 'Transit Systems', 'Airports'], key = 'asset_type_transportation')       
      
       
  
    
  #Owned Asset Details - from Komal
  st.markdown(" ")  
  st.header("Owned Asset Details")
  
  
  col1,col2,col3=st.beta_columns(3)
  with col1:
    st.info("Type of Asset for Rent")

    asset_for_rent = col1.selectbox('Choose one of the below', 
                  ['Buildings', 'Manufacturing Facility ', 'Agricultural', 
                   'Energy & Utilities Infrastructure', 'Transportation Infrastructure', 'Telecoms Infrastructure'], key='rent')
    if asset_for_rent == 'Buildings':
      asset_rent_building = col1.selectbox('Choose a Building type', 
                  ['Residential', 'Low/High Rise', 'House of Worship', 'Industrial', 
                   'Data Centers', 'Hospital', 'Hotel', 'Retail', 'Parking'], key = 'asset_rent_building')
    elif asset_for_rent == 'Energy & Utilities Infrastructure':
      asset_rent_energy = col1.selectbox('Choose an Infrastructure type', 
                  ['Electricity', 'Water', 'Oil Pipelines', 'Solar/Wind Farms', 'Sewage'], key ='asset_rent_energy') 
    elif asset_for_rent == 'Transportation Infrastructure':
      asset_rent_transportation = col1.selectbox('Choose an Infrastructure type', 
                  ['Roads', 'Bridges', 'Rail', 'Transit Systems', 'Airports'], key = 'asset_rent_transportation') 
    else: col1.selectbox(' ', ['']) 
    

    st.info("Value of Assets for Rent")
    asset1=st.number_input("For Asset 1 (in USD)", value=0,step=100,key='asset1')
    asset2=st.number_input("For Asset 2 (in USD)", value=0,step=100,key='asset2')
    #asset3=st.number_input("For Asset 3 (in USD)", value=0,step=100,key='asset3')    


  with col2:
    st.info("Type of Asset for Sale")
    #asset_for_sale=st.multiselect('Select the Assets',['Land','Building','Machinery','Other Asset'],key='sale')
    asset_for_sale = col2.selectbox('Choose one of the below', 
                  ['Buildings', 'Manufacturing Facility ', 'Agricultural', 'Energy & Utilities Infrastructure', 
                   'Transportation Infrastructure', 'Telecoms Infrastructure'], key='sale')
    if asset_for_sale == 'Buildings':
      col2.selectbox('Choose a Building type', 
                  ['Residential', 'Low/High Rise', 'House of Worship', 'Industrial', 
                   'Data Centers', 'Hospital', 'Hotel', 'Retail', 'Parking'])
    elif asset_for_sale == 'Energy & Utilities Infrastructure':
      col2.selectbox('Choose an Infrastructure type', 
                  ['Electricity', 'Water', 'Oil Pipelines', 'Solar/Wind Farms', 'Sewage']) 
    elif asset_for_sale == 'Transportation Infrastructure':
      col2.selectbox('Choose an Infrastructure type', 
                  ['Roads', 'Bridges', 'Rail', 'Transit Systems', 'Airports']) 
    else: col2.selectbox(' ', ['']) 
    
    st.info("Value of Assets for Sale")
    asset11=st.number_input("For Asset 1 (in USD)", value=0,step=100,key='asset11')
    asset22=st.number_input("For Asset 2 (in USD)", value=0,step=100,key='asset22')
    #asset33=st.number_input("For Asset 3 (in USD)", value=0,step=100,key='asset33')

  with col3:
    st.info("Annual Utility Costs (per asset)")
    a1=st.number_input("For Land (in USD)", value=0,step=100,key='a1')
    a2=st.number_input("For Building (in USD)", value=0,step=100,key='a2')
    a3=st.number_input("For machinery (in USD)", value=0,step=100,key='a3')
    a4=st.number_input("Other Asset(in USD)", value=0,step=100,key='a4')


  st.markdown(" ")
  st.header("Other Information")

  col11,col12,col13=st.beta_columns(3)
  col11.markdown("")
  col11.info("Other Information")
  Carbon_Emission=col12.number_input("Total Annual Carbon Emissions (tons)", value=0)
  Annual_Tax_Benefits=col13.number_input("Annual Tax Benefits Received for FLR (USD)", value=0,step=100)
  


  # Code from Bandhav
  # For Banks/Lenders Only - Bandhav 
  st.header('For Banks/Lenders only')
  cola1, cola2,cola3 = st.beta_columns(3)
  with cola1:
    st.markdown("")
    st.info('Amount of credit risk due to climate risk affected areas')
  with cola2:
    # st.info('Credit risk amount (USD)')
    credit_amount = st.number_input('Credit risk amount (USD)',value=0,step=1000)
  with cola3:
    # st.info('Type of climate risk')
    climate_risk_banks = st.selectbox('Type of climate risk',['Cyclones', 'Hurricanes', 
                         'Drought', 'Wildfires', 'Coastal Flooding','Pluvial Flooding',
                         'Fluvial Flooding', 'Earthquakes', 'Tsunamis', 'Sea Level Rise', 
                         'Chronic Heat Waves', 'Extreme Cold', 'Water Stress'])



  # For Insurers Only (Public & Private Sector) - Bandhav
  st.header('For Insurers only (Public & Private Sector)')
  colb1,colb2,colb3 = st.beta_columns(3)
  with colb1:
    climate_risk_insurers1 = st.selectbox('Type of climate risks',['Cyclones', 'Hurricanes', 
                         'Drought', 'Wildfires', 'Coastal Flooding','Pluvial Flooding',
                         'Fluvial Flooding', 'Earthquakes', 'Tsunamis', 'Sea Level Rise', 
                         'Chronic Heat Waves', 'Extreme Cold', 'Water Stress'], key = 'climate_risk_insurers1')
    climate_risk_insurers2 = st.selectbox('Type of climate risks',['Cyclones', 'Hurricanes', 
                         'Drought', 'Wildfires', 'Coastal Flooding','Pluvial Flooding',
                         'Fluvial Flooding', 'Earthquakes', 'Tsunamis', 'Sea Level Rise', 
                         'Chronic Heat Waves', 'Extreme Cold', 'Water Stress'], key = 'climate_risk_insurers2')
    
    job_loss_insurers = st.number_input('Avg no of job losses due to natural disasters',value=0)
    
  with colb2:
    modelling_loss_insurers1 = st.number_input('Catastrophe modelling expected loss (USD)', value=0, key = 'modelling_loss_insurers1')
    modelling_loss_insurers2 = st.number_input('Catastrophe modelling expected loss (USD)', value=0, key = 'modelling_loss_insurers2')
  #with colb3:
    #job_loss_insurers = st.number_input('Avg no of job losses due to natural disasters',value=0)



  # For Hospital/Hotel Owners Only - Bandhav
  st.header('For Hospitality / Hotel Owners only')
  colc1,colc2,colc3 = st.beta_columns(3)
  with colc1:
    avg_room_rate_hotel = st.number_input('Average Room Rate (USD)', value=0)
    ann_touri_rev_hotel = st.number_input('Annual Tourism Revenue (Past 3 Years)',value=0)
  with colc2:
    avg_rate_view_hotel = st.number_input('Average Room Rate with View (USD)',value=0)
    ann_touri_arr_hotel = st.number_input('Annual no of Tourist Arrivals (Past 3 Years)', value=0)
  with colc3:
    avr_rate_no_view_hotel = st.number_input('Average Room Rate, No View (USD)',value=0)
    rev_loss_natudis_hotel = st.number_input('Revenue Losses due to Natural Disasters', value=0)



  # For Public Investors - Bandhav
  st.header('For Public Investors')
  
  hide_public = st.checkbox("Check box to hide Public Investors section")
  if not hide_public:
  
      cold1,cold2,cold3 = st.beta_columns(3)
      with cold1:
        st.text('')
        st.info('Health')
      with cold2:
        ann_comdis_public = st.number_input('Total Annual Expenditure on Noncommunicable Diseases (USD)',value=0)
        noofdeath_disease = st.number_input('Number of deaths attributable to NCDs, Respiratory Diseases, Pollution, Mental Health',value=0)
        ann_prolos_public = st.number_input('Total Annual National Health Related Productivity Loss (USD)',value=0)
      with cold3:
        ann_resdis_public = st.number_input('Total Annual Expenditure on Respiratory Diseases (USD)',value=0)
        noofdeath_hygiene = st.number_input('Number of deaths attributable to Unsafe Water, Sanitation, Hygeine (per capita)', value=0)
        avg_life_public = st.number_input('Average Life Expectancy',value=0)
    
    
      cole1,cole2,cole3 = st.beta_columns(3)
      with cole1:
        st.text('')
        st.info('Tourism')
      with cole2:
        ann_tour_public1 = st.number_input('Annual Tourism Revenues (Past 3 Years) (USD) Year 1', value=0)
        ann_tour_public2 = st.number_input('Annual Tourism Revenues (Past 3 Years) (USD) Year 2', value=0)
        ann_tour_public3 = st.number_input('Annual Tourism Revenues (Past 3 Years) (USD) Year 3', value=0)
        cur_tousiz_public = st.number_input('Current Tourism Sector Size (USD)',value=0)
      with cole3:
        ann_inttou_public1 = st.number_input('Annual Number of International Tourist Arrivals (Past 3 Years) Year 1',value=0)
        ann_inttou_public2 = st.number_input('Annual Number of International Tourist Arrivals (Past 3 Years) Year 2',value=0)
        ann_inttou_public3 = st.number_input('Annual Number of International Tourist Arrivals (Past 3 Years) Year 3',value=0)
        tour_gdp_public = st.number_input('Tourism Sector as % of GDP (USD)',value=0)
    
    
      colf1,colf2,colf3 = st.beta_columns(3)
      with colf1:
        st.text('')
        st.info('Employment')
      with colf2:
        tot_jobs_public = st.number_input('Total no of Jobs In Forestry and Ecotourism Sectors',value=0)
        labor_prod_public = st.number_input('National Labor Productivity (GDP per hour worked)',value=0)
      with colf3:
        avg_joblos_public = st.number_input('Average no of Job Losses Due to Natural Disasters',value=0)
        tot_incjob_public = st.number_input('Total Earned Income from Jobs in Forestry, Ecotourism (USD)',value=0)
    
    
      colg1,colg2,colg3 = st.beta_columns(3)
      with colg1:
        st.text('')
        st.info('Others')
      with colg2:
        ann_foss_public = st.number_input('Total Annual Fossil Fuel Subsidies (USD)',value=0)
      with colg3:
        ann_acaavg_public = st.number_input('Annual Academic Average',value=0)

  

# # execute the main function  	
# if __name__ == '__main__':
# 	main()