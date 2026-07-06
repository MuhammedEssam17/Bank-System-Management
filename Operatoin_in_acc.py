import streamlit as st


def opperation_page(account, system):
    st.sidebar.write(f"user: {account.user_name}")
    st.sidebar.write(f"bank: {account.bank_name}")

    if st.sidebar.button("Logout"):
        st.session_state.account = None
        st.rerun()
    st.subheader("Account Operatoins: ")
    operation = st.selectbox(
        "Choose and operation: ",
        ["Check Accnount and Inof", "Deposit", "Withdrwas", "Delete Account"],
    )
    if operation == "Check Accnount and Inof":
        st.info("Account Information: ")
        st.write(f"user name {account.user_name}")
        st.write(f"bank name {account.bank_name }")
        st.write(f"balance {account.balance}")

    elif operation == "Deposit":
        deposit_amount = st.number_input(
            "Enter the amount to deposit: ",
            min_value=0.0,
            max_value=10000000.0,
            step=100.0,
        )
        st.write(f"you have in your balance {account.balance}"),
        if st.button("Confirm Deposit"):
            if deposit_amount > 0:
                try:
                    account.deposit(deposit_amount)
                    system.update_balance(account)
                    st.success(
                        f"{deposit_amount} deposited successfully, your new balance is {account.balance}"
                    )
                except ValueError:
                    st.warning(f"your balance is {account.balance}:x:")
            else:
                st.warning("please enter a valid amount to deposit :warning:")

    elif operation == "Withdrwas":
        withdraw_amount = st.number_input(
            "Enter the amount to withdraw: ",
            min_value=0.0,
            max_value=1000000.0,
            step=100.0,
        )
        st.write(f"you have in your balance {account.balance}"),
        if st.button("Confirm Withdraw"):
            if withdraw_amount > 0:
                try:
                    account.withdrawl(withdraw_amount)
                    system.update_balance(account)
                    st.success(
                        f"{withdraw_amount} withdrawn successfully, your new balance is {account.balance}"
                    )
                except ValueError:
                    st.warning(f"your balance is {account.balance}:x:")
            else:
                st.warning("please enter a valid amount to withdraw :warning:")

    elif operation == "Delete Account":
        st.warning("Are you sure you want to delete your account? :warning:")
        confirmation = st.selectbox(
            "Select an option: ", ["Yes, delete my account", "No, keep my account"]
        )
        if st.button("Confirm"):
            if confirmation == "Yes, delete my account":
                system.delete_account(account)
                st.session_state.account = None
                st.success(
                    "your account has been deleted successfully :white_check_mark:"
                )

            else:
                st.info("your account is safe ")
