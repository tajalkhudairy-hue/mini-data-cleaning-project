import pandas as pd

def clean_data_project(df_raw):
    df = df_raw.copy()

    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["income"] = pd.to_numeric(df["income"], errors="coerce")
    df["signup_time"] = pd.to_datetime(df["signup_time"], errors="coerce")

    df["age"] = df["age"].fillna(df["age"].median())
    df["income"] = df["income"].fillna(df["income"].median())

    cap = df["income"].quantile(0.99)
    df["income"] = df["income"].clip(upper=cap)

    df["city"] = df["city"].str.strip().str.lower()
    df["signup_time"] = df["signup_time"].dt.tz_localize("UTC")

    return df


if __name__ == "__main__":
    df_raw = pd.read_csv("mini_project_dataset.csv")
    df_clean = clean_data_project(df_raw)
    df_clean.to_csv("cleaned_dataset.csv", index=False)
