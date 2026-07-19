import pandas as pd
import plotly.graph_objects as go

# 1. Load data, skipping the title row
df = pd.read_csv('Trimmed mean.csv', skiprows=1, names=['Date', 'All groups CPI', 'Trimmed mean'])

# 2. Convert Date column using 'mixed' format
# 'dayfirst=True' ensures "22-Mar" is parsed correctly as March 2022
df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)

# 3. Sort by date to ensure the lines connect chronologically
df = df.sort_values('Date')

# 4. Create the figure
fig = go.Figure()

fig.add_trace(go.Scatter(x=df['Date'], y=df['All groups CPI'],
                    mode='lines+markers', name='All groups CPI',
                    line=dict(color='#5DADE2', width=2)))

fig.add_trace(go.Scatter(x=df['Date'], y=df['Trimmed mean'],
                    mode='lines+markers', name='Trimmed mean',
                    line=dict(color='#1A5276', width=2)))

# 5. Apply Dark Theme styling
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title="Australian CPI Trends",
    xaxis=dict(showgrid=True, gridcolor='#333333', title="Date"),
    yaxis=dict(showgrid=True, gridcolor='#333333', title="Percentage change (%)"),
    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
)

fig.write_html("index.html")