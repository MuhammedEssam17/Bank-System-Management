from Bank_system import Bank_System
import streamlit as st

st.set_page_config(
    page_title="Bank System", page_icon=":money_with_wings:", layout="centered"
)

if "system" not in st.session_state:
    st.session_state.system = Bank_System()

if "account" not in st.session_state:
    st.session_state.account = None

system = st.session_state.system

from Login import login_page
from Regestier import creat_acc

st.title("Bank System")
st.markdown("---------------")

if st.session_state.account is None:
    menu = st.sidebar.radio("Main Menu", ["Login", "Create Account"])

    if menu == "Login":
        login_page(system)

    elif menu == "Create Account":
        creat_acc(system)

else:
    account = st.session_state.account
    from Operatoin_in_acc import opperation_page

    opperation_page(account, system)
