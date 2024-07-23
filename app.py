import json
import streamlit as st
import os
from langchain_community.vectorstores.upstash import UpstashVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from dotenv import load_dotenv # Add
load_dotenv() # Add

embeddings = OpenAIEmbeddings()

store = UpstashVectorStore(
    embedding=embeddings
)

def add_structured_documents(data):
    document = Document(
        page_content=data["Description"],
        metadata={
            "title": data["Title"],
            "type": data["Type"],
            "price": data["Price"],
            "tags": data["Tags"],
            "attributes": data["Attributes"]
        }
    )
    store.add_documents([document])
    print("structured documents are inserted succesfully")
def add_free_documents(data):
    document = Document(
        page_content=data["Content"],
        metadata={
            "title": data["Title"],
            "url": data["url"],
            "image_url": data["image_url"]
        }
    )
    store.add_documents([document])
    print("free documents are inserted successfully")
def add_field():
    if 'fields' not in st.session_state:
        st.session_state['fields'] = [{'key': '', 'value': ''}]
    else:
        st.session_state['fields'].append({'key': '', 'value': ''})

# Function to delete the last field in the custom form
def delete_field():
    if 'fields' in st.session_state and st.session_state['fields']:
        st.session_state['fields'].pop()

st.title("Manage Data")

# Structured Data Section
st.header("Structured Data")
with st.form(key='structured_data_form'):
    data_type = st.text_input("Type")
    price = st.text_input("Price")
    title = st.text_input("Title")
    description = st.text_input("Description")
    tags = st.text_input("Tags (Keywords)")
    attributes = st.text_input("Attributes")
    submit_button = st.form_submit_button(label='Submit Structured Data')

if submit_button:
    # Function to map inputs into key-value pairs and convert to JSON
    structured_data = {
        "Type": data_type,
        "Price": price,
        "Title": title,
        "Description": description,
        "Tags": tags,
        "Attributes": attributes
    }    
    add_structured_documents(structured_data)
    
    json_data = json.dumps(structured_data, indent=4)
    st.json(json_data)

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
    custom_data = {field['key']: field['value'] for field in st.session_state['fields'] if field['key'] and field['value']}
    custom_json_data = json.dumps(custom_data, indent=4)
    st.json(custom_json_data)

# Free Section
st.header("Free")
with st.form(key='free_form'):
    free_title = st.text_input("Title")
    free_textarea = st.text_input("Content")
    free_url = st.text_input("URL")
    free_img = st.text_input("Image URL")


    free_submit_button = st.form_submit_button(label='Submit Free Data')

if free_submit_button:
    free_data = {
        "Title": free_title,
        "Content": free_textarea,
        "url" : free_url,
        "image_url":free_img
    }
    free_json_data = json.dumps(free_data, indent=4)
    st.json(free_json_data)
