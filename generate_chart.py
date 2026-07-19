import pandas as pd
import plotly.graph_objects as go

# 1. Load the data
# skiprows=1 skips the title row; names assigns the column headers
df = pd.read_csv('Trimmed mean.csv', skiprows=1, names=['Date', 'All groups CPI', 'Trimmed mean'])

# 2. Convert Date column using the format '%b-%y' for 'Mar-22' style dates
df['Date'] = pd.to_datetime(df['Date'], format='%b-%y')

# 3. Create the figure
fig = go.Figure()

# Add All groups CPI line
fig.add_trace(go.Scatter(x=df['Date'], y=df['All groups CPI'],
                    mode='lines', name='All groups CPI',
                    line=dict(color='#5DADE2', width=2)))

# Add Trimmed mean line
fig.add_trace(go.Scatter(x=df['Date'], y=df['Trimmed mean'],
                    mode='lines', name='Trimmed mean',
                    line=dict(color='#1A5276', width=2)))

# 4. Apply Dark Theme styling
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title="Australian CPI Trends",
    xaxis=dict(showgrid=True, gridcolor='#333333', title="Date"),
    yaxis=dict(showgrid=True, gridcolor='#333333', title="Percentage change (%)"),
    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
)

# 5. Save to index.html
fig.write_html("index.html")