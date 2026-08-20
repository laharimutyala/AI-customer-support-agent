import streamlit as st
import requests

st.set_page_config(
    page_title="AI Customer Support",
    page_icon="🤖",
    layout="centered"
)

# -----------------------
# Session State
# -----------------------
if "customer" not in st.session_state:
    st.session_state.customer = ""

if "issue" not in st.session_state:
    st.session_state.issue = ""

if "response_data" not in st.session_state:
    st.session_state.response_data = None


# -----------------------
# Title
# -----------------------
st.title(" AI Customer Support Agent")
st.write("Need help? Describe your issue and our AI assistant will assist you.")

st.divider()

# -----------------------
# Input Form
# -----------------------
customer = st.text_input(
    "Customer Name",
    key="customer"
)

issue = st.text_area(
    "Describe your issue",
    height=150,
    key="issue"
)

# -----------------------
# Submit
# -----------------------
if st.button("Submit Ticket", use_container_width=True):

    if customer.strip() == "" or issue.strip() == "":
        st.warning("Please fill all the fields.")
    else:

        with st.spinner("Generating AI response..."):

            response = requests.post(
                "http://127.0.0.1:8000/tickets",
                json={
                    "customer": customer,
                    "issue": issue
                }
            )

            if response.status_code == 200:
                st.session_state.response_data = response.json()
            else:
                st.error("Unable to connect to server.")

# -----------------------
# Show AI Response
# -----------------------
if st.session_state.response_data is not None:

    data = st.session_state.response_data

    st.success("✅ Your request has been submitted successfully!")

    st.markdown("## 🤖 AI Assistant")

    st.info(data["response"])

    st.write("")

    if st.button("➕ CLEAR", use_container_width=True):  

        st.session_state.clear()
        st.rerun()