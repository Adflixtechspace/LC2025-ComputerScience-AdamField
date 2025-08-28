import plotly.graph_objects as go

# Create a simple plot
fig = go.Figure()

# Add data to the plot
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines', name='Line'))

# Set the title and center it
fig.update_layout(
    title={
        'text': "Centered Plot Title",  # Title text
        'x': 0.5,                       # Center the title
        'xanchor': 'center',            # Ensure alignment is centered
        'yanchor': 'top'                # Align the title at the top
    }
)

# Show the figure
fig.show()