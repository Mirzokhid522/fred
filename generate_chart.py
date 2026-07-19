import pandas as pd
import plotly.graph_objects as go

# 1. Load the data
# Adjust 'Date', 'All groups CPI', 'Trimmed mean' to match your CSV headers exactly
df = pd.read_csv('Trimmed mean.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 2. Create the figure
fig = go.Figure()

# Add All groups CPI line
fig.add_trace(go.Scatter(x=df['Date'], y=df['All groups CPI'],
                    mode='lines', name='All groups CPI',
                    line=dict(color='#5DADE2', width=2)))

# Add Trimmed mean line
fig.add_trace(go.Scatter(x=df['Date'], y=df['Trimmed mean'],
                    mode='lines', name='Trimmed mean',
                    line=dict(color='#1A5276', width=2)))

# 3. Apply Dark Theme styling
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title="Australian CPI Trends",
    xaxis=dict(showgrid=True, gridcolor='#333333', title="Date"),
    yaxis=dict(showgrid=True, gridcolor='#333333', title="Percentage change (%)"),
    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
)

# 4. Save to index.html
fig.write_html("index.html")