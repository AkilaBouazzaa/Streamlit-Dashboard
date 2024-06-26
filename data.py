import psycopg2
import pandas as pd

def load_fraud_data(filter_type, month, trimester, start_date, end_date):
    # Database connection details
    db_params = {
        "dbname": "CNAS",
        "user": "postgres",
        "password": "SQLAKILA111",
        "host": "localhost",
        "port": "5432"
    }

    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        if filter_type == "Month":
            query = f"""
            SELECT 
                DATE_PART('week', "DATE_PAIEMENT") AS week,
                "month",
                "trimester",
                "TRANCHE_AGE_BENEF",
                "SEXE_F",
                "SEXE_M",
                "TS_O",
                "TS_N",
                "NUM_ENR",
                "CODEPS",
                "ID",
                "NO_DOSSIER_NAT",
                "DATE_PAIEMENT",
                "QUANTITE_MED",
                "nom_dci",
                "predictions",
                "C17",
                "C80",
                SUM("MT_MEDIC") AS total_cost,
                COUNT(*) AS total_records,
                SUM(CASE WHEN "predictions" = 1 THEN 1 ELSE 0 END) AS fraud_cases,
                SUM(CASE WHEN "predictions" = 2 THEN 1 ELSE 0 END) AS sus_cases,
                SUM(CASE WHEN "predictions" = 1 AND "SEXE_F" = 1 THEN 1 ELSE 0 END) AS female_fraud_cases,
                SUM(CASE WHEN "predictions" = 1 AND "SEXE_M" = 1 THEN 1 ELSE 0 END) AS male_fraud_cases
            FROM results
            WHERE "month" = {month}
            GROUP BY week, "month", "trimester", "TRANCHE_AGE_BENEF", "SEXE_F", "SEXE_M", "TS_O", "TS_N", "NUM_ENR", "CODEPS", "ID", "NO_DOSSIER_NAT", "DATE_PAIEMENT", "QUANTITE_MED","nom_dci","predictions", "C17","C80"
            ORDER BY week
            """
        elif filter_type == "Trimester":
            query = f"""
            SELECT 
                DATE_PART('week', "DATE_PAIEMENT") AS week,
                "month",
                "trimester",
                "TRANCHE_AGE_BENEF",
                "SEXE_F",
                "SEXE_M",
                "TS_O",
                "TS_N",
                "NUM_ENR",
                "CODEPS",
                "ID",
                "NO_DOSSIER_NAT",
                "DATE_PAIEMENT",
                "QUANTITE_MED",
                "nom_dci",
                "predictions",
                "C17","C80",
                SUM("MT_MEDIC") AS total_cost,
                COUNT(*) AS total_records,
                SUM(CASE WHEN "predictions" = 1 THEN 1 ELSE 0 END) AS fraud_cases,
                SUM(CASE WHEN "predictions" = 2 THEN 1 ELSE 0 END) AS sus_cases,
                SUM(CASE WHEN "predictions" = 1 AND "SEXE_F" = 1 THEN 1 ELSE 0 END) AS female_fraud_cases,
                SUM(CASE WHEN "predictions" = 1 AND "SEXE_M" = 1 THEN 1 ELSE 0 END) AS male_fraud_cases
            FROM results
            WHERE "trimester" = {trimester}
            GROUP BY week, "month", "trimester", "TRANCHE_AGE_BENEF", "SEXE_F", "SEXE_M", "TS_O", "TS_N", "NUM_ENR", "CODEPS", "ID", "NO_DOSSIER_NAT", "DATE_PAIEMENT", "QUANTITE_MED","nom_dci","predictions","C17","C80"
            ORDER BY week
            """
        elif filter_type == "Date Range":
            query = f"""
            SELECT 
                DATE_PART('week', "DATE_PAIEMENT") AS week,
                "month",
                "trimester",
                "TRANCHE_AGE_BENEF",
                "SEXE_F",
                "SEXE_M",
                "TS_O",
                "TS_N",
                "NUM_ENR",
                "CODEPS",
                "ID",
                "NO_DOSSIER_NAT",
                "DATE_PAIEMENT",
                "QUANTITE_MED",
                "nom_dci",
                "predictions",
                "C17","C80",
                SUM(CASE WHEN "predictions" = 1 THEN "MT_MEDIC" ELSE 0 END) AS total_cost, 
                COUNT(*) AS total_records,
                SUM(CASE WHEN "predictions" = 1 THEN 1 ELSE 0 END) AS fraud_cases,
                SUM(CASE WHEN "predictions" = 2 THEN 1 ELSE 0 END) AS sus_cases,
                SUM(CASE WHEN "predictions" = 1 AND "SEXE_F" = 1 THEN 1 ELSE 0 END) AS female_fraud_cases,
                SUM(CASE WHEN "predictions" = 1 AND "SEXE_M" = 1 THEN 1 ELSE 0 END) AS male_fraud_cases
            FROM results
            WHERE "DATE_PAIEMENT" BETWEEN '{start_date}' AND '{end_date}'
            GROUP BY week, "month", "trimester", "TRANCHE_AGE_BENEF", "SEXE_F", "SEXE_M", "TS_O", "TS_N", "NUM_ENR", "CODEPS", "ID", "NO_DOSSIER_NAT", "DATE_PAIEMENT", "QUANTITE_MED","nom_dci", "predictions","C17","C80"
            ORDER BY week
            """

        cursor.execute(query)
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
        fraud_data = pd.DataFrame(rows, columns=colnames)
        
        if fraud_data.empty:
            print("Data loaded but DataFrame is empty")
        else:
            print("Data loaded successfully")
        return fraud_data

    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()

    finally:
        if connection:
            cursor.close()
            connection.close()

