import sqlite3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_best_hour():
    conn = sqlite3.connect("database.db")
    logs = conn.execute("SELECT completion_hour FROM logs").fetchall()
    conn.close()

    if len(logs) < 3:
        return "Not enough data"

    df = pd.DataFrame(logs, columns=["completion_hour"])
    df["x"] = np.arange(len(df))

    model = LinearRegression()
    model.fit(df[["x"]], df["completion_hour"])

    prediction = int(model.predict([[len(df)]])[0])
    return prediction
