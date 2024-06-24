# import streamlit as st
# from config import setup_page
# from data import load_fraud_data
# from auth import login
# from sidebar import setup_sidebar, setup_admin_sidebar
# from kpi_display import display_kpis
# from plots import display_tab1, display_tab2
# import admin_dashboard
# setup_page()
# if login():
#     st.title('📊 CNAS Fraud/Abuse Detection in Medication Consumption Dashboard')
    
#     # Check user role and display the appropriate dashboard
#     if st.session_state['role'] in ['Data Analyst']:
#         # Setup sidebar and get the selected filter type and filters
#         filter_type, month, trimester, start_date, end_date = setup_sidebar()
        
#         # Load the data based on the selected filters
#         fraud_data = load_fraud_data(filter_type, month=month, trimester=trimester, start_date=start_date, end_date=end_date)
        
#         if fraud_data is not None and not fraud_data.empty:
#             print(fraud_data.columns)  # Log the columns of the loaded data
#             print(fraud_data.head())   # Log the first few rows of the loaded data
            
#             # Placeholder for the KPIs
#             placeholder = st.empty()
#             with placeholder.container():
#                 display_kpis(fraud_data)

#             # Horizontal line to separate the KPIs from the rest of the content
#             st.markdown('---')

#             # Define tabs
#             tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

#             # Tab 1 content
#             with tab1:
#                 display_tab1(fraud_data)

#             # Tab 2 content
#             with tab2:
#                 display_tab2(fraud_data)
#         else:
#             st.error("Failed to load data. Please check your database connection or query.")
#             print("Failed to load data. Please check your database connection or query.")
#     elif st.session_state['role'] == 'Admin':
#         # Setup the admin sidebar
#         setup_admin_sidebar()
        
#         # Display the admin dashboard
#         with admin_dashboard.DatabaseConnection(
#             host='localhost',
#             user='postgres',
#             password='SQLAKILA111',
#             database='CNAS'
#         ) as db:
#             admin_dashboard.display_admin_dashboard(db.cursor, db.conn)
#     else:
#         st.error("You do not have permission to view this dashboard.")

import streamlit as st
from config import setup_page
from data import load_fraud_data
from auth import login
from sidebar import setup_sidebar, setup_admin_sidebar,setup_mlops_sidebar
from kpi_display import display_kpis
from plots import display_tab1, display_tab2, display_tab3
import admin_dashboard
from monitoring import display_monitoring_page

setup_page()

if login():
    st.markdown("""
        <style>
            .main-title {
                font-size: 2.5em;
                color: #0477BF;
                text-align: left;
                margin-top: 20px;
            }
            .kpi-container {
                display: flex;
                justify-content: space-around;
                margin: 20px 0;
                gap: 20px;  /* Add gap between cards */
            }
            .kpi-card {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
                flex: 1;  /* Distribute the space equally among cards */
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                max-width: 200px;  /* Set a maximum width for the cards */
                border: 2px solid #f0f0f0;
            }
            .kpi-label {
                font-size: 1.2em;
                color: #333;
                margin-top: 5px;
            }
            
             .kpi-value {
                font-size: 2em;
                color: #0477BF;
                font-weight: bold;
                max-width: 100%;  /* Add this line to limit the width of the value */
                overflow: hidden;  /* Add this line to hide any overflowing content */
                text-overflow: ellipsis;  /* Add this line to show ellipsis for overflowing content */
                white-space: nowrap;  /* Add this line to prevent wrapping of the value */
            }
            .kpi-card:hover .tooltip {
                visibility: visible;
                opacity: 1;
            }
            .tooltip {
                visibility: hidden;
                background-color: #555;
                color: #fff;
                text-align: center;
                border-radius: 6px;
                padding: 5px;
                position: absolute;
                z-index: 1;
                bottom: 125%;  /* Position the tooltip above the text */
                left: 50%;
                margin-left: -60px;
                opacity: 0;
                transition: opacity 0.3s;
                width: 120px;
                word-wrap: break-word;
            }
            .tooltip::after {
                content: "";
                position: absolute;
                top: 100%;  /* At the bottom of the tooltip */
                left: 50%;
                margin-left: -5px;
                border-width: 5px;
                border-style: solid;
                border-color: #555 transparent transparent transparent;
            }
            .tab-content {
                padding: 20px;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
            }
             .box {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                border: 2px solid #f0f0f0;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-title">📊 CNAS Fraud/Abuse Detection in Medication Consumption Dashboard</h1>', unsafe_allow_html=True)
    
    # Check user role and display the appropriate dashboard
    if st.session_state['role'] in ['Data Analyst']:
        # Setup sidebar and get the selected filter type and filters
        filter_type, month, trimester, start_date, end_date = setup_sidebar()
        
        # Load the data based on the selected filters
        fraud_data = load_fraud_data(filter_type, month=month, trimester=trimester, start_date=start_date, end_date=end_date)
        # medicaments_data= load_medicaments_data()
        
        if fraud_data is not None and not fraud_data.empty:
            # print(fraud_data.columns)  # Log the columns of the loaded data
            # print(fraud_data.head())   # Log the first few rows of the loaded data
            
            # Placeholder for the KPIs
            placeholder = st.empty()
            with placeholder.container():
                display_kpis(fraud_data)

            # Horizontal line to separate the KPIs from the rest of the content
            st.markdown('---')

            # Define tabs
            tab1, tab2, tab3 = st.tabs(["Overview", "Detailed view","Black list Management"])

            # Tab 1 content
            with tab1:
                # st.html('<div class="tab-content">')
                display_tab1(fraud_data)
                # st.html('</div>')

            # Tab 2 content
            with tab2:
                # st.markdown('<div class="tab-content">', unsafe_allow_html=True)
                display_tab2(fraud_data)
                # st.markdown('</div>', unsafe_allow_html=True)
            with tab3:
                display_tab3(fraud_data)
        else:
            st.error("Failed to load data. Please check your database connection or query.")
            print("Failed to load data. Please check your database connection or query.")
    elif st.session_state['role'] == 'Admin':
        # Setup the admin sidebar
        setup_admin_sidebar()
        
        # Display the admin dashboard
        with admin_dashboard.DatabaseConnection(
            host='localhost',
            user='postgres',
            password='SQLAKILA111',
            database='CNAS'
        ) as db:
            admin_dashboard.display_admin_dashboard(db.cursor, db.conn)
    elif st.session_state['role'] == 'MLOps Eng':
        # Setup the admin sidebar
        # setup_mlops_sidebar()
        selected_model=setup_mlops_sidebar()
        display_monitoring_page(selected_model)
    else:
        st.error("You do not have permission to view this dashboard.")