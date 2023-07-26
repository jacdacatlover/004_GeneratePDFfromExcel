import pandas as pd
import glob
from fpdf import FPDF

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df=pd.read_excel(filepath,sheet_name="Sheet 1")
    pdf = FPDF()