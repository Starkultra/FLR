# -*- coding: utf-8 -*-
"""
Created on Fri May 14 09:43:04 2021

@author: fluec
"""


import streamlit as st
import onetfund_app_page_input, onetfund_app_page_environmental # import your app modules here
import onetfund_app_page_social, onetfund_app_page_economic # import your app modules here
import onetfund_app_page_financial, onetfund_app_page_impact
from PIL import Image
import SessionState


def main():
    st.set_page_config(layout="wide")
    
    
    logo = Image.open('logo_trillion_tree_fund.png')
    c1, c2 = st.beta_columns((1, 6))
    c1.image(logo, width=None)

    page = st.sidebar.radio("Go to page",
        ('Input', 'Impact Overview', 'Financial Statement', 'Economic Statement', 'Social Statement', 'Environmental Statement'))

    state = SessionState.get(amount_investment=50000000)


    if page == 'Input':
        onetfund_app_page_input.main(state)
    elif page == 'Impact Overview':
        #st.markdown("### Impact Overview coming soon")
        onetfund_app_page_impact.main(state)
    elif page == 'Financial Statement':
        onetfund_app_page_financial.main()
        #st.info("Financial impact page coming soon")
    elif page == 'Economic Statement':
        onetfund_app_page_economic.main()
        #st.error("Economic impact page coming soon")
    elif page == 'Social Statement':
        onetfund_app_page_social.main()
        #st.warning("Social impact page coming soon")
    elif page == 'Environmental Statement':    
        #st.success("Environmental impact page coming soon")
        onetfund_app_page_environmental.main()

main()
