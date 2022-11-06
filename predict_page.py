
import streamlit as st
import pickle  
import numpy as np

def load_model():
    with open('Predict_model.pkl', 'rb') as file:
        data = pickle.load(file)  
        rfst_loaded=data["model"]  
    return rfst_loaded

Mode=load_model()

def show_predict_page():
    st.title("""Activity Recognition""")
    st.write("""We need some information to recognize the activity""")
    st.write("""So please fill this form""")

    alx=st.number_input("alx",step=1.,format="%.6f")
    st.write('The current number is ', alx)
    aly=st.number_input("aly",step=1.,format="%.6f")
    st.write('The current number is ', aly)
    alz=st.number_input("alz",step=1.,format="%.6f")
    st.write('The current number is ', alz)
    glx=st.number_input("glx",step=1.,format="%.6f")
    st.write('The current number is ', glx)
    gly=st.number_input("gly",step=1.,format="%.6f")
    st.write('The current number is ', gly)
    glz=st.number_input("glz",step=1.,format="%.6f")
    st.write('The current number is ', glz)
    arx=st.number_input("arx",step=1.,format="%.6f")
    st.write('The current number is ', arx)
    ary=st.number_input("ary",step=1.,format="%.6f")
    st.write('The current number is ', ary)
    arz=st.number_input("arz",step=1.,format="%.6f")
    st.write('The current number is ', arz)
    grx=st.number_input("grx",step=1.,format="%.6f")
    st.write('The current number is ', grx)       
    gry=st.number_input("gry",step=1.,format="%.6f")
    st.write('The current number is ', gry)
    grz=st.number_input("grz",step=1.,format="%.6f")
    st.write('The current number is ', grz)


    ok=st.button("Predict")
    if ok:
        X=[[alx,aly,alz,glx,gly,glz,arx,ary,arz,grx,gry,grz]]
        # _loaded = data["model"]
        Prediction=Mode.predict(X)
        if Prediction[0]==0:
            st.subheader(f"No activity")
        elif Prediction[0]==1:
            st.subheader(f"Standing still (1 min)")
        elif Prediction[0]==2:
            st.subheader(f"setting and relaxing (1 min) ")
        elif Prediction[0]==3:
            st.subheader(f"Lying down (1 min) ")
        elif Prediction[0]==4:
            st.subheader(f"walking (1 min) ")
        elif Prediction[0]==5:
            st.subheader(f"Climbing stairs (1 min) ")
        elif Prediction[0]==6:
            st.subheader(f"Waist bends forward (20x) ")
        elif Prediction[0]==7:
            st.subheader(f"Frontal elevation of arms (20x) ")
        elif Prediction[0]==8:
            st.subheader(f"Knees bending (crouching) (20x) ")
        elif Prediction[0]==9:
            st.subheader(f"Cycling (1 min) ")
        elif Prediction[0]==10:
            st.subheader(f"Jogging (1 min) ") 
        elif Prediction[0]==11:
            st.subheader(f"Running (1 min) ")  
        elif Prediction[0]==12:
            st.subheader(f"Jump front & back (20x) ")  



        st.subheader(f"Prediction of the activity is {Prediction[0]}")