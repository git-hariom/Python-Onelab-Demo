import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.table import Table
 
# Read Excel file
def graphres():
    df = pd.read_excel(r'C:\Users\Public\output.xlsx')
 
    # Set the width of each bar
    barWidth = 0.4
    
    # Set the position of each bar on the x-axis
    r1 = range(len(df))
    r2 = [x + barWidth for x in r1]
    
    # Create a vertical clustered bar chart for Pass and Fail counts
    fig, ax = plt.subplots()
    ax.bar(r1, df['Pass'], width=barWidth, color='g', label='Pass')
    ax.bar(r2, df['Fail'], width=barWidth, color='r', label='Fail')
    
    # Set the y-axis label
    ax.set_ylabel('Number of Occurrences')
    
    # Set the title
    ax.set_title('Sample Output Graph')
    
    # Set the x-axis tick marks and labels
    ax.set_xticks([r + barWidth / 2 for r in r1])
    ax.set_xticklabels(df['Rule_Name'])
    
    # Show legend
    ax.legend()
    
    # Define the table content
    table_data = []
    for i in range(len(df)):
        table_data.append([df['Rule_Name'][i], df['Pass'][i], df['Fail'][i]])
    
    # Create the table
    table = ax.table(cellText=table_data, loc='bottom', cellLoc='center', colLabels=['Rule Name', 'Pass', 'Fail'])
    
    # Set the table font size
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    
    # Adjust the table layout and add padding
    plt.subplots_adjust(left=0.2, bottom=0.3)
    
    # Show the graph
    plt.show()