import pandas as pd 
import numpy as np 

INR = 1.1
Medication = "Warfin to treat and prevent blood clots"
INRLevels = ["low", 0.8, 1.1, 1.5, 2.0, 2.5, 3.0, 3.5, "high"]
Patient = {
    "Age": 18, 
    "Name": "Peter Piper",
    "Gender": "Male",
    "Visits": ["2/4/2005", "4/23/2019", "6/8/2020", "3/27/2022"],
    "Test-Results": {
        "ABO": "A Positive",
        "SCN": "Negative",
        "Hemoglobin": 16.0, 
    }
}

print (INR)
print (Medication)
print (INRLevels)
print (Patient)
