
## Project Structure

sales-etl-project/
├── data/
├── output/
├── sales_etl.py
└── README.md
# Sales ETL Project

This project reads CSV files, cleans and transforms the data, joins customer, product, and order tables, and loads the final results into an output CSV file.


## Technologies Used

- Python
- Pandas
- CSV
- Git
- GitHub

## ETL Process

- Extract: Read customer, product, and order data from CSV files.
- Transform: Remove duplicates, clean extra spaces, standardize city names, convert data types, join the datasets, calculate total sales, and sort the results.
- Load: Save the final transformed data to `output/finalsales.csv`.

## How to Run

Run the following command:

python sales_etl.py