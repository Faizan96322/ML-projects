import numpy as np
import pickle
import streamlit as st


#loading the saved model
loaded_model = pickle.load(open('/Users/faizansyed/PycharmProjects/Streamlit-ML/trained_model.sav', 'rb'))

def diabetes_prediction(input_data):


    #converting list to np array
    input_data_to_np = np.asarray(input_data)

    #reshaping
    input_data_reshape = input_data_to_np.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)

    if(prediction[0] == 0):
      return"Hurray you dont have diabetes!! :-}"
    else:
      return "Iam very sorry to say this But, you have diabetes '_',"


def main():
    #Title of the webpage
    st.title('Diabetes Prediction Web App')

    #getting inputs from the user
    Pregnancies = st.text_input("Number of Pregnancies : ")
    Glucose = st.text_input("Glucose Level : ")
    BloodPressure =st.text_input("Blood Pressure value : ")
    SKinThickness = st.text_input("Skin Thickness : ")
    Insulin = st.text_input("Insulin Level : ")
    BMI = st.text_input("BMI value : ")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value  : ")
    Age = st.text_input("Age of the person : ")

    #PREDICTION:

    diagonisis = ''

    if st.button("Diabetes Test Result"):
        diagonisis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SKinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

        st.success(diagonisis)

if __name__ == '__main__':
    main()


