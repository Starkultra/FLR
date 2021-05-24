import streamlit as st
import pandas as pd
import plotly.express as px
#import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt



def main(state):
    # make dataframe for treemap
    category = ['Economic', 'Economic', 'Economic', 'Economic', 'Economic', 'Economic',
                'Envirnonmental','Envirnonmental','Envirnonmental','Envirnonmental','Envirnonmental',
                'Financial', 'Financial','Financial', 'Financial', 'Financial', 'Financial',
                'Social', 'Social', 'Social', 'Social', 'Social']
    name = ['Jobs', 'Business Disruptions ($)', 
            'GDP ($ or %)', 'Annual Fossil Fuel <br>Subsidy Reduction ($)', 
            'Labour Productivity / <br>Temperature Change (hrs)','Tourism (% of GDP)',
            'Carbon Sequestered (tons)', 'Soil Erosion Rate', 
            'Waste of Water <br> Filtration Value ($)', 'Ecosystem Services <br>Vulnerability',
            'Water  Vulnerability',
            'Damages ($)', 'Tourism Revenue ($ %)', 'Credit Risk ($)', 
            'Property Value ($)', 'Tax Benefits ($)', 'Business Disruptions ($)',
            'Public Health <br>Expenditure ($)', 'Public Health <br>Vulnerability',
            'Food Vulnerability', 'Health Related <br>Productivity Loss',
            'Cost of Carbon ($)']
    amount = [100, 100, 100, 100, 100, 100,
              120, 120, 120, 120, 120, 
              100, 100, 100, 100, 100, 100, 
              120, 120, 120, 120, 120]
    
    df = pd.DataFrame(dict(category=category, name=name,  amount=amount))
    df["Impact Overview"] = "Impact Overview" # in order to have a single root node

    # make dataframe for Total Investment Value plot
    df_graph = pd.DataFrame({ 
                       'Year': [2021,2026,2031,2036,2041,2046,2051],
                       'USD': [10000, 25000, 40000,75000,98000,110111,150000]})


    st.header("Impact Overview")
    
    colA1, colA2 = st.beta_columns([1,2])
    with colA1: 
        st.write(" ")
        st.write(" ")
        st.write("### Total Investment Value")


        fig, ax = plt.subplots()
        ax=sns.lineplot(x='Year', y='USD', data=df_graph, color='red',linewidth=2.5)
        ax.set_ylabel("USD")
        st.pyplot(fig)
        
        
    
        st.markdown(f"Amount Invested in Forest Landscape Restoration: ${state.amount_investment}M")
        total_investment = 1600000000000
        ti = total_investment/1000000000000
        st.markdown(f"Total Expected Value of Investment by 2050: ${ti}TR")
        annualized_roi = 5
        st.write(f"Annualized ROI: {annualized_roi}%")
        total_roi = 50
        st.write(f"Total ROI: {total_roi}%")

        
        st.write("### Selected Risks")
        st.write("Cyclones")
        st.write("Hurricanes")
        st.write("Drought")
        st.write("Wildfires")
        st.write("Coastal Flooding")
        st.write("Pluvial Flooding")
        st.write("Fluvial Flooding")
        st.write("Earthquakes")
        st.write("Tsunamis")
        st.write("Sea Level Rise")
        st.write("Chronic Heat Waves")
        st.write("Extreme Cold")
        st.write("Water Stress")
        
        
    with colA2:
        fig = px.treemap(df, path=['Impact Overview', 'category', 'name'], values='amount', 
                         color='category',color_discrete_map={'(?)':'white', 
                         'Envirnonmental':'#3a9385', 'Financial':'#a1d7d4', 
                         'Economic':'#082c3c', 'Social':'#d9c161'},  height=1000)
        fig.update_layout(font=dict(size=14,color="white"))
        st.plotly_chart(fig, use_container_width=True)


    
    
# if __name__ == '__main__':
# 	main()     
