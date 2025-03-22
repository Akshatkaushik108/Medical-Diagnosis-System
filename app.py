import streamlit as st
import pickle
from streamlit_option_menu import option_menu 


st.set_page_config(page_title="Disease Prediction", page_icon="🩺")

#ofh


models = {
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'alzheimers': pickle.load(open('Models/alzheimers_model.sav', 'rb')),
}

with st.sidebar:
    selected = option_menu('Select a Disease to predict',
    ['Alzheimers Prediction',
     'Heart Disease Prediction',
     'Parkinsons Prediction']
)

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)
#Alzheimers
if selected == 'Alzheimers Prediction':
    st.title('Alzheimers')
    st.write("Enter the following details to predict Alzheimers:")

    Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')
    Gender = display_input('Gender', 'Enter gender (0 for Male, 1 for Female)', 'Gender', 'number')
    Ethnicity = display_input('Ethnicity (0: Caucasian, 1: African American, 2: Asian, 3: Other)', 'Enter ethnicity code', 'Ethnicity', 'number')
    EducationLevel = display_input('Education Level(0: None, 1: High School, 2: Bachelor`s, 3: Higher)', 'Enter education level (0 to 10)', 'EducationLevel', 'number')
    BMI = display_input('Body Mass Index', 'Enter BMI of the person (range 15 to 40)', 'BMI', 'number')
    Smoking = display_input('Smoking', 'Enter 1 if the person smokes, 0 otherwise', 'Smoking', 'number')
    AlcoholConsumption = display_input('Alcohol Consumption', 'Weekly alcohol consumption in units', 'AlcoholConsumption', 'number')
    PhysicalActivity = display_input('Physical Activity', 'Weekly physical activity in hours', 'PhysicalActivity', 'number')
    DietQuality = display_input('Diet Quality', 'Diet quality score (0 to 10)', 'DietQuality', 'number')
    SleepQuality = display_input('Sleep Quality', 'Sleep quality score', 'SleepQuality', 'number')
    FamilyHistoryAlzheimers = display_input('Family History of Alzheimer’s', 'Enter 1 if there is a family history, 0 otherwise', 'FamilyHistoryAlzheimers', 'number')
    CardiovascularDisease = display_input('Cardiovascular Disease', 'Enter 1 if the person has cardiovascular disease, 0 otherwise', 'CardiovascularDisease', 'number')
    Diabetes = display_input('Diabetes', 'Enter 1 if the person has diabetes, 0 otherwise', 'Diabetes', 'number')
    Depression = display_input('Depression', 'Enter 1 if the person has depression, 0 otherwise', 'Depression', 'number')
    HeadInjury = display_input('Head Injury', 'Enter 1 if the person has had a head injury, 0 otherwise', 'HeadInjury', 'number')
    Hypertension = display_input('Hypertension', 'Enter 1 if the person has hypertension, 0 otherwise', 'Hypertension', 'number')
    SystolicBP = display_input('Systolic Blood Pressure', 'Enter Systolic BP (mmHg)', 'SystolicBP', 'number')
    DiastolicBP = display_input('Diastolic Blood Pressure', 'Enter Diastolic BP (mmHg)', 'DiastolicBP', 'number')
    CholesterolTotal = display_input('Total Cholesterol', 'Total cholesterol levels (mg/dL)', 'CholesterolTotal', 'number')
    CholesterolLDL = display_input('Cholesterol LDL', 'Low-density lipoprotein cholesterol levels (mg/dL)', 'CholesterolLDL', 'number')
    CholesterolHDL = display_input('Cholesterol HDL', 'High-density lipoprotein cholesterol levels (mg/dL)', 'CholesterolHDL', 'number')
    CholesterolTriglycerides = display_input('Triglycerides', 'Triglyceride levels (mg/dL)', 'CholesterolTriglycerides', 'number')
    MMSE = display_input('Mini-Mental State Examination', 'MMSE score (range 0 to 30)', 'MMSE', 'number')
    FunctionalAssessment = display_input('Functional Assessment', 'Functional assessment score (range 0 to 10)', 'FunctionalAssessment', 'number')
    MemoryComplaints = display_input('Memory Complaints', 'Enter 1 if the person has memory complaints, 0 otherwise', 'MemoryComplaints', 'number')
    BehavioralProblems = display_input('Behavioral Problems', 'Enter 1 if the person has behavioral problems, 0 otherwise', 'BehavioralProblems', 'number')
    ADL = display_input('Activities of Daily Living', 'ADL score (range 0 to 10)', 'ADL', 'number')
    Confusion = display_input('Confusion', 'Enter 1 if the person experiences confusion, 0 otherwise', 'Confusion', 'number')
    Disorientation = display_input('Disorientation', 'Enter 1 if the person experiences disorientation, 0 otherwise', 'Disorientation', 'number')
    PersonalityChanges = display_input('Personality Changes', 'Enter 1 if the person has personality changes, 0 otherwise', 'PersonalityChanges', 'number')
    DifficultyCompletingTasks = display_input('Difficulty Completing Tasks', 'Enter 1 if the person has difficulty completing tasks, 0 otherwise', 'DifficultyCompletingTasks', 'number')
    Forgetfulness = display_input('Forgetfulness', 'Enter 1 if the person experiences forgetfulness, 0 otherwise', 'Forgetfulness', 'number')


    alzheimers_diagnosis = ''
    if st.button('Alzheimers Test Result'):
        alzheimer_prediction = models['alzheimers'].predict([[Age, Gender, Ethnicity, EducationLevel, BMI, Smoking, AlcoholConsumption, PhysicalActivity, DietQuality, SleepQuality,
                                                              FamilyHistoryAlzheimers, CardiovascularDisease, Diabetes, Depression, HeadInjury, Hypertension,  
                                                              SystolicBP, DiastolicBP, CholesterolTotal, CholesterolLDL, CholesterolHDL, CholesterolTriglycerides, 
                                                              MMSE, FunctionalAssessment, MemoryComplaints, BehavioralProblems, ADL, Confusion, Disorientation, PersonalityChanges,
                                                              DifficultyCompletingTasks, Forgetfulness]])
        alzheimers_diagnosis = 'The person has alzheimers' if alzheimer_prediction[0] == 1 else 'The person does not have alzheimers'
        st.success(alzheimers_diagnosis)
#Heart
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease')
    st.write("Enter the following details to predict heart disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
    cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
    restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
    thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
    exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
    oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
    slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
    ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
    thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.success(heart_diagnosis)
#Parkinson
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease")
    st.write("Enter the following details to predict Parkinson's disease:")

    fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
    fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
    flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
    Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
    Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
    RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
    PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
    DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
    Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
    Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
    APQ3 = display_input('Shimmer:APQ3', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
    APQ5 = display_input('Shimmer:APQ5', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
    APQ = display_input('MDVP:APQ', 'Enter MDVP:APQ value', 'APQ', 'number')
    DDA = display_input('Shimmer:DDA', 'Enter Shimmer:DDA value', 'DDA', 'number')
    NHR = display_input('NHR', 'Enter NHR value', 'NHR', 'number')
    HNR = display_input('HNR', 'Enter HNR value', 'HNR', 'number')
    RPDE = display_input('RPDE', 'Enter RPDE value', 'RPDE', 'number')
    DFA = display_input('DFA', 'Enter DFA value', 'DFA', 'number')
    spread1 = display_input('Spread1', 'Enter spread1 value', 'spread1', 'number')
    spread2 = display_input('Spread2', 'Enter spread2 value', 'spread2', 'number')
    D2 = display_input('D2', 'Enter D2 value', 'D2', 'number')
    PPE = display_input('PPE', 'Enter PPE value', 'PPE', 'number')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)
