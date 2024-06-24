# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go

# def display_tab1(fraud_data):
#     if fraud_data is None or fraud_data.empty:
#         st.error("No data available for plotting.")
#         return

#     tab1_col1, tab1_col2 = st.columns(2)
#     with tab1_col1:
#         # st.markdown('<div class="box">', unsafe_allow_html=True)
#         # st.write('**Weekly Fraudulent Claims**')
#         if 'week' in fraud_data.columns:
#             weekly_fraud_cases = fraud_data.groupby('week')['fraud_cases'].sum().reset_index()
#             fig = px.line(weekly_fraud_cases, x='week', y='fraud_cases', title='Weekly Fraudulent Claims')
#             st.plotly_chart(fig)
#         elif 'month' in fraud_data.columns:
#             monthly_fraud_cases = fraud_data.groupby('month')['fraud_cases'].sum().reset_index()
#             fig = px.line(monthly_fraud_cases, x='month', y='fraud_cases', title='Monthly Fraudulent Claims')
#             st.plotly_chart(fig)
#         elif 'trimester' in fraud_data.columns:
#             trimester_fraud_cases = fraud_data.groupby('trimester')['fraud_cases'].sum().reset_index()
#             fig = px.line(trimester_fraud_cases, x='trimester', y='fraud_cases', title='Trimester Fraudulent Claims')
#             st.plotly_chart(fig)
#         # st.markdown('</div>', unsafe_allow_html=True)

#         # st.markdown('<div class="box">', unsafe_allow_html=True)
#         st.write('**Prejudice of Fraudulent Claims**')
#         if 'week' in fraud_data.columns:
#             weekly_total_cost = fraud_data.groupby('week')['total_cost'].sum().reset_index()
#             fig = px.line(weekly_total_cost, x='week', y='total_cost', labels={'total_cost': 'Prejudice in DZD'})
#             st.plotly_chart(fig)
#         elif 'month' in fraud_data.columns:
#             monthly_total_cost = fraud_data.groupby('month')['total_cost'].sum().reset_index()
#             fig = px.line(monthly_total_cost, x='month', y='total_cost', labels={'total_cost': 'Prejudice in DZD'})
#             st.plotly_chart(fig)
#         elif 'trimester' in fraud_data.columns:
#             trimester_total_cost = fraud_data.groupby('trimester')['total_cost'].sum().reset_index()
#             fig = px.line(trimester_total_cost, x='trimester', y='total_cost',  labels={'total_cost': 'Prejudice in DZD'})
#             st.plotly_chart(fig)
#         # st.markdown('</div>', unsafe_allow_html=True)
#         # st.markdown('<div class="box">', unsafe_allow_html=True)
#         st.write('**Representation of Top 10 Medications Most Susceptible to Fraud**')
#         top_10_num_enr_count = fraud_data[fraud_data['fraud_cases'] > 0]['NUM_ENR'].value_counts().head(10)
#         fig = px.pie(values=top_10_num_enr_count.values, names=top_10_num_enr_count.index)
#         st.plotly_chart(fig)
#         # st.markdown('</div>', unsafe_allow_html=True)
#         # join with medicaments data on num_enr

        

#     with tab1_col2:
#         # st.markdown('<div class="box">', unsafe_allow_html=True)
#         st.write('**Count of Fraudulent Claims per Gender**')
#         gender_counts={
#             'Gender':['Female', 'Male'],
#             'Count':[
#                 fraud_data['female_fraud_cases'].sum(),
#                 fraud_data['male_fraud_cases'].sum()
#                 ]
#         }
#         gender_df = pd.DataFrame(gender_counts)
#         fig=px.bar(gender_df,x='Gender',y='Count',color='Count', labels={'Gender': ' Gender', 'Count': 'Count of fradulent claims'})
#         st.plotly_chart(fig)
#         # st.markdown('</div>', unsafe_allow_html=True)
        
#         # st.markdown('<div class="box">', unsafe_allow_html=True)
#         st.write('**Count of Fraudulent Claims per TS**')
#         fraud_label_count_ts = fraud_data[fraud_data['fraud_cases'] > 0].groupby(['TS_O', 'TS_N']).size().reset_index(name='count')
#         fig = px.bar(fraud_label_count_ts, x='TS_O', y='count', color='TS_N', labels={'TS_O': 'TS'})
#         st.plotly_chart(fig)
#         # st.markdown('</div>', unsafe_allow_html=True)

