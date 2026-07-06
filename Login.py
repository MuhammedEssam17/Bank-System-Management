import streamlit as st


def login_page(system):
    st.subheader("Login....")
    user_name = st.text_input("Enter the Username: ")
    password = st.text_input("Enter the Password: ", type="password")
    bank_name = st.selectbox("Select Bank: ", ["NBE", "CIB"])

    if st.button("Login"):
        account = system.login(user_name, bank_name, password)
        if account:
            st.session_state.account = account
            st.success(
                f"Logged in successfully to your account {user_name} with {bank_name} Bank ♥"
            )
            st.rerun()
        else:
            st.error("Invalid username or password, please try again :x:")
