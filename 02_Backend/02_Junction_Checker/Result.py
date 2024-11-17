import pandas as pd

# Read the sample data from the Excel file
def tableresult():
    df = pd.read_excel(r'C:\Users\Public\usercode.xlsx')

    # Group the DataFrame by `Rule_Name`, `Result`, and `Desc`
    grouped = df.groupby(['Rule_Name', 'Result']).size()
    
    # Pivot the DataFrame to convert the rows into columns
    pivot = grouped.unstack(fill_value=0)
    
    # Output the results to an Excel file
    pivot.to_excel(r'C:\Users\Public\output.xlsx')