#         # st.markdown('<div class="box">', unsafe_allow_html=True)
#         st.write('**Count of Fraudulent Claims per Age Group**')
#         fraud_label_count_age = fraud_data[fraud_data['fraud_cases'] > 0].groupby('TRANCHE_AGE_BENEF').size().reset_index(name='count')
#         fig = px.bar(fraud_label_count_age, x='TRANCHE_AGE_BENEF', y='count', color='count')
#         st.plotly_chart(fig)
#         # st.markdown('</div>', unsafe_allow_html=True)

        

# def display_tab2(fraud_data):
#     if fraud_data is None or fraud_data.empty:
#         st.error("No data available for plotting.")
#         return

#     tab2_col1, tab2_col2 = st.columns(2)
#     with tab2_col1:
    
#         # st.markdown('<div class="box">', unsafe_allow_html=True)
#         st.write('**List of Top 10 Medications Most Susceptible to Fraud**')
#         top_10_num_enr = fraud_data[fraud_data['fraud_cases'] == 1]['NOM_DCI'].value_counts().head(10).index.tolist()
#         top_10_num_enr_df = pd.DataFrame({'NOM_DCI': top_10_num_enr})
#         st.dataframe(top_10_num_enr_df)
#         # st.markdown('</div>', unsafe_allow_html=True)
# # def display_tab2(fraud_data, medicaments_data):
# #     if fraud_data is None or fraud_data.empty:
# #         st.error("No data available for plotting.")
# #         return

# #     # Ensure the column names are uppercased for consistency
# #     fraud_data.columns = fraud_data.columns.str.upper()
# #     medicaments_data.columns = medicaments_data.columns.str.upper()

# #     # Print the column names to check if they exist and are correct
# #     st.write("Fraud Data Columns: ", fraud_data.columns)
# #     st.write("Medicaments Data Columns: ", medicaments_data.columns)

# #     # Join fraud_data with medicaments_data on NUM_ENR
# #     fraud_data = fraud_data.merge(medicaments_data, how='left', on='NUM_ENREG')

# #     tab2_col1, tab2_col2 = st.columns(2)
# #     with tab2_col1:
# #         st.markdown('<div class="box">', unsafe_allow_html=True)
# #         st.write('**Representation of Top 10 Medications Most Susceptible to Fraud**')
# #         top_10_num_enr_count = fraud_data[fraud_data['FRAUD_CASES'] > 0]['NUM_ENR'].value_counts().head(10)
# #         top_10_num_enr_labels = fraud_data[fraud_data['NUM_ENR'].isin(top_10_num_enr_count.index)]['NOM_DCI'].unique()
# #         fig = px.pie(values=top_10_num_enr_count.values, names=top_10_num_enr_labels, title='Top 10 Medications Most Susceptible to Fraud')
# #         st.plotly_chart(fig)
# #         st.markdown('</div>', unsafe_allow_html=True)

# #         st.markdown('<div class="box">', unsafe_allow_html=True)
# #         st.write('**List of Top 10 Medications Most Susceptible to Fraud**')
# #         top_10_num_enr = fraud_data[fraud_data['FRAUD_CASES'] > 0]['NUM_ENR'].value_counts().head(10).index.tolist()
# #         top_10_num_enr_df = pd.DataFrame({'NUM_ENR': top_10_num_enr})
# #         top_10_num_enr_df = top_10_num_enr_df.merge(medicaments_data, how='left', on='NUM_ENR')[['NUM_ENR', 'NOM_DCI']]
# #         st.dataframe(top_10_num_enr_df)
# #         st.markdown('</div>', unsafe_allow_html=True)
#     with tab2_col2:
#         # st.markdown('<div class="box">', unsafe_allow_html=True)
#         st.write('**List of Top 10 Most Frequent Pharmacies Susceptible to Fraud**')
#         top_10_code_ps = fraud_data[fraud_data['fraud_cases'] > 0]['CODEPS'].value_counts().head(10).index.tolist()
#         top_10_code_ps_df = pd.DataFrame({'CODEPS': top_10_code_ps})
#         st.dataframe(top_10_code_ps_df)
#         # st.markdown('</div>', unsafe_allow_html=True)
        
#         # st.markdown('<div class="box">', unsafe_allow_html=True)
#         st.write('**Recent Fraudulent Claims**')
#         def apply_color(val):
#             if val == 'fraud':
#                 color = 'red'
#             elif val == 'not fraud':
#                 color = 'green'
#             else:
#                 color = 'yellow'
#             return f'color: {color}'

