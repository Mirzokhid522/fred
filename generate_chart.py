import pandas as pd
import plotly.graph_objects as go

# 1. Load the data from the CSV file
df = pd.read_csv('CPI_Data.csv')

# 2. Convert the 'Date' column to datetime objects
# The date format in the CSV is 'MMM-YY' (e.g., 'Mar-22')
df['Date'] = pd.to_datetime(df['Date'], format='%b-%y')

# 3. Sort the dataframe by date to ensure the line chart plots correctly
df = df.sort_values('Date')

# 4. Initialize the figure
fig = go.Figure()

# 5. Add 'All groups CPI' trace
fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['All groups CPI'],
    mode='lines+markers', 
    name='All groups CPI',
    line=dict(color='#5DADE2', width=2)
))

# 6. Add 'Trimmed mean' trace
fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Trimmed mean'],
    mode='lines+markers', 
    name='Trimmed mean',
    line=dict(color='#1A5276', width=2)
))

# 7. Apply the dark-themed layout
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title="Australian CPI Trends",
    xaxis=dict(showgrid=True, gridcolor='#333333', title="Date"),
    yaxis=dict(showgrid=True, gridcolor='#333333', title="Percentage change (%)"),
    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
)

# 8. Export to index.html
fig.write_html("index.html")