# ism2411-data-cleaning-copilot
This project demonstrates data cleaning on a messy sales dataset using Python and GitHub Copilot. The goal is to standardize and clean the dataset so it is ready for analysis, while also showcasing responsible use of AI coding tools.

### Features
- Standardizes column names to lowercase and underscores
- Removes whitespace inconsistencies in product and category names
- Handles missing values consistently
- Removes invalid rows with negative prices or quantities
- Outputs a cleaned CSV file ready for analysis

### How to Run
1. Clone the repository
2. Navigate to the project folder
3. Run `python src/data_cleaning.py`
4. The cleaned CSV will be saved to `data/processed/sales_data_clean.csv`

### Diagram
ism2411-data-cleaning-copilot/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv
│   └── processed/
│       └── sales_data_clean.csv   # created by your script
├── src/
│   └── data_cleaning.py          
├── README.md                      A Python data cleaning script that transforms a messy sales CSV into a clean, analysis-ready dataset
└── reflection.md                  # The diagram is how the project wil be organized
