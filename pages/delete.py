import json
import streamlit as st
from upstash_vector import Index

# Initialize the Index
index = Index(
    url="https://cheerful-anchovy-80923-us1-vector.upstash.io",
    token="ABoFMGNoZWVyZnVsLWFuY2hvdnktODA5MjMtdXMxYWRtaW5aVFZqWkdZM016Y3RPRE5qWlMwMFpHWXlMV0UwWlRBdE9XVmpNMkl4Wm1NMVlqRTI=",
)

# Fetch all data function
def fetch_data():
    cursor = "0"
    results = []
    while True:
        response = index.range(cursor=cursor, limit=100, include_metadata=True)
        results.extend(response.vectors)
        cursor = response.next_cursor
        if cursor == "":
            break
    return results

# Delete vector function
def delete_vector(vector_id):
    response = index.delete(vector_id)
    print("a9wad response fl3alam l3arabi ochar9 l'awsat")
    print(response)
    return response

# Streamlit app
st.title("Upstash Vectors Data")

if "data_fetched" not in st.session_state:
    st.session_state.data_fetched = False

def refresh_data():
    st.session_state.data_fetched = True
    st.session_state.results = fetch_data()

if st.button('Fetch Data') or st.session_state.data_fetched:
    refresh_data()
    results = st.session_state.results
    if results:
        st.write("Total Vectors:", len(results))
        for vector in results:
            title = vector.metadata.get("title", vector.metadata.get("Título", "No Title"))
            with st.expander(title):
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(label="View More", key="Id" + vector.id):
                        st.write(json.dumps(vector.metadata, indent=4))
                with col2:
                    if st.button(label="Delete", key="del_" + vector.id):
                        response = delete_vector(vector.id)
                        if response.deleted:
                            st.write(f"Vector {vector.id} deleted successfully.")
                            # Refresh data after deletion
                            refresh_data()
                        else:
                            st.write(f"Failed to delete vector {vector.id}.")
    else:
        st.write("No data found.")
