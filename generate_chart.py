import pandas as pd
import plotly.graph_objects as go

file_path = 'Trimmed mean.csv'

try:
    # Load and clean
    df = pd.read_csv(file_path, header=1)
    df = df.dropna(how='all')
    
    # Ensure the first column (Date) is converted properly
    date_col = df.columns[0]
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col])

    # Create the chart
    fig = go.Figure()

    # Add "All groups CPI" (Column 2)
    fig.add_trace(go.Scatter(
        x=df[date_col], y=df.iloc[:, 1], 
        mode='lines', name='All groups CPI',
        line=dict(color='#5DADE2', width=2)
    ))

    # Add "Trimmed mean" (Column 3)
    fig.add_trace(go.Scatter(
        x=df[date_col], y=df.iloc[:, 2], 
        mode='lines', name='Trimmed mean',
        line=dict(color='#1B4F72', width=2)
    ))

    # Styling for dark theme and layout
    fig.update_layout(
        template="plotly_dark",
        title="Australian CPI Trends",
        xaxis_title="Date",
        yaxis_title="Percentage change (%)",
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
        plot_bgcolor='black',
        paper_bgcolor='black'
    )

    fig.write_html("index.html")
    print("Chart generated successfully as index.html")

except Exception as e:
    print(f"Error: {e}")