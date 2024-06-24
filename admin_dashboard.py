# import streamlit as st
# import psycopg2
# from datetime import datetime
# import pandas as pd
# import time

# # Context manager for database connection
# class DatabaseConnection:
#     def __init__(self, host, user, password, database):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.database = database
#         self.conn = None
#         self.cursor = None

#     def __enter__(self):
#         self.conn = psycopg2.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database
#         )
#         self.cursor = self.conn.cursor()
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.cursor.close()
#         self.conn.close()

# # Fetch all users and return as a DataFrame
# def fetch_all_users_df(cursor):
#     cursor.execute("SELECT username, role, date_created, email, phone FROM credentials")
#     rows = cursor.fetchall()
#     df = pd.DataFrame(rows, columns=['Username', 'Role', 'Date Created', 'Email', 'Phone'])
#     df.index += 0  # Adjust index to start from 0
#     df.reset_index(inplace=True)
#     df.rename(columns={'index': '#'}, inplace=True)
#     return df

# # Function to add a new user
# def add_user(cursor, conn, username, password, role, email, phone):
#     cursor.execute("INSERT INTO credentials (username, password, role, date_created, email, phone) VALUES (%s, %s, %s, NOW(), %s, %s)", (username, password, role, email, phone))
#     conn.commit()

# # Function to delete a user
# def delete_user(cursor, conn, username):
#     cursor.execute("DELETE FROM credentials WHERE username=%s", (username,))
#     conn.commit()
# def fetch_active_sessions_count(cursor):
#     cursor.execute("SELECT COUNT(*) FROM sessions WHERE is_active = TRUE")
#     return cursor.fetchone()[0]
# # Function to update a user's details
# def update_user_details(cursor, conn, old_username, new_username, new_role, email, phone):
#     cursor.execute("UPDATE credentials SET username=%s, role=%s, email=%s, phone=%s WHERE username=%s", (new_username, new_role, email, phone, old_username))
#     conn.commit()

# def display_admin_dashboard(cursor, conn):
#     st.markdown("""
#         <style>
#         table {
#             width: 100%;
#             border-collapse: collapse;
#         }
#         th {
#             background-color: #0072bb;
#             color: white;
#             border: 3px solid black;
#             padding: 6px;
#             text-align: left;
#         }
#         td {
#             border: 3px solid black;
#             padding: 6px;
#             text-align: left;
#         }
#         .action-buttons {
#             display: flex;
#             gap: 10px;
#             font-weight: bold;
#         }
#         .action-button {
#             background-color: white;
#             color: black;
#             font-weight: bold;
#             border: 1px solid #ddd;
#             padding: 5px;
#             cursor: pointer;
#             font-size: 12px;
#             width: 32px;
#             height: 32px;
#             border-radius: 50%; /* Rounded corners */
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Shadow effect */
#             transition: background-color 0.3s, transform 0.3s; /* Smooth transition */
#         }
#         .action-button:hover {
#             background-color: #f0f0f0;
#             transform: translateY(-2px); /* Slight lift on hover */
#         }
#         .form-container {
#             margin-top: 20px; /* Add gap between form and table */
#             padding: 20px;
#             border: 1px solid #ddd;
#             border-radius: 10px;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#             background-color: #f9f9f9;
#         }
#         .form-container h2 {
#             margin-bottom: 20px;
#         }
#         .form-container .form-field {
#             display: flex;
#             align-items: center;
#             margin-bottom: 15px;
#         }
#         .form-container .form-field i {
#             margin-right: 10px;
#             color: #0072bb;
#         }
#         .form-container .form-field input,
#         .form-container .form-field select {
#             flex: 1;
#             padding: 10px;
#             border: 1px solid #ddd;
#             border-radius: 5px;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#         <head>
#             <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
#         </head>
#         <style>
#         .big-font {
#             font-size:40px !important;
#         }
#         .icon-header {
#             font-size:24px !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     st.markdown('<h1 class="big-font"><i class="fas fa-shield-alt"></i> Admin Dashboard</h1>', unsafe_allow_html=True)
    

    
#     tab1, tab2, tab3, tab4, tab5, tab6 =st.tabs(["User Management", "System Settings", "Notifications and Alerts", "Additional Configuration Options", "High-Level KPIs","Add user"])
#     with tab1:
     
    
#         st.header("User Management")
#         # Fetch and display users
#         st.markdown('<h2 class="icon-header">User Management</h2>', unsafe_allow_html=True)

