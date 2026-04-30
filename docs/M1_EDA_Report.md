# M1 — EDA Report

## Amazon Electronics Dataset — Ratings Only

---

## 1. Dataset Overview

- | Metric | Value |
- |--------|-------|
- | Source | Amazon Product Reviews v2 |
- | Category | Electronics |
- | Type | Ratings Only |
- | Columns | user_id, product_id, rating, date |

---

## 2. Data Cleaning

- | Step | Description |
- |------|-------------|
- | Remove Duplicates | Removed duplicate rows |
- | Filter Ratings | Kept ratings between 1 and 5 |
- | Active Users | Kept users with at least 5 ratings |
- | Popular Products | Kept products with at least 5 ratings |

---

## 3. EDA Insights

### 3.1 Rating Distribution

- Most users tend to give high ratings (4 and 5 stars)
- Very few users give 1 or 2 star ratings

### 3.2 User Activity

- Most users have rated only a few products
- A small number of users are very active

### 3.3 Product Popularity

- Most products have very few ratings
- A small number of products are very popular

### 3.4 Ratings over Time

- Rating activity has increased over the years
- Peak activity was observed in recent years

---

## 4. Sparsity Analysis

- The user-item matrix is highly sparse
- Most users have not rated most products
- Sparsity is above 99%

---

## 5. Output Files

- | File | Description |
- |------|-------------|
- | ratings_clean.csv | Cleaned ratings dataset |
- | eda_report.png | EDA visualizations |

---

## 6. Next Steps

- Use cleaned data for model development (M2)
- Build collaborative filtering model
- Build content-based filtering model
