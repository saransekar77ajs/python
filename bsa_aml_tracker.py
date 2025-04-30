import pandas as pd
from datetime import datetime, timedelta


# Function to get the Wednesday of the current week
def get_current_week_wednesday():
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    wednesday = start_of_week + timedelta(days=2)
    return wednesday


# Function to apply DQ Checks
def apply_dq_check(df, tracker):
    observations = []
    current_week_wednesday = get_current_week_wednesday()

    # Clean percentage fields
    percentage_fields = ["Prior Week % Complete", "% Complete", "CTR", "SAR", "EWFCRA"]
    for field in percentage_fields:
        if field in df.columns:
            df[field] = (
                df[field]
                .astype(str)
                .str.replace("%", "", regex=False)
                .str.replace(r"[^\d\.]", "", regex=True)
                .str.strip()
            )
            df[field] = pd.to_numeric(df[field], errors="coerce") * 100

    for index, row in df.iterrows():
        # DQ1: If Status = On Track then the "Current % Complete" column should have a % value other than 0
        if row["Status"] == "On Track" and df.at[index, "% Complete"] == 0:
            observations.append(
                {
                    "Tracker Name": tracker,
                    "Row #": index + 2,
                    "Field Name": "% Complete",
                    "Observation": "Status is On Track but % Complete is 0.",
                }
            )

        # DQ2: If Status = On Track then the "Finish Date" should be later than Wednesday of the review week
        finish_date = row["Due Date"]
        if isinstance(finish_date, str):
            finish_date = datetime.strptime(finish_date, "%m/%d/%Y")
        if row["Status"] == "On Track" and finish_date <= current_week_wednesday:
            observations.append(
                {
                    "Tracker Name": tracker,
                    "Row #": index + 2,
                    "Field Name": "Due Date",
                    "Observation": "Status is On Track but due date is not later than Wednesday of the review week.",
                }
            )

        # DQ3: If Status = On Track then the "Current % Complete" should be less than 100%
        if row["Status"] == "On Track" and df.at[index, "% Complete"] == 100:
            observations.append(
                {
                    "Tracker Name": tracker,
                    "Row #": index + 2,
                    "Field Name": "% Complete",
                    "Observation": "Status is On Track but % Complete is 100%.",
                }
            )
        # to check the numeric value of the percentage field
        # if row["Status"] == "Completed":
        #     print(
        #         f"[DEBUG] Row {index + 2}: Status=Completed, % Complete={df.at[index, '% Complete']}"
        #     )

        # DQ4: If Status = Completed then the "Current % Complete" should be 100%
        if row["Status"] == "Completed" and df.at[index, "% Complete"] != 100:
            observations.append(
                {
                    "Tracker Name": tracker,
                    "Row #": index + 2,
                    "Field Name": "% Complete",
                    "Observation": "Status is Completed but % Complete is not 100%.",
                }
            )

        # DQ5: If Status = Completed then the "Completed Date" should have completion date populated less than today
        completion_date = row["Completion Date"]
        if isinstance(completion_date, str):
            try:
                completion_date = datetime.strptime(completion_date, "%m/%d/%Y")
            except ValueError:
                completion_date = None

        if pd.isnull(completion_date):
            completion_date = None
        if row["Status"] == "Completed" and (
            not completion_date or completion_date >= datetime.now()
        ):
            observations.append(
                {
                    "Tracker Name": tracker,
                    "Row #": index + 2,
                    "Field Name": "Completion Date",
                    "Observation": "Status is Completed but Completion Date is not populated or is >= Today.",
                }
            )

        # DQ6: If Status = Not Started then the "Current % Complete" should have null or 0%
        if row["Status"] == "Not Started" and df.at[index, "% Complete"] != 0:
            observations.append(
                {
                    "Tracker Name": tracker,
                    "Row #": index + 2,
                    "Field Name": "% Complete",
                    "Observation": "Status is Not Started but % Complete is not null or 0%.",
                }
            )

        # DQ7: If Status = Not Started then the "Start Date" should be later than Tuesday of the review week
        review_week_tuesday = current_week_wednesday - timedelta(days=1)
        start_date = row["Start Date"]
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%m/%d/%Y")
        if row["Status"] == "Not Started" and start_date <= review_week_tuesday:
            observations.append(
                {
                    "Tracker Name": tracker,
                    "Row #": index + 2,
                    "Field Name": "Start Date",
                    "Observation": "Status is Not Started but Start Date is not later than Tuesday of the review week.",
                }
            )

        # DQ8: If Status = Off Track or AT Risk, then column R through U should be populated with correct values
        if row["Status"] in ["Off Track", "AT Risk"] and (
            not row["Status Reason"]
            or not row["Reason Description"]
            or not row["Path to Resolution"]
            or not row["Target Resolution Date"]
        ):
            observations.append(
                {
                    "Tracker Name": tracker,
                    "Row #": index + 2,
                    "Field Name": "Status Reason, Reason Description, Path to Resolution, Target Resolution Date",
                    "Observation": "Status is Off Track or AT Risk but required columns are not populated with correct values.",
                }
            )

        # DQ9: If Status = Off Track or AT Risk, then the "Target Resolution Date" shouldn't be less than the review date
        target_resolution_date = row["Target Resolution Date"]
        if isinstance(target_resolution_date, str):
            try:
                target_resolution_date = datetime.strptime(
                    target_resolution_date, "%m/%d/%Y"
                )
            except ValueError:
                target_resolution_date = None
        if pd.isnull(target_resolution_date):
            target_resolution_date = None
        review_date = datetime.now()
        if row["Status"] in ["Off Track", "AT Risk"] and (
            not target_resolution_date or target_resolution_date < review_date
        ):
            observations.append(
                {
                    "Tracker Name": tracker,
                    "Row #": index + 2,
                    "Field Name": "Target Resolution Date",
                    "Observation": "Status is Off Track or AT Risk but Target Resolution Date is less than the review date.",
                }
            )

        # Check for non-numeric values in percentage fields
        percentage_fields = [
            "Prior Week % Complete",
            "% Complete",
            "CTR",
            "SAR",
            "EWFCRA",
        ]
        for field in percentage_fields:
            value = str(row[field]).replace("%", "").strip()
            if not value.replace(".", "", 1).isdigit():
                observations.append(
                    {
                        "Tracker Name": tracker,
                        "Row #": index + 2,
                        "Field Name": field,
                        "Observation": f"{field} contains non-numeric value.",
                    }
                )
    return observations


# Read the data
path = "C:\\Users\\saran\\OneDrive\\Desktop\\CBX_9_Weekly_Status.xlsx"
df = pd.read_excel(path)

# Apply DQ Checks
observations = apply_dq_check(df, "CB X-9")

# Convert observations to DataFrame
observations_df = pd.DataFrame(observations)

# Save observations to Excel
observations_df.to_excel(
    "C:\\Users\\saran\\OneDrive\\Desktop\\DQ_Validations_Results_New.xlsx", index=False
)

print("DQ Validation results have been saved successfully")
