import streamlit as st


def creat_acc(system):
    st.subheader("let's create your account......")
    new_user = st.text_input("Enter your username: ")
    new_password = st.text_input("Enter your password: ", type="password")
    new_bank = st.selectbox("Select your bank: ", ["NBE", "CIB"])
    initial_balance = st.number_input(
        "Enter your initial balance: ",
        min_value=0.0,
        max_value=1000000.0,
        step=100.0,
    )
    if st.button("Create account"):
        if new_user and new_password:
            system.create_account(new_user, new_bank, new_password, initial_balance)
            st.success(
                "your account created successfully, you can now login to your account anytime"
            )
        else:
            st.warning(
                "please fill in all fields to create your account with out any problems :warning:"
            )
