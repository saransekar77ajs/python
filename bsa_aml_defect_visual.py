import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap

# Load the Excel file
# file_path = "C:\\Users\\saran\\OneDrive\\Desktop\\DQ_Validations_Results_New.xlsx"
file_path = "C:\\Users\\saran\\Downloads\\Sample_DQ_Validations_Results.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# Create a separate table view to show what went wrong
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis("tight")
ax.axis("off")
table_data = df[["Tracker Name", "Row #", "Field Name", "Observation"]]

# Wrap text in the Observation column to prevent overflow
wrapped_table_data = table_data.copy()
wrapped_table_data["Observation"] = wrapped_table_data["Observation"].apply(
    lambda x: "\n".join(wrap(x, width=50))
)

# Create a table with adjusted column widths and wrapped text in the Observation column
table = ax.table(
    cellText=wrapped_table_data.values,
    colLabels=wrapped_table_data.columns,
    loc="center",
    cellLoc="center",
)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Adjust column widths
col_widths = [
    0.15,
    0.10,
    0.15,
    0.60,
]  # Adjusted widths for Tracker Name, Row #, Field Name, and Observation
for i, width in enumerate(col_widths):
    table.auto_set_column_width(i)
    for key, cell in table.get_celld().items():
        if key[1] == i:
            cell.set_width(width)

# Increase row height further without shrinking the entire image or affecting the bar chart y-axis values
for key, cell in table.get_celld().items():
    cell.set_height(0.05)

# Adjust layout and save the table view as an image file
plt.tight_layout()
plt.savefig("tracker_observations_table_view.png")

# Show the table view
plt.show()
