
# Import necessary libraries for different Auto-EDA libraries
import pandas as pd
import sweetviz as sv
from pandas_profiling import ProfileReport
from autoviz.AutoViz_Class import AutoViz_Class
from dataprep.eda import create_report
import dtale

# Load the dataset
file_path = 'data_3.xlsx'  # Ensure the file is in the correct directory
data = pd.read_excel(file_path)

# 1. SweetViz EDA
def sweetviz_report(data):
    report = sv.analyze(data)
    report.show_html('sweetviz_report.html')

# 2. Pandas Profiling EDA
def pandas_profiling_report(data):
    profile = ProfileReport(data, title="Pandas Profiling EDA Report", explorative=True)
    profile.to_file('pandas_profiling_report.html')

# 3. AutoViz EDA
def autoviz_report(file_path):
    AV = AutoViz_Class()
    df_autoviz = AV.AutoViz(file_path, sep=',')

# 4. Dataprep EDA
def dataprep_report(data):
    report = create_report(data)
    report.show_browser()

# 5. D-Tale EDA
def dtale_report(data):
    d = dtale.show(data)
    d.open_browser()

# Call each function for Auto-EDA

# SweetViz EDA
sweetviz_report(data)

# Pandas Profiling EDA
pandas_profiling_report(data)

# AutoViz EDA
autoviz_report(file_path)

# Dataprep EDA
dataprep_report(data)

# D-Tale EDA
dtale_report(data)
