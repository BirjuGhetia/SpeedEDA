# Loading Packages for our program
import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sweetviz as sv



# Pandas Function
def pandas(df):
    st.dataframe(df.head())
    profile = ProfileReport(df)
    st_profile_report(profile)


# Sweet Viz Function
def sweetviz(df):
    st.dataframe(df.head())
    if st.button("Generate Sweetviz Report"): #Normal Workflow
      report = sv.analyze(df)
      report.show_html()
      st_display_sweetviz("SWEETVIZ_REPORT.html")


# Loading Random Dataset
def load_data():
        a = pd.DataFrame(
        np.random.rand(100, 5),
        columns = ['a', 'b', 'c', 'd', 'e']
        )
        return a


# Main function
def main():
    # Creating sidebar and Menus
    menu = ["Home", "Pandas Profile", "Sweetviz"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Pandas Profiling Report
    if choice == "Pandas Profile":
        st.subheader("Automated EDA with Pandas Profile")
        # Uploading Dataset
        data_file = st.file_uploader("Upload CSV", type = ['csv'])

        if data_file is not None:
            df = pd.read_csv(data_file)
            pandas(df)
        else :
            st.info('Waiting for CSV file to be uploaded.')
            if st.button('Press to use Example Dataset'): 
              df = load_data()
              pandas(df)
            
        

    # Sweet Viz
    elif choice == "Sweetviz":
        st.subheader("Automated EDA with Sweetviz")
        # Uploading Dataset
        data_file = st.file_uploader("Upload CSV", type = ['csv'])

        if data_file is not None:
            df = pd.read_csv(data_file)
            sweetviz(df)
        else :
            st.info('Waiting for CSV file to be uploaded.')
            if st.button('Press to use Example Dataset'): 
              df = load_data()
              sweetviz(df)

    else :
        # Web App Title
        st.markdown('''
        # **Welcome to Our EDA App**
        This web app performs **Speed EDA** using the **pandas-profiling** and **sweetviz** library.

        Start by opening sidebar and choosing one of the three options available.

        ###### Powered by Streamlit
        *(Support us by visiting https://www.twistblogg.com)*
        
        ###### Developed By:

        ---
        ''')

        html_table= "<table><thead><tr><th>Team</th><th>IDs</th></tr></thead><tfoot><tr><td></td></tr></tfoot><tbody><tr><td>Aman Bhattarai</td><td>500188703</td></tr><tr><td>Birju Ghetia</td><td>500187534</td></tr><tr><td>Charan Chatarasi</td><td>500190019</td></tr><tr><td>Sai Teja Chinthala</td><td>500187171</td></tr> <tr><td>Vishal Naram</td><td>500188508</td></tr></tbody></table>"

        st.markdown(html_table, unsafe_allow_html=True)
      

        
        
        



if __name__ == '__main__':
   main()