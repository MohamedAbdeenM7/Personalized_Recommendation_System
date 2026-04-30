import pandas as pd
import os

def load_ratings(path: str) -> pd.DataFrame:
    """
    Load ratings from CSV file

    Parameters:
        path: File path on Drive

    Returns:
        DataFrame with columns: user_id, product_id, rating, date
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(
        path,
        header=None,
        names=["user_id", "product_id", "rating", "timestamp"]
    )

    df["date"] = pd.to_datetime(df["timestamp"], unit="s")
    df = df.drop(columns=["timestamp"])

    print(f"✅ Data loaded successfully!")
    print(f"📊 Shape: {df.shape}")
    print(f"👥 Unique Users: {df['user_id'].nunique():,}")
    print(f"📦 Unique Products: {df['product_id'].nunique():,}")

    return df


def validate_data(df: pd.DataFrame) -> bool:
    """
    Validate the loaded data

    Parameters:
        df: DataFrame to validate

    Returns:
        True if data is valid
    """
    required_columns = ["user_id", "product_id", "rating", "date"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"❌ Missing column: {col}")

    if not df["rating"].between(1, 5).all():
        raise ValueError("❌ Ratings must be between 1 and 5")

    if df.isnull().sum().sum() > 0:
        raise ValueError("❌ Data contains missing values")

    print("✅ Data validation passed!")
    return True


if __name__ == "__main__":
    DATA_PATH = "/content/drive/MyDrive/recommendation-data/Electronics.csv"
    df = load_ratings(DATA_PATH)
    validate_data(df)
    print(df.head())