#         fraud_data['predictions'] = np.where(fraud_data['fraud_cases'] > 0, 'fraud', 'not fraud')
#         styled_data = fraud_data[['ID', 'NUM_ENR', 'NO_DOSSIER_NAT', 'DATE_PAIEMENT', 'QUANTITE_MED', 'CODEPS', 'total_cost', 'predictions']].tail(50).style.applymap(apply_color, subset=['predictions'])
#         st.dataframe(styled_data)
#         # st.markdown('</div>', unsafe_allow_html=True)

# # Example usage of the function
# if __name__ == "__main__":
#     # Replace with actual data loading
#     fraud_data = pd.DataFrame()  # Placeholder for the actual fraud data
#     tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
#     with tab1:
#         display_tab1(fraud_data)
#     with tab2:
#         display_tab2(fraud_data)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
import plotly.express as px
import plotly.graph_objects as go

def plots_css():
    st.markdown(
        """
        <style>
            .chart-container {
                padding: 20px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px; /* Adds space between containers */
                border: 1px solid #e6e6e6;
                width: 100%;
                overflow: hidden;
                position: relative;
            }
            .container-spacing {
                margin-bottom: 20px !important; /* Adds space between containers */
            }
            .dataframe-header {
                background-color: #0072bb;
                color: white;
                font-weight: bold;
            }
            .download-button-container {
                display: flex;
                justify-content: flex-end;
                margin-bottom: 10px;
                position: absolute;
                top: 0;
                right: 0;
            }
            .stDownloadButton {
                padding: 8px 16px;
                border-radius: 5px;
                text-decoration: none;
                text-align: center;
                display: inline-block;
                font-size: 16px;
                margin-left: 10px;
            }
            .stDownloadButton:hover {
                
            }
            .scrollable-container {
                max-height: 500px; /* Adjust the height as needed */
                overflow-y: auto;
                border:...
        """,
        unsafe_allow_html=True,
    )



