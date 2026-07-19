import pandas as pd
import plotly.graph_objects as go

# 1. Load the data, ignoring the title row
df = pd.read_csv('Trimmed mean.csv', skiprows=1, names=['Date', 'All groups CPI', 'Trimmed mean'])

# 2. Aggressive Data Cleaning:
# Strip whitespace from the 'Date' column and force it to a string type
df['Date'] = df['Date'].astype(str).str.strip()

# Attempt parsing with a manual cleanup approach
# This converts '22-Mar' by forcing it to datetime; if it fails, it will provide more info
try:
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b', errors='coerce')
except Exception as e:
    print(f"Error parsing dates: {e}")

# 3. Create the figure
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=df['Date'], y=df['All groups CPI'], mode='lines', name='All groups CPI', line=dict(color='#5DADE2')))
fig.add_trace(go.Scatter(x=df['Date'], y=df['Trimmed mean'], mode='lines', name='Trimmed mean', line=dict(color='#1A5276')))

# 4. Styling
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title="Australian CPI Trends",
    xaxis=dict(showgrid=True, gridcolor='#333333'),
    yaxis=dict(showgrid=True, gridcolor='#333333')
)

fig.write_html("index.html")