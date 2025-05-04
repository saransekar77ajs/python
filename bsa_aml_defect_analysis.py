import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Load your data
df = pd.read_excel("C:\\Users\\saran\\Downloads\\Sample_DQ_Validations_Results.xlsx")

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Dropdown(
            id="tracker-dropdown",
            options=[
                {"label": tracker, "value": tracker}
                for tracker in df["Tracker Name"].unique()
            ],
            value=df["Tracker Name"].unique()[0],
        ),
        dcc.Graph(id="summary-graph"),
        dcc.Graph(id="details-graph"),
    ]
)


@app.callback(Output("summary-graph", "figure"), Input("tracker-dropdown", "value"))
def update_summary(selected_tracker):
    filtered_df = df[df["Tracker Name"] == selected_tracker]
    summary_data = filtered_df.groupby("Field Name").size().reset_index(name="Count")
    return {
        "data": [
            {"x": summary_data["Field Name"], "y": summary_data["Count"], "type": "bar"}
        ],
        "layout": {"title": "Summary View"},
    }


@app.callback(Output("details-graph", "figure"), Input("tracker-dropdown", "value"))
def update_details(selected_tracker):
    filtered_df = df[df["Tracker Name"] == selected_tracker]
    return {
        "data": [
            {
                "x": filtered_df["Row #"],
                "y": filtered_df["Observation"],
                "type": "scatter",
                "mode": "markers",
            }
        ],
        "layout": {"title": "Detailed View"},
    }


if __name__ == "__main__":
    app.run(debug=True)
