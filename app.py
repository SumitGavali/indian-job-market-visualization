#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)


# In[2]:


app = Dash(__name__)


# In[3]:


df= pd.read_csv("india_job_market_dataset.csv")


# In[5]:


# Load dataset
file_path = "india_job_market_dataset.csv"  # Ensure correct path
df = pd.read_csv("india_job_market_dataset.csv")

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Indian Job Market", style={'text-align': 'center'}),

    dcc.Dropdown(
        id="skills_dropdown",
        options=[{"label": skill, "value": skill} for skill in 
                 ['AWS', 'C++', 'Digital Marketing', 'Excel', 'Java', 'Python', 'Machine Learning', 'SQL']],
        multi=False,
        value="Python",  # Set a valid default skill
        style={'width': "40%"}
    ),
    
    html.Div(id='output_container', children=[]),
    html.Br(),
    
    dcc.Graph(id='job_distribution_graph', figure={})
])


# Callback to update the output container and graph
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='job_distribution_graph', component_property='figure')],
    [Input(component_id='skills_dropdown', component_property='value')]  # Fixed bracket placement
)
def update_graph(selected_skill):
    # Filter data based on the selected skill
    filtered_df = df[df['Skills Required'].str.contains(selected_skill, na=False)]
    
    # Update output text
    output_text = f"Showing job listings for {selected_skill} ({len(filtered_df)} jobs found)."

    # Count job locations and rename columns for Plotly
    location_counts = filtered_df['Job Location'].value_counts().reset_index()
    location_counts.columns = ['Location', 'Job Count']  # Rename for clarity
    
    # Create a bar chart showing job counts by location
    fig = px.bar(
        location_counts,
        x='Location', 
        y='Job Count',
        labels={'Location': 'City', 'Job Count': 'Number of Jobs'},
        title=f"Job Distribution for {selected_skill}"
    )
    
    return output_text, fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:





# In[ ]:




