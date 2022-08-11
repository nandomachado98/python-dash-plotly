from dash import Dash
import dash_html_components as html

# Create a dash application
app = Dash(__name__)

# Application layout
app.layout = html.H1('hi mom')

# Run the app
app.run_server(debug=True)

