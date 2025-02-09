import streamlit as st

st.title("Currency Converter with Wallet")

# Define exchange rates
exchange_rates = {
    'USD': {'EUR': 0.95, 'GBP': 0.82, 'JPY': 140.5, 'USD': 1, 'KRW': 1300},
    'EUR': {'USD': 1.05, 'GBP': 0.86, 'JPY': 147.9, 'EUR': 1, 'KRW': 1365},
    'GBP': {'USD': 1.22, 'EUR': 1.16, 'JPY': 171.8, 'GBP': 1, 'KRW': 1583},
    'JPY': {'USD': 0.0071, 'EUR': 0.0068, 'GBP': 0.0058, 'JPY': 1, 'KRW': 9.2},
    'KRW': {'USD': 0.00077, 'EUR': 0.00073, 'GBP': 0.00063, 'JPY': 0.11, 'KRW': 1}
}

# Initialize wallet in session state if it does not exist
if 'wallet' not in st.session_state:
    st.session_state['wallet'] = {currency: 0 for currency in exchange_rates}

# Operations: Deposit, Withdraw, Exchange
operation = st.selectbox("Choose Operation", ("deposit", "withdraw", "exchange"))
amount = st.number_input("Amount", min_value=0.0, format="%f")
currency = st.selectbox("Currency", options=list(exchange_rates.keys()))

if operation == "exchange":
    target_currency = st.selectbox("Target Currency", options=list(exchange_rates.keys()))
    if st.button("Execute Exchange"):
        pass
        # TODO
else:
    if st.button(f"{operation.title()} {amount} {currency}"):
        if operation == "deposit":
            pass
            # TODO
        elif operation == "withdraw":
            pass
            # TODO

# Wallet display
st.subheader("Your Wallet")
for currency, amount in st.session_state['wallet'].items():
    st.write(f"{currency}: {amount}")
