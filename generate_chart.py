import pandas as pd
import plotly.graph_objects as go

# 1. Load data, skipping the title row
df = pd.read_csv('Trimmed mean.csv', skiprows=1, names=['Date', 'All groups CPI', 'Trimmed mean'])

# 2. Fix the dates explicitly to 'YYYY-Mon' format
def fix_year(date_str):
    date_str = str(date_str).strip()
    # Replace '22-', '23-', etc. with '2022-', '2023-'
    for year in ['22', '23', '24', '25', '26']:
        if date_str.startswith(year + '-'):
            return date_str.replace(year + '-', '20' + year + '-')
    return date_str

df['Date'] = df['Date'].apply(fix_year)

# 3. Convert to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%b')

# 4. Sort by date
df = df.sort_values('Date')

# 5. Create the figure
fig = go.Figure()

fig.add_trace(go.Scatter(x=df['Date'], y=df['All groups CPI'],
                    mode='lines+markers', name='All groups CPI',
                    line=dict(color='#5DADE2', width=2)))

fig.add_trace(go.Scatter(x=df['Date'], y=df['Trimmed mean'],
                    mode='lines+markers', name='Trimmed mean',
                    line=dict(color='#1A5276', width=2)))

# 6. Apply Dark Theme styling
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title="Australian CPI Trends",
    xaxis=dict(showgrid=True, gridcolor='#333333', title="Date"),
    yaxis=dict(showgrid=True, gridcolor='#333333', title="Percentage change (%)"),
    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
)

# 7. Save to index.html
fig.write_html("index.html")