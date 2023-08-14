# health-analytics
This repository is a Python coding exercise assignment for HHA 506 where I will be working with GitHub, Google Shell, and Python. In this project I will be creating a new repository, cloning it to a Google Shell environment where I will write a Python program and push the code back to GitHub.

## Variables, Lists, and Dictionary 
Utilizing a number variable, string variable, and a list I created a fake INR test result for a patient who is taking Warfin. The INR lab result is the number variable. The string variabe is the medication the patient is on which is Warfin, which requires INR monitoring. Lastly the list contained INR values from low to high, so the patient can see where their test result lies. 
Using a dictionary I created a mock patient profile which included their personal information, lab results, past visits, etc.  

## Function 
Utilizing a function I created a transfusion predictor which predicts if a patient will have to underego a transfusion based off of their hemoglobin and platelet counts. If the patient has a hemoglobin value less than or equal to 11 the transfusion predictor will predict/print that the patient needs a blood transfusion or else that they don't need a blood transfusion. If the patient has a platelet value less than or equal to 5,000 the transfusion predictor will predict/print that the patient needs a platelet transfusion or else that they don't need a platelet transfusion. With the example provided in this code the patient has a hemoglobin value of 16 and a platelet count of 10,000. When these values of the variables hemoglobin and platelts are inputted into the function it should output "Transfusion Predictor: ['do not need a blood transfusion', 'do not need a platelet transfusion']". For the second example provided in this code the patient has a hemoglobin value of 7 and a platelet count of 25,000. When theses values for these variables are inputted into the function the output should be Transfusion Predictor: ['need a blood transfusion', 'do not need a platelet transfusion']. 