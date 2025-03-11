import streamlit as st
import re
import random
import string

st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔐",
    layout="centered",
    menu_items={
        'About': """
        **Password Strength Meter App**  
        Built with ❤️ by Abubakar Siddique  
        📧 Email: a3123080192@gmail.com  
        📞 Contact: +92 312 3080192
        """
    }
)

st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    
    .title {
        color: #0073e6;
    }
    
    .stButton > button {
        background-color: #0073e6;
        color: white;
    }
    </style>
    """,
      unsafe_allow_html=True)

st.sidebar.title("Instructions")
st.sidebar.write("""
1. Enter your password in the text field.
2. Click **Check Password Strength** to evaluate your password.
3. If the password is weak, you'll receive suggestions for improvements.
4. Use the **Generate Strong Password** button to get a secure password suggestion.
""")

def check_password(password):
    
    score = 0
    feedback = []
    common_passwords = [
    "123456", "password", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123", "password1", "111111",
    "123123", "admin", "letmein", "welcome", "monkey", "1234", "sunshine", "iloveyou", "princess", "football",
    "charlie", "donald", "dragon", "baseball", "trustno1", "shadow", "superman", "hello", "freedom", "whatever",
    "master", "qwertyuiop", "654321", "jordan23", "robert", "michael", "hunter", "buster", "thomas", "jennifer",
    "121212", "soccer", "killer", "george", "harley", "maggie", "flower", "starwars", "cheese", "computer",
    "internet", "access", "pepper", "summer", "ashley", "nicole", "daniel", "andrew", "biteme", "ginger",
    "batman", "matrix", "pokemon", "liverpool", "sparky", "mickey", "tigger", "joshua", "love", "whatever1",
    "merlin", "carlos", "snoopy", "banana", "chocolate", "blink182", "cookie", "naruto", "letmein123", "mustang",
    "dragonball", "skate", "asdfgh", "hunter2", "welcome1", "passw0rd", "zaq12wsx", "star", "yamaha", "testing",
    "babygirl", "babygirl1", "trustme", "nintendo", "startrek", "google", "123qwe", "iloveyou1", "dolphin", "pass123",
    "jackson", "oliver", "chris", "austin", "victory"
]

    if password.lower() in common_passwords:
        feedback.append("This password is too common. Please choose a less common password.")
        return 0, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    if len(password) >= 12:
        score += 1

    return score, feedback

def password_strength_category(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"

def generate_password(length=14):
    if length < 12:
        length = 12  

    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*")
    
    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    remaining_chars = random.choices(all_chars, k=remaining_length)
    
    password_list = [uppercase, lowercase, digit, special] + remaining_chars
    random.shuffle(password_list)
    return "".join(password_list)


st.title("🔐 Password Strength Meter")
st.subheader("Need to check the strength of your password?")

user_password = st.text_input("Enter your password", type="password")

if st.button("Check Password Strength"):
    if user_password:
        score, feedback = check_password(user_password)
        category = password_strength_category(score)
        st.write(f"**Strength Score:** {score}/5")
        st.write(f"**Password Category:** {category}")
        
        if category == "Weak":
            st.error("Your password is weak. Suggestions:")
            for tip in feedback:
                st.write("- " + tip)
        elif category == "Moderate":
            st.warning("Your password is moderate. Consider these improvements:")
            for tip in feedback:
                st.write("- " + tip)
        else:
            st.success("Your password is strong!")
    else:
        st.info("Please enter a password to check its strength.")

st.write("---")
st.write("### Need a Strong Password?")

if st.button("Generate Strong Password"):
    new_password = generate_password(14)
    st.code(new_password, language=None)