#         # Add CRUD buttons
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             if st.button('Add New User'):
#                 st.session_state.show_add_user_form = True
#                 st.session_state.show_update_delete_form = None
#         with col2:
#             if st.button('Update User'):
#                 st.session_state.show_update_delete_form = 'update'
#                 st.session_state.show_add_user_form = False
#         with col3:
#             if st.button('Delete User'):
#                 st.session_state.show_update_delete_form = 'delete'
#                 st.session_state.show_add_user_form = False
#         df = fetch_all_users_df(cursor)
        
#         if st.session_state.get('show_update_delete_form', None):
#             selected_indices = st.multiselect("Select rows to update/delete:", df.index)

#             html_table = df.to_html(index=False, classes='dataframe')
#             st.markdown(html_table, unsafe_allow_html=True)

#             role_options = ["Admin", "Data Analyst", "MLOps Eng", "Médecin Chef"]

#             # Add user form
#         if st.session_state.get('show_add_user_form', False):
#             st.markdown('<div class="form-container">', unsafe_allow_html=True)
#             with st.form(key='add_user_form'):
#                 st.write("Add New User")
#                 new_username = st.text_input("New Username", key='new_username')
#                 new_password = st.text_input("New Password", type="password", key='new_password')
#                 new_role = st.selectbox("New Role", role_options, key='new_role')
#                 new_email = st.text_input("Email", key='new_email')
#                 new_phone = st.text_input("Phone", key='new_phone')
#                 add_user_button = st.form_submit_button("Add User")
#                 if add_user_button:
#                     if new_username and new_password:
#                         add_user(cursor, conn, new_username, new_password, new_role, new_email, new_phone)
#                         st.success(f"User {new_username} added successfully")
#                         st.session_state.show_add_user_form = False  # Hide the form
#                         time.sleep(1)  # Keep the success message for 1 seconds
#                         st.experimental_rerun()
#                     else:
#                         st.error("Username and password cannot be empty")
#             st.markdown('</div>', unsafe_allow_html=True)

#         # Update user form
#         if st.session_state.get('show_update_delete_form', None) == 'update':
#             if selected_indices:
#                 for idx in selected_indices:
#                     selected_user = df.iloc[idx]
#                     st.markdown('<div class="form-container">', unsafe_allow_html=True)
#                     with st.form(key=f'update_user_form_{idx}'):
#                         st.write(f"Update User: {selected_user['Username']}")
#                         new_username = st.text_input("Username", value=selected_user['Username'], key=f"new_username_{idx}")
#                         new_role = st.selectbox("New Role", role_options, index=role_options.index(selected_user['Role']), key=f"new_role_{idx}")
#                         new_email = st.text_input("Email", value=selected_user['Email'], key=f"new_email_{idx}")
#                         new_phone = st.text_input("Phone", value=selected_user['Phone'], key=f"new_phone_{idx}")
#                         update_user_button = st.form_submit_button("Update User")
#                         if update_user_button:
#                             update_user_details(cursor, conn, selected_user['Username'], new_username, new_role, new_email, new_phone)
#                             success_placeholder = st.empty()
#                             success_placeholder.success(f"User {new_username}'s details updated successfully")
#                             st.session_state.show_update_delete_form = None  # Hide the form
#                             time.sleep(1)  # Keep the success message for 1 seconds
#                             success_placeholder.empty()
#                             st.experimental_rerun()
#                     st.markdown('</div>', unsafe_allow_html=True)

#         # Delete user form
#         if st.session_state.get('show_update_delete_form', None) == 'delete':
#             if selected_indices:
#                 for idx in selected_indices:
#                     selected_user = df.iloc[idx]
#                     if st.button(f"Confirm Deletion of {selected_user['Username']}", key=f'delete_{idx}'):
#                         delete_user(cursor, conn, selected_user['Username'])
#                         success_placeholder = st.empty()
#                         success_placeholder.success(f"User {selected_user['Username']} deleted successfully")
#                         st.session_state.show_update_delete_form = None  # Hide the form
#                         time.sleep(1)  # Keep the success message for 1 seconds
#                         success_placeholder.empty()
#                         st.experimental_rerun()

        
#     with tab2:
#         # System Settings Section
#         st.subheader("System Settings")
#         st.text("Configure application settings here.")
#         # Add your system settings controls here
#     with tab3:
#         # Notifications and Alerts Section
#         st.subheader("Settings for Notifications and Alerts")
#         st.text("Configure notifications and alert settings here.")
#         # Add your notifications and alerts controls here
#     with tab4:
#         # Additional Configuration Options Section
#         st.subheader("Additional Configuration Options")
#         st.text("Additional configuration options here.")
#         # Add your additional configuration options here
#     with tab5:
#         # High-Level KPIs Section
#         st.subheader("High-Level KPIs")
#         st.text("Overview of key performance indicators.")
#         st.metric(label="Total Users", value=len(df))
    