def display_tab1(fraud_data):
    if fraud_data is None or fraud_data.empty:
        st.error("No data available for plotting.")
        return

    tab1_col1, tab1_col2 = st.columns(2)
    with tab1_col1:
        # st.markdown('<div class="box">', unsafe_allow_html=True)
        # st.write('**Weekly Fraudulent Claims**')
        if 'week' in fraud_data.columns:
            weekly_fraud_cases = fraud_data.groupby('week')['fraud_cases'].sum().reset_index()
            fig = px.line(weekly_fraud_cases, x='week', y='fraud_cases', title='Weekly Fraudulent Claims')
            st.plotly_chart(fig)
        elif 'month' in fraud_data.columns:
            monthly_fraud_cases = fraud_data.groupby('month')['fraud_cases'].sum().reset_index()
            fig = px.line(monthly_fraud_cases, x='month', y='fraud_cases', title='Monthly Fraudulent Claims')
            st.plotly_chart(fig)
        elif 'trimester' in fraud_data.columns:
            trimester_fraud_cases = fraud_data.groupby('trimester')['fraud_cases'].sum().reset_index()
            fig = px.line(trimester_fraud_cases, x='trimester', y='fraud_cases', title='Trimester Fraudulent Claims')
            st.plotly_chart(fig)
        # st.markdown('</div>', unsafe_allow_html=True)

        # st.markdown('<div class="box">', unsafe_allow_html=True)
        # st.write('**Count of Fraudulent Claims per Age Group**')
        fraud_label_count_age = fraud_data[fraud_data['fraud_cases'] > 0].groupby('TRANCHE_AGE_BENEF').size().reset_index(name='count')
        fig = px.bar(fraud_label_count_age, x='TRANCHE_AGE_BENEF', y='count', title='Count of Fraudulent Claims per Age Group', color='count')
        st.plotly_chart(fig)
        # st.markdown('</div>', unsafe_allow_html=True)

                # st.markdown('<div class="box">', unsafe_allow_html=True)
        st.write('**Prejudice of Fraudulent Claims**')
        if 'week' in fraud_data.columns:
            weekly_total_cost = fraud_data.groupby('week')['total_cost'].sum().reset_index()
            fig = px.line(weekly_total_cost, x='week', y='total_cost', labels={'total_cost': 'Prejudice in DZD'})
            st.plotly_chart(fig)
        elif 'month' in fraud_data.columns:
            monthly_total_cost = fraud_data.groupby('month')['total_cost'].sum().reset_index()
            fig = px.line(monthly_total_cost, x='month', y='total_cost', labels={'total_cost': 'Prejudice in DZD'})
            st.plotly_chart(fig)
        elif 'trimester' in fraud_data.columns:
            trimester_total_cost = fraud_data.groupby('trimester')['total_cost'].sum().reset_index()
            fig = px.line(trimester_total_cost, x='trimester', y='total_cost',  labels={'total_cost': 'Prejudice in DZD'})
            st.plotly_chart(fig)
        # st.markdown('</div>', unsafe_allow_html=True)
    with tab1_col2:
        # st.markdown('<div class="box">', unsafe_allow_html=True)
        # Combine the counts from SEXE_F and SEXE_M
        gender_counts = {
            'Gender': ['Female', 'Male'],
            'Count': [
                fraud_data['female_fraud_cases'].sum(),
                fraud_data['male_fraud_cases'].sum()
            ]
        }
        gender_df = pd.DataFrame(gender_counts)
        fig = px.bar(gender_df, x='Gender', y='Count', title='Count of Fraudulent Claims per Gender', color='Count', labels={'Gender': 'Gender'})
        st.plotly_chart(fig)
        # st.markdown('</div>', unsafe_allow_html=True)
        
        
        # st.markdown('<div class="box">', unsafe_allow_html=True)
        # Combine the counts from TS_O and TS_N
        ts_counts = {
            'TS': ['TS_O', 'TS_N'],
            'Count': [
                fraud_data[fraud_data['fraud_cases'] > 0]['TS_O'].sum(),
                fraud_data[fraud_data['fraud_cases'] > 0]['TS_N'].sum()
            ]
        }
        ts_df = pd.DataFrame(ts_counts)
        fig = px.bar(ts_df, x='TS', y='Count', title='Count of Fraudulent Claims per TS', color='Count', labels={'TS': 'TS'})
        st.plotly_chart(fig)
        # st.markdown('</div>', unsafe_allow_html=True)

         # Ensure only rows with fraud cases > 0 are considered
        fraud_data_with_cases = fraud_data[fraud_data['fraud_cases'] > 0]

        # Get the top 10 NUM_ENR by count
        top_10_num_enr_count = fraud_data_with_cases['NUM_ENR'].value_counts().head(10)

        # Get the corresponding nom_dci for the top 10 NUM_ENR
        top_10_num_enr_labels = fraud_data_with_cases[fraud_data_with_cases['NUM_ENR'].isin(top_10_num_enr_count.index)][['NUM_ENR', 'nom_dci']]

        # Ensure unique NUM_ENR to nom_dci mapping
        top_10_num_enr_labels = top_10_num_enr_labels.drop_duplicates(subset=['NUM_ENR'])

        # Reorder the labels to match the counts order
        top_10_num_enr_labels = top_10_num_enr_labels.set_index('NUM_ENR').loc[top_10_num_enr_count.index]['nom_dci']

        # Check lengths of values and names to ensure they match
        assert len(top_10_num_enr_count) == len(top_10_num_enr_labels), "Lengths of values and names do not match!"

        # Create the pie chart
        fig = px.pie(values=top_10_num_enr_count.values, names=top_10_num_enr_labels, title='Top 10 Medications Most Susceptible to Fraud')
        st.plotly_chart(fig)
        fig.update_layout(
            legend=dict(
                orientation="h",  # Horizontal orientation
                yanchor="top",
                y=-0.3,  # Position legend below the chart
                xanchor="center",
                x=0.5
            ),
            margin=dict(l=20, r=20, t=40, b=100)  # Increase bottom margin to fit the legend
        )


# def display_tab2(fraud_data):
#     if fraud_data is None or fraud_data.empty:
#         st.error("No data available for plotting.")
#         return

#     tab2_col1, tab2_col2 = st.columns(2)
#     with tab2_col1:
#         st.markdown('<div class="box">', unsafe_allow_html=True)
#         st.write('**Representation of Top 10 Medications Most Susceptible to Fraud**')
#         top_10_num_enr_count = fraud_data[fraud_data['fraud_cases'] > 0]['NUM_ENR'].value_counts().head(10)
#         fig = px.pie(values=top_10_num_enr_count.values, names=top_10_num_enr_count.index, title='Top 10 Medications Most Susceptible to Fraud')
#         st.plotly_chart(fig)
#         st.markdown('</div>', unsafe_allow_html=True)
#         # join with medicaments data on num_enr


