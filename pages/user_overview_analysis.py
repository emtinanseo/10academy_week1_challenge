import streamlit as st
import pandas as pd

def app():
    st.title('User Overview Analysis')

    st.markdown('**This is the `User Overview` of this the user analysis multi page.**')

    st.markdown('**In this app, we will see the data and some visualization of user engagement.**')

    df = pd.read_csv('../outcomes/user_overview_data.csv')
    st.write(df)
    st.title('Top 10 handsets used by the customers')
    st.image('../outcomes/top10handsettypes.jpg')
    st.title('Top 3 manufacturers that provide handset to the users')
    st.image('../outcomes/top3handsetmanufacturers.jpg')
    st.title('Top 10 handset made by Apple company')
    st.image('../outcomes/topApplehandsets.jpg')
    st.title('Top 10 handset made by Huawei company')
    st.image('../outcomes/topHuaweihandsets.jpg')
    st.title('Top 10 handset made by Samsung company')
    st.image('../outcomes/topSamsunghandsets.jpg')