#         # active_sessions = fetch_active_sessions_count(cursor)
#         # st.metric(label="Active Sessions", value=active_sessions)  # Use real data
        
#         # st.metric(label="System Uptime", value="99.9%")
#     with tab6:
#             st.subheader("Add user")
#             # # Add button for adding new user
#             # if st.button('Add New User', key="add_user_button", help="Add new user"):
#             st.session_state.show_add_user_form = True
#             if st.session_state.get('show_add_user_form', False):
#                 with st.form(key='add_user_form'):
#                     st.write("Add New User")
#                     new_username = st.text_input("Username")
#                     new_password = st.text_input("Password", type="password")
#                     new_role = st.selectbox("Role", role_options)
#                     add_user_button = st.form_submit_button("Add User")
#                     if add_user_button:
#                         if new_username and new_password:
#                             add_user(cursor, conn, new_username, new_password, new_role)
#                             st.success(f"User {new_username} added successfully")
#                             st.experimental_rerun()
#                             #clear form once the new user is added
#                             st.session_state.show_add_user_form = False
#                         else:
#                             st.error("Username and password cannot be empty")
                    



# # Main execution
# if __name__ == "__main__":
#     with DatabaseConnection(host='localhost', user='postgres', password='SQLAKILA111', database='CNAS') as db:
#         display_admin_dashboard(db.cursor, db.conn)

import streamlit as st
import psycopg2
import pandas as pd
from datetime import datetime
import time

# Context manager for database connection
class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conn.close()

# Fetch all users and return as a DataFrame
def fetch_all_users_df(cursor):
    cursor.execute("SELECT username, role, date_created, email, phone FROM credentials")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['Username', 'Role', 'Date Created', 'Email', 'Phone'])
    df.index += 0  # Adjust index to start from 0
    df.reset_index(inplace=True)
    df.rename(columns={'index': '#'}, inplace=True)
    return df

# Function to add a new user
def add_user(cursor, conn, username, password, role, email, phone):
    cursor.execute("INSERT INTO credentials (username, password, role, date_created, email, phone) VALUES (%s, %s, %s, NOW(), %s, %s)", (username, password, role, email, phone))
    conn.commit()

# Function to delete a user
def delete_user(cursor, conn, username):
    cursor.execute("DELETE FROM credentials WHERE username=%s", (username,))
    conn.commit()
def fetch_active_sessions_count(cursor):
    cursor.execute("SELECT COUNT(*) FROM sessions WHERE is_active = TRUE")
    return cursor.fetchone()[0]
# Function to update a user's details
def update_user_details(cursor, conn, old_username, new_username, new_role, email, phone):
    cursor.execute("UPDATE credentials SET username=%s, role=%s, email=%s, phone=%s WHERE username=%s", (new_username, new_role, email, phone, old_username))
    conn.commit()