#         st.markdown('<div class="box">', unsafe_allow_html=True)
#         st.write('**List of Top 10 Medications Most Susceptible to Fraud**')
#         top_10_num_enr = fraud_data[fraud_data['fraud_cases'] > 0]['NUM_ENR'].value_counts().head(10).index.tolist()
#         top_10_num_enr_df = pd.DataFrame({'NUM_ENR': top_10_num_enr})
#         st.dataframe(top_10_num_enr_df)

def display_tab2(fraud_data):
    if fraud_data is None or fraud_data.empty:
        st.error("No data available for plotting.")
        return

    tab2_col1, tab2_col2 = st.columns(2)
    with tab2_col1:
        # st.markdown('<div class="box">', unsafe_allow_html=True)
        # st.write('**Representation of Top 10 Medications Most Susceptible to Fraud**')
        # top_10_num_enr_count = fraud_data[fraud_data['fraud_cases'] ==1]['NUM_ENR'].value_counts().head(10)
        # top_10_num_enr_labels = fraud_data[fraud_data['NUM_ENR'].isin(top_10_num_enr_count.index)]['nom_dci'].unique()
        # fig = px.pie(values=top_10_num_enr_count.values, names=top_10_num_enr_labels, title='Top 10 Medications Most Susceptible to Fraud')
        # st.plotly_chart(fig)
        # st.markdown('</div>', unsafe_allow_html=True)

       

        # st.markdown('<div class="box">', unsafe_allow_html=True)
        st.write('**List of Top 10 Medications Most Susceptible to Fraud**')
        top_10_num_enr = fraud_data[fraud_data['fraud_cases'] ==1]['NUM_ENR'].value_counts().head(10).index.tolist()
        top_10_num_enr_df = fraud_data[fraud_data['NUM_ENR'].isin(top_10_num_enr)][['NUM_ENR', 'nom_dci']].drop_duplicates()
        st.dataframe(top_10_num_enr_df)
        # st.markdown('</div>', unsafe_allow_html=True)
        
        # st.markdown('<div class="box">', unsafe_allow_html=True)
        st.write('**List of Top 10 Most Frequent Pharmacies Susceptible to Fraud**')
        top_10_code_ps = fraud_data[fraud_data['fraud_cases'] == 1]['CODEPS'].value_counts().head(10).reset_index()
        top_10_code_ps.columns = ['CODEPS', 'count']
        st.dataframe(top_10_code_ps)

    with tab2_col2:
        # st.markdown('<div class="box">', unsafe_allow_html=True)
        st.write('**Recent Fraudulent Claims**')
        
        def apply_color(val):
            if val == 'fraud':
                color = 'red'
            elif val == 'suspicious':
                color = 'yellow'
            elif val == 'not fraud':
                color = 'green'
            else:
                color = 'gray'
            return f'color: {color}'

        fraud_data['predictions'] = np.select(
            [fraud_data['predictions'] == 1, fraud_data['predictions'] == 2, fraud_data['predictions'] == 0],
            ['fraud', 'suspicious', 'not fraud'],
            default='unknown'
        )
        
        styled_data = fraud_data[fraud_data['predictions'] == 'fraud'][['ID', 'NUM_ENR', 'NO_DOSSIER_NAT', 'DATE_PAIEMENT', 'QUANTITE_MED', 'CODEPS',  'total_cost', 'predictions']].tail(50).style.applymap(apply_color, subset=['predictions'])
        st.dataframe(styled_data)
        # st.markdown('</div>', unsafe_allow_html=True)

        

        # st.write('**Pie Chart of Top 10 Most Frequent Pharmacies Susceptible to Fraud**')
        # fig = px.pie(top_10_code_ps, values='count', names='CODEPS')
        # st.plotly_chart(fig)
        # # st.markdown('</div>', unsafe_allow_html=True)
        def generate_random_coordinates(n, lat_bounds=(36, 36.8), lon_bounds=(6.5, 6.9)):
            latitudes = np.random.uniform(lat_bounds[0], lat_bounds[1], n)
            longitudes = np.random.uniform(lon_bounds[0], lon_bounds[1], n)
            return latitudes, longitudes

        def display_pharmacies_map(top_10_code_ps):
            # Generate random coordinates
            latitudes, longitudes = generate_random_coordinates(len(top_10_code_ps))

            # Add coordinates to the DataFrame
            top_10_code_ps['Latitude'] = latitudes
            top_10_code_ps['Longitude'] = longitudes

            # Create a scatter map
            fig = px.scatter_mapbox(top_10_code_ps, lat="Latitude", lon="Longitude", hover_name="CODEPS", hover_data=["count"],
                                    color_discrete_sequence=["blue"], zoom=5, height=300)
            fig.update_layout(mapbox_style="open-street-map", mapbox_center_lat=28, mapbox_center_lon=3)
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(fig)


        # Display map visualization
        st.write('**Map of Top 10 Most Frequent Pharmacies Susceptible to Fraud**')
        display_pharmacies_map(top_10_code_ps)


