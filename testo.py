import streamlit as st

# Function to add a new field to the custom form
def add_field():
    if 'fields' not in st.session_state:
        st.session_state['fields'] = [{'key': '', 'value': ''}]
    else:
        st.session_state['fields'].append({'key': '', 'value': ''})

# Function to delete the last field in the custom form
def delete_field():
    if 'fields' in st.session_state and st.session_state['fields']:
        st.session_state['fields'].pop()

st.title("Streamlit Form Example")

# Structured Data Section
st.header("Structured Data")
with st.form(key='structured_data_form'):
    type = st.text_input("Title")
    price = st.text_input("Price")
    title = st.text_input("Title")
    description = st.text_input("Description")
    tags = st.text_input("Tags (Keywords)")
    attributes = st.text_input("Attributes")
    submit_button = st.form_submit_button(label='Submit Structured Data')

if submit_button:
    st.write(f"Price: {price}, Title: {title}")

# Custom Section
st.header("Custom")
add_field_button = st.button(label="Add Field", on_click=add_field)
delete_field_button = st.button(label="Delete Field", on_click=delete_field)

if 'fields' not in st.session_state:
    st.session_state['fields'] = []

custom_form = st.form(key='custom_form')
for i, field in enumerate(st.session_state['fields']):
    key = custom_form.text_input(f"Key {i+1}", value=field['key'], key=f'key_{i}')
    value = custom_form.text_input(f"Value {i+1}", value=field['value'], key=f'value_{i}')
    st.session_state['fields'][i] = {'key': key, 'value': value}

custom_submit_button = custom_form.form_submit_button(label='Submit Custom Data')

if custom_submit_button:
    st.write("Custom Data:")
    for field in st.session_state['fields']:
        st.write(f"{field['key']}: {field['value']}")

# Free Section
st.header("Free")
with st.form(key='free_form'):
    free_title = st.text_input("Title")
    free_subtitle = st.text_input("Subtitle")
    free_submit_button = st.form_submit_button(label='Submit Free Data')

if free_submit_button:
    st.write(f"Title: {free_title}, Subtitle: {free_subtitle}")
