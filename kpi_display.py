import streamlit as st

def display_kpis(fraud_data):
    if fraud_data is None or fraud_data.empty:
        st.error("No data available to display KPIs.")
        return

    # Extract KPI values
    total_fraudulent_claims = fraud_data['fraud_cases'].sum()
    female_suspects = fraud_data['female_fraud_cases'].sum()
    male_suspects = fraud_data['male_fraud_cases'].sum()
    medications_involved = fraud_data['NUM_ENR'].nunique()
    prejudice = fraud_data['total_cost'].sum() 
    sus_cases=fraud_data['sus_cases'].sum()


    # Display KPIs using custom HTML
    st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-card">
                <span class="kpi-value">{total_fraudulent_claims}</span>
                <span class="kpi-label">Total Fraudulent Claims 🔍</span>
            </div>
            <div class="kpi-card">
                <span class="kpi-value">{female_suspects}</span>
                <span class="kpi-label">Female Suspects 👩‍⚕️</span>
            </div>
            <div class="kpi-card">
                <span class="kpi-value">{male_suspects}</span>
                <span class="kpi-label">Male Suspects 👨‍⚕️</span>
            </div>
            <div class="kpi-card">
                <span class="kpi-value">{medications_involved}</span>
                <span class="kpi-label">Medications Involved 💊</span>
            </div>
            <div class="kpi-card">
                <span class="kpi-value">{sus_cases}</span>
                <span class="kpi-label">Suspicious cases 🕵️‍♂️</span>
            </div>
            
        </div>
    """, unsafe_allow_html=True)

# <div class="kpi-card">
#                 <span class="kpi-value">{prejudice}</span>
#                 <span class="kpi-label">Prejudice in DZD 💰</span>
#                 <div class="tooltip">{prejudice}</div>
#             </div>