# 📦 Data — Amazon Electronics Dataset

---

## 📌 Source

- **Name:** Amazon Product Reviews v2
- **Category:** Electronics
- **Link:** <https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/>
- **Type:** Ratings Only (5-core)

---

## 📊 Dataset Structure

- | Column | Type | Description |
- |--------|------|-------------|
- | user_id | string | Unique user identifier |
- | product_id | string | Unique product identifier (ASIN) |
- | rating | float | User rating (1.0 to 5.0) |
- | date | datetime | Date of the rating |

---

## 📁 Folder Structure

- data/
- ├── raw/
  │   └── Electronics.csv        # Raw ratings file (not on GitHub)
- └── processed/
    └── ratings_clean.csv      # Cleaned ratings file (not on GitHub)

---

## ⚠️ Important Notes

1. Raw data is NOT uploaded to GitHub
2. Data is stored on Google Drive
3. Path: /content/drive/MyDrive/recommendation-data/

---

## 📈 Dataset Stats (After Preprocessing)

- | Metric | Value |
- |--------|-------|
- | Total Ratings | Filtered to active users |
- | Unique Users | Users with at least 5 ratings |
- | Unique Products | Products with at least 5 ratings |
- | Rating Range | 1.0 to 5.0 |
- | Sparsity | Above 99% |

---

## 🚀 How to Load the Data

### Step 1: Mount Google Drive

from google.colab import drive
drive.mount('/content/drive')

### Step 2: Load Raw Data

import pandas as pd

df = pd.read_csv(
    '/content/drive/MyDrive/recommendation-data/Electronics.csv',
    header=None,
    names=['user_id', 'product_id', 'rating', 'timestamp']
)

### Step 3: Load Clean Data

df_clean = pd.read_csv(
    '/content/drive/MyDrive/recommendation-data/ratings_clean.csv'
)

---

## 🔧 Preprocessing Steps Applied

- | Step | Description |
- |------|-------------|
- | Remove Duplicates | Removed duplicate rows |
- | Filter Ratings | Kept ratings between 1.0 and 5.0 |
- | Active Users | Kept users with at least 5 ratings |
- | Popular Products | Kept products with at least 5 ratings |
- | Timestamp | Converted to datetime format |
