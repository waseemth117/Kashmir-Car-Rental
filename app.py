import streamlit as st
import urllib.parse

st.set_page_config(page_title="Kashmir Car Rental", page_icon="🚗")

# Aapka Number aur Message setup
phone_number = "916005669944" #

st.title("🏔️ Kashmir Car Rental Service")
st.write("Tourists ke liye behtareen gadiyan aur local owners ke liye business!")

menu = ["Gadi Book Karein", "Apni Gadi Rent par Dein"]
choice = st.sidebar.selectbox("Menu Chunnein", menu)

if choice == "Gadi Book Karein":
    st.subheader("Available Cars in Kashmir")
    
    cars = [
        {"name": "Scorpio", "price": "3500", "loc": "Srinagar"},
        {"name": "Innova", "price": "4500", "loc": "Gulmarg"},
        {"name": "Swift", "price": "2200", "loc": "Pahalgam"}
    ]

    for car in cars:
        with st.container():
            st.write(f"### {car['name']}")
            st.write(f"Price: ₹{car['price']}/day | Location: {car['loc']}")
            
            # WhatsApp link banana
            msg = f"Hello, mujhe aapki app se {car['name']} book karni hai. Location: {car['loc']}"
            encoded_msg = urllib.parse.quote(msg)
            whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_msg}"
            
            st.markdown(f'''<a href="{whatsapp_url}" target="_blank">
                <button style="background-color: #25D366; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">
                WhatsApp par Book Karein
                </button></a>''', unsafe_local_html=True)
            st.write("---")

elif choice == "Apni Gadi Rent par Dein":
    st.subheader("Owner Registration Form")
    with st.form("OwnerForm"):
        name = st.text_input("Aapka Naam")
        car_model = st.text_input("Gadi ka Model")
        rent = st.number_input("Ek din ka kiraya (₹)", min_value=500)
        submitted = st.form_submit_button("Submit Details")
        if submitted:
            st.success("Shukriya! Hum aapse jald rabta karenge.")