def display_admin_dashboard(cursor, conn):
    st.markdown("""
        <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th {
            background-color: #0072bb;
            color: white;
            border: 3px solid black;
            padding: 6px;
            text-align: left;
        }
        td {
            border: 3px solid black;
            padding: 6px;
            text-align: left;
        }
        .action-buttons {
            display: flex;
            gap: 10px;
            font-weight: bold;
        }
        .action-button {
            background-color: white;
            color: black;
            font-weight: bold;
            border: 1px solid #ddd;
            padding: 5px;
            cursor: pointer;
            font-size: 12px;
            width: 32px;
            height: 32px;
            border-radius: 50%; /* Rounded corners */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Shadow effect */
            transition: background-color 0.3s, transform 0.3s; /* Smooth transition */
        }
        .action-button:hover {
            background-color: #f0f0f0;
            transform: translateY(-2px); /* Slight lift on hover */
        }
        .form-container {
            margin-top: 20px; /* Add gap between form and table */
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            background-color: #f9f9f9;
        }
        .form-container h2 {
            margin-bottom: 20px;
        }
        .form-container .form-field {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }
        .form-container .form-field i {
            margin-right: 10px;
            color: #0072bb;
        }
        .form-container .form-field input,
        .form-container .form-field select {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        </head>
        <style>
        .big-font {
            font-size:40px !important;
        }
        .icon-header {
            font-size:24px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="big-font"><i class="fas fa-shield-alt"></i> Admin Dashboard</h1>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5 =st.tabs(["User Management", "System Settings", "Notifications and Alerts", "Additional Configuration Options", "High-Level KPIs"])
    with tab1:
        st.markdown('<h2 class="icon-header">User Management</h2>', unsafe_allow_html=True)

        # Add CRUD buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button('Add New User'):
                st.session_state.show_add_user_form = True
                st.session_state.show_update_delete_form = None
        with col2:
            if st.button('Update User'):
                st.session_state.show_update_delete_form = 'update'
                st.session_state.show_add_user_form = False
        with col3:
            if st.button('Delete User'):
                st.session_state.show_update_delete_form = 'delete'
                st.session_state.show_add_user_form = False

        # Fetch and display users
        df = fetch_all_users_df(cursor)
        
        if st.session_state.get('show_update_delete_form', None):
            selected_indices = st.multiselect("Select rows to update/delete:", df.index)

        html_table = df.to_html(index=False, classes='dataframe')
        st.markdown(html_table, unsafe_allow_html=True)

        role_options = ["Admin", "Data Analyst", "MLOps Eng", "Médecin Chef"]

        # Add user form
        if st.session_state.get('show_add_user_form', False):
            st.markdown('---')
            # st.markdown('<div class="form-container">', unsafe_allow_html=True)
            with st.form(key='add_user_form'):
                st.write("Add New User")
                new_username = st.text_input("Username", key='new_username')
                new_password = st.text_input("Password", type="password", key='new_password')
                new_role = st.selectbox("Role", role_options, key='new_role')
                new_email = st.text_input("Email", key='new_email')
                new_phone = st.text_input("Phone", key='new_phone')
                add_user_button = st.form_submit_button("Add User")
                if add_user_button:
                    if new_username and new_password:
                        add_user(cursor, conn, new_username, new_password, new_role, new_email, new_phone)
                        st.success(f"User {new_username} added successfully")
                        st.session_state.show_add_user_form = False  # Hide the form
                        time.sleep(1)  # Keep the success message for 1 seconds
                        st.experimental_rerun()
                    else:
                        st.error("Username and password cannot be empty")
            st.markdown('</div>', unsafe_allow_html=True)

        # Update user form
        if st.session_state.get('show_update_delete_form', None) == 'update':
            if selected_indices:
                for idx in selected_indices:
                    selected_user = df.iloc[idx]
                    st.markdown('<div class="form-container">', unsafe_allow_html=True)
                    with st.form(key=f'update_user_form_{idx}'):
                        st.write(f"Update User: {selected_user['Username']}")
                        new_username = st.text_input("Username", value=selected_user['Username'], key=f"new_username_{idx}")
                        new_role = st.selectbox("New Role", role_options, index=role_options.index(selected_user['Role']), key=f"new_role_{idx}")
                        new_email = st.text_input("Email", value=selected_user['Email'], key=f"new_email_{idx}")
                        new_phone = st.text_input("Phone", value=selected_user['Phone'], key=f"new_phone_{idx}")
                        update_user_button = st.form_submit_button("Update User")
                        if update_user_button:
                            update_user_details(cursor, conn, selected_user['Username'], new_username, new_role, new_email, new_phone)
                            success_placeholder = st.empty()
                            success_placeholder.success(f"User {new_username}'s details updated successfully")
                            st.session_state.show_update_delete_form = None  # Hide the form
                            time.sleep(1)  # Keep the success message for 1 seconds
                            success_placeholder.empty()
                            st.experimental_rerun()
                    st.markdown('</div>', unsafe_allow_html=True)

        # Delete user form
        if st.session_state.get('show_update_delete_form', None) == 'delete':
            if selected_indices:
                for idx in selected_indices:
                    selected_user = df.iloc[idx]
                    if st.button(f"Confirm Deletion of {selected_user['Username']}", key=f'delete_{idx}'):
                        delete_user(cursor, conn, selected_user['Username'])
                        success_placeholder = st.empty()
                        success_placeholder.success(f"User {selected_user['Username']} deleted successfully")
                        st.session_state.show_update_delete_form = None  # Hide the form
                        time.sleep(1)  # Keep the success message for 1 seconds
                        success_placeholder.empty()
                        st.experimental_rerun()
    with tab2: 
        st.subheader("System Settings")
        st.text("Configure application settings here.")
    with tab3:
        st.subheader("Settings for Notifications and Alerts")
        st.text("Configure notifications and alert settings here.")
    with tab4:
        st.subheader("Additional Configuration Options")
        st.text("Additional configuration options here.")
    with tab5:
        st.subheader("High-Level KPIs")
        st.text("Overview of key performance indicators.")
        st.metric(label="Total Users", value=len(df))
        st.metric(label="System Uptime", value="99.9%")
    
    # active_sessions = fetch_active_sessions_count(cursor)
    # st.metric(label="Active Sessions", value=active_sessions)
    
    

if __name__ == "__main__":
    with DatabaseConnection(host='localhost', user='postgres', password='Postgres123', database='FraudDetection') as db:
        display_admin_dashboard(db.cursor, db.conn)