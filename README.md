# mini-data-cleaning-project
# Mini Data Cleaning Project
## Overview
This project demonstrates cleaning a real dataset end-to-end using Python and pandas.
The goal is to transform raw data into an analysis-ready dataset.
## Dataset
The dataset contains the following columns:
* **age** – may include missing values
* **income** – includes missing values and extreme outliers
* **city** – text values with inconsistent formatting
* **signup_time** – stored as text and requires datetime conversion
## Cleaning Steps
The following steps were applied:
1. Converted data types to numeric and datetime where needed
2. Filled missing values in **age** and **income** using the median
3. Limited extreme **income** values at the 99th percentile
4. Cleaned **city** text by removing spaces and converting to lowercase
5. Converted **signup_time** to UTC timezone
## Output
The cleaned dataset is saved as:
```
cleaned_dataset.csv
```
## How to Run
```bash
python clean_data.py
```
This will generate the cleaned dataset automatically.
## Conclusion
The project shows a simple and clear data-cleaning pipeline that prepares raw data for analysis or machine learning.
