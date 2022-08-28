import streamlit as st
import pandas as pd
import sys
sys.path.append("..")

st.title("User Overview Analysis")

st.sidebar.markdown("""
                    User Analytics in the
                    Telecommunication Industry\n
                    TellCo Customers\' Data
                    """)

st.markdown("The goal of this app is to give an overview of the dataset. It provides a preview of Telecom customers' data aggregated per user, as well as visualization of graphical univariate and bivariate analysis.")

st.header('Dataset Aggregated by User')
df = pd.read_csv('../outcomes/user_overview_analysis.csv')
st.write(df)

st.header('Preliminary Insights')
st.subheader('Top 10 handsets used by the customers')
st.image('../outcomes/top10handsettypes.jpg')

st.subheader('Top 3 Handset Manufacturers')
st.image('../outcomes/top3handsetmanufacturers.jpg')

st.subheader('The top 5 handsets per top 3 handset manufacturer')
st.markdown('1. Top 5 handset made by Apple company')
st.image('../outcomes/topApplehandsets.jpg')
st.markdown('2. Top 5 handset made by Samsung company')
st.image('../outcomes/topSamsunghandsets.jpg')
st.markdown('3. Top 5 handset made by Huawei company')
st.image('../outcomes/topHuaweihandsets.jpg')

st.header('Graphical Univariate Analysis')
st.subheader('Number of Sessions Per User')
st.image('../outcomes/distribution of num of sessions.jpg')


##for multiapp usage
##from multi_app import MultiApp
#import user_overview_analysis #, user_engagement, user_experience, , user_satisfaction # import your app modules here

#app = MultiApp()

#st.sidebar.markdown('# **Tellco Customers Analysis**')
#st.sidebar.markdown("""
#Before investing on a business it is a must to have best understanding about the field. This #project is all about analyzing TellCo's user and find out whether it is worth buying or selling.
#""")

# Add all your application here
#app.add_app("User Overview", user_overview_analysis.app)
#app.add_app("User Engagement", user_engagement.app)
#app.add_app("User Experience", user_experience.app)
#app.add_app("User Satisfaction", user_satisfaction.app)
# The main app
#app.run()