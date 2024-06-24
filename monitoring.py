import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def display_monitoring_page(selected_model):
    tabs = st.tabs(["Model Performance", "Data Drift Detection"])

    with tabs[0]:
        st.header("Model Performance")
        
        # Define model performance metrics for different models
        model_metrics_dict = {
            'Random Forest': {
                'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
                'Score': [0.95, 0.96, 0.94, 0.95]
            },
            'Decision Tree': {
                'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
                'Score': [0.90, 0.92, 0.88, 0.90]
            },
            'SVM': {
                'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
                'Score': [0.85, 0.87, 0.83, 0.85]
            },
            'Gradient Boost': {
                'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
                'Score': [0.85, 0.87, 0.83, 0.85]
            },
            'XGBoost': {
                'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
                'Score': [0.85, 0.87, 0.83, 0.85]
            },
            'Naive Bayes': {
                'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
                'Score': [0.85, 0.87, 0.83, 0.85]
            }

        }

        # Fetch metrics for the selected model
        model_metrics = model_metrics_dict[selected_model]
        model_metrics_df = pd.DataFrame(model_metrics)
        
        # Display metrics as a table
        st.write("### Metrics Table")
        st.dataframe(model_metrics_df)
        
        # Display metrics as a bar chart
        st.write("### Metrics Bar Chart")
        fig = px.bar(model_metrics_df, x='Metric', y='Score', color='Metric', title='Model Performance Metrics')
        st.plotly_chart(fig)
        
        # Example confusion matrices for different models
        confusion_matrices_dict = {
            'Random Forest': pd.DataFrame(
                {'Predicted Negative': [50, 10], 'Predicted Positive': [5, 35]},
                index=['Actual Negative', 'Actual Positive']
            ),
            'Decision Tree': pd.DataFrame(
                {'Predicted Negative': [45, 15], 'Predicted Positive': [10, 30]},
                index=['Actual Negative', 'Actual Positive']
            ),
            'SVM': pd.DataFrame(
                {'Predicted Negative': [40, 20], 'Predicted Positive': [15, 25]},
                index=['Actual Negative', 'Actual Positive']
                
            ),
            'Gradient Boost': pd.DataFrame(
                {'Predicted Negative': [40, 20], 'Predicted Positive': [15, 25]},
                index=['Actual Negative', 'Actual Positive']
                
            ),
            'XGBoost': pd.DataFrame(
                {'Predicted Negative': [40, 20], 'Predicted Positive': [15, 25]},
                index=['Actual Negative', 'Actual Positive']
                
            ),
            'Naive Bayes': pd.DataFrame(
                {'Predicted Negative': [40, 20], 'Predicted Positive': [15, 25]},
                index=['Actual Negative', 'Actual Positive']
                
            )
            
        }

        # Fetch confusion matrix for the selected model
        confusion_matrix = confusion_matrices_dict[selected_model]
        
        # Display confusion matrix as a table
        st.write("### Confusion Matrix")
        st.dataframe(confusion_matrix)
        
        # Confusion matrix as a heatmap
        fig = go.Figure(data=go.Heatmap(
            z=confusion_matrix.values,
            x=confusion_matrix.columns,
            y=confusion_matrix.index,
            colorscale='Viridis'))
        fig.update_layout(title='Confusion Matrix', xaxis_nticks=36)
        st.plotly_chart(fig)
        
        # ROC curves for different models
        roc_curves_dict = {
            
            'Random Forest': ([0, 0.1, 0.4, 1], [0, 0.7, 0.9, 1]),
            'Decision Tree': ([0, 0.2, 0.5, 1], [0, 0.6, 0.85, 1]),
            'Logistic Regression': ([0, 0.3, 0.6, 1], [0, 0.5, 0.8, 1]),
            'Gradient Boost': ([0, 0.3, 0.6, 1], [0, 0.5, 0.8, 1]),
            'XGBoost': ([0, 0.3, 0.6, 1], [0, 0.5, 0.8, 1]),
            'Naive Bayes': ([0, 0.3, 0.6, 1], [0, 0.5, 0.8, 1])
        }

        # Fetch ROC curve for the selected model
        fpr, tpr = roc_curves_dict[selected_model]
        
        # Display ROC Curve
        st.write("### ROC Curve")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines+markers', name='ROC Curve'))
        fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='Random Classifier', line=dict(dash='dash')))
        fig.update_layout(title='Receiver Operating Characteristic (ROC) Curve', xaxis_title='False Positive Rate', yaxis_title='True Positive Rate')
        st.plotly_chart(fig)
        
    with tabs[1]:
        st.header("Data Drift Detection")
        
        # Example data drift detection results
        drift_metrics = {
            'Feature': ['age', 'gender', 'qute'],
            'Drift Score': [0.02, 0.03, 0.05],
            'Threshold': [0.05, 0.05, 0.05]
        }
        drift_metrics_df = pd.DataFrame(drift_metrics)
        
        # Display data drift metrics as a table
        st.write("### Data Drift Metrics Table")
        st.dataframe(drift_metrics_df)
        
        # Display data drift metrics as a bar chart
        st.write("### Data Drift Bar Chart")
        fig = px.bar(drift_metrics_df, x='Feature', y='Drift Score', color='Feature', title='Data Drift Detection Scores')
        st.plotly_chart(fig)
        
        # Drift detection detailed results
        st.write("### Drift Detection Details")
        detailed_drift = {
            'Feature': ['age', 'gender', 'qute'],
            'P-Value': [0.02, 0.04, 0.06],
            'Distribution Change': ['Yes', 'Yes', 'No']
        }
        detailed_drift_df = pd.DataFrame(detailed_drift)
        st.dataframe(detailed_drift_df)

if __name__ == "__main__":
    from sidebar import setup_sidebar  # Assuming the sidebar setup is in a file named sidebar.py
    selected_model = setup_sidebar()
    display_monitoring_page(selected_model)