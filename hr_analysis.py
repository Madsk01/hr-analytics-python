import pandas as pd

data = pd.read_csv("hr_data.csv")

data["Join_Date"] = pd.to_datetime(data["Join_Date"])
data["Exit_Date"] = pd.to_datetime(data["Exit_Date"])

total_employees = len(data)

active = data[data["Status"] == "Active"].shape[0]

leavers = data[data["Status"] == "Left"].shape[0]

current_year = 2024
joiners = data[data["Join_Date"].dt.year == current_year].shape[0]

attrition_rate = (leavers / total_employees) * 100
new_hire_percent = (joiners / total_employees) * 100

print("Total Employees:", total_employees)
print("Active Headcount:", active)
print("Leavers:", leavers)
print("Joiners:", joiners)
print("Attrition Rate:", round(attrition_rate,2), "%")
print("New Hire %:", round(new_hire_percent,2), "%")