def display_tab3(fraud_data):
    if fraud_data is None or fraud_data.empty:
        st.error("No data available for the blacklist.")
        return

    # # Apply CSS for chart containers
    # plots_css()

    # st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.write('### Blacklist - Suspicious and Fraudulent Cases')

    # Filter fraud data for blacklisted individuals (predictions = 'fraud' or 'suspicious')
    blacklist_data = fraud_data[(fraud_data['predictions'] == 'fraud') | (fraud_data['predictions'] == 'suspicious')]

    if blacklist_data.empty:
        st.warning("No suspicious or fraudulent cases found.")
        return

    # Select only the necessary columns
    blacklist_columns = ['ID', 'NUM_ENR', 'NO_DOSSIER_NAT', 'DATE_PAIEMENT', 'TRANCHE_AGE_BENEF', 'C80', 'C17', 'QUANTITE_MED', 'total_cost', 'predictions']
    blacklist_data = blacklist_data[blacklist_columns]

    # Search functionality
    search_term = st.text_input("Search Blacklist", value="")

    if search_term:
        filtered_data = blacklist_data[
            blacklist_data.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        ]
    else:
        filtered_data = blacklist_data
    
        # st.markdown('<div class="scrollable-container">', unsafe_allow_html=True)
        styled_filtered_data = filtered_data.style.set_table_styles(
            [{'selector': 'th', 'props': [('background-color', '#0072bb'), ('color', 'white'), ('font-weight', 'bold')]}]
        )
        st.dataframe(styled_filtered_data)
        # st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="download-button-container">', unsafe_allow_html=True)
    st.download_button(
            label="Download data as CSV",
            data=filtered_data.to_csv(index=False).encode('utf-8'),
            file_name='blacklist_data.csv',
            mime='text/csv',
        )
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("### Detailed Information")
    # Display detailed view of selected individual
    selected_id = st.selectbox("Select an individual ID for more details", filtered_data['ID'].unique())
    selected_data = filtered_data[filtered_data['ID'] == selected_id]

    if not selected_data.empty:
        # Calculate total cost and quantity for the selected ID
        total_cost = fraud_data[fraud_data['ID'] == selected_id]['total_cost'].sum()
        total_quantity = fraud_data[fraud_data['ID'] == selected_id]['QUANTITE_MED'].sum()
        # Find the last date of payment
        last_payment_date = fraud_data[fraud_data['ID'] == selected_id]['DATE_PAIEMENT'].max()

        
        st.write("#### Personal Information")
        st.write(f"**ID:** {selected_data.iloc[0]['ID']}")
        st.write(f"**Date of his First Payment:** {selected_data.iloc[0]['DATE_PAIEMENT']}")
        st.write(f"**Date of his Last Payment:** {last_payment_date}")
        st.write(f"**Age Group:** {selected_data.iloc[0]['TRANCHE_AGE_BENEF']}")
        st.write(f"**Chronic Disease C80:** {'Yes' if selected_data.iloc[0]['C80'] == 1 else 'No'}")
        st.write(f"**Chronic Disease C17:** {'Yes' if selected_data.iloc[0]['C17'] == 1 else 'No'}")
        
        st.write("#### Fraud Information")
        st.write(f"**Total Cost:** {total_cost}")
        st.write(f"**Quantity of Medication:** {total_quantity}")
        st.write(f"**Fraud Type:** {'Fraud' if selected_data.iloc[0]['predictions'] == 'fraud' else 'Suspicious'}")
        st.write("#### Transactions")
        # Filter the main DataFrame to get transactions for the selected ID
        transactions = fraud_data[fraud_data['ID'] == selected_id][['DATE_PAIEMENT', 'NUM_ENR', 'NO_DOSSIER_NAT', 'QUANTITE_MED', 'total_cost','predictions']]
        styled_transactions = transactions.style.set_table_styles(
            [{'selector': 'th', 'props': [('background-color', '#0072bb'), ('color', 'white'), ('font-weight', 'bold')]}]
        )
        st.dataframe(styled_transactions)
    
    # st.markdown('</div>', unsafe_allow_html=True)

