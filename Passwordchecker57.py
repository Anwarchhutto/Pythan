

import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker By Anwar Chhutto", page_icon="🔑", layout="centered" ),

#custom css
st.markdown("""
    <style>
        .main{text-align: center;} 
        .stTextInput {width: 60% lmportant; margin: auto; }
        .stButton button {width: 50%; background-color green; color: white; font-size: 18px;}
        .stButton button:hover { background-color: #45a049;}
    </style>      
     """, unsafe_allow_html=True)

#page title and decription
st.title("🔐 Password Strength Generator")
st.write("Entre your password below to check its security level.🔍 ")

#function to check password strength
def check_password_strength(password):
    score = 0 
    feedback = []

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌ Password should be **atleast 8 character long**.")

if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password): # type: ignore
    score += 1 # type: ignore
else:
    feedback.append("Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.") # type: ignore

if re.search(r"\d", password):
    score += 1 
else:
    feedback.append("Password should include **at least one number (0-9) **.")

#Special characters
if re.search(r"[!@#$%^&*]", password):
    score += 1
else:
    feedback.append("❌ Include**at least one specail character (!@#$%^&*)**.")

#display password strength results
if score == 4:
    st.success("✔️ **strong password** -Your password is sesure.")
elif score == 3 :
    st.info("⚠️ **Moderate password** - Consider improving security by adding more feature")
else:
    st.error("❌**Week password** - Follow the suggestion below to strength it.")

#feedback
if feedback:
    with st.expander("**Improve your Password** "):
        for item in feedback:
            st.write(item)
password = st.text_input("Entre your password:", type= "password", help= "Ensure your password is strong 🔒")


#Button Working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please entre a password first!") #show warning if password empty
