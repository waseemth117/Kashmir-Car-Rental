import streamlit as st

# App ka Title aur Icon
st.set_page_config(page_title="Kashmir Car Rental", page_icon="🚗")
st.title("🏔️ Kashmir Car Rental Service")
st.write("Tourists ke liye behtareen gadiyan aur local owners ke liye business!")

# Sirf do main options rakhe hain
menu = ["Gadi Book Karein", "Apni Gadi Rent par Dein"]
choice = st.sidebar.selectbox("Menu Chunnein", menu)

# 1. Booking Section
if choice == "Gadi Book Karein":
    st.subheader("Available Cars in Kashmir")
    st.info("🚗 Scorpio - ₹3500/day | Srinagar")
    st.info("🚗 Innova - ₹4500/day | Gulmarg")
    st.info("🚗 Swift - ₹2200/day | Pahalgam")
    
    if st.button("Abhi Book Karein"):
        st.success("Aapki request bhej di gayi hai! Hum aapse jald rabta karenge.")

# 2. Owner Registration Section
elif choice == "Apni Gadi Rent par Dein":
    st.subheader("Car Owner Registration Form")
    with st.form("OwnerForm"):
        name = st.text_input("Aapka Poora Naam")
        car_model = st.text_input("Gadi ka Model aur Number")
        rent = st.number_input("Ek din ka kiraya (₹)", min_value=500)
        phone = st.text_input("Aapka WhatsApp Number")
        submitted = st.form_submit_button("App par Dalein")
        if submitted:
            st.success(f"Shukriya {name}! Verification ke baad aapki gadi list ho jayegi.")
