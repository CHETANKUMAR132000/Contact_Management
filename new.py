# app.py

import streamlit as st
from bst import ContactBST

# Initialize the Binary Search Tree for contacts
contact_bst = ContactBST()

# Streamlit App
st.title("Contact Management System")

# Tabs for different functionalities
tab1, tab2, tab3, tab4 = st.tabs(["Add Contact", "Display Contacts", "Search Contact", "Delete Contact"])

# 1. Add Contact
with tab1:
    st.header("Add a New Contact")
    contact_name = st.text_input("Enter contact name")
    if st.button("Add Contact"):
        if contact_name:
            contact_bst.insert(contact_name)
            st.success(f"Contact '{contact_name}' added!")
        else:
            st.error("Please enter a valid name.")

# 2. Display Contacts
with tab2:
    st.header("All Contacts")
    contacts = contact_bst.display_contacts()
    if contacts:
        st.write("Contacts in alphabetical order:")
        st.write(contacts)
    else:
        st.write("No contacts to display.")

# 3. Search Contact
with tab3:
    st.header("Search for a Contact")
    search_name = st.text_input("Enter contact name to search")
    if st.button("Search Contact"):
        if search_name:
            found = contact_bst.search(search_name)
            if found:
                st.success(f"Contact '{search_name}' found!")
            else:
                st.error(f"Contact '{search_name}' not found.")
        else:
            st.error("Please enter a valid name.")

# 4. Delete Contact
with tab4:
    st.header("Delete a Contact")
    delete_name = st.text_input("Enter contact name to delete")
    if st.button("Delete Contact"):
        if delete_name:
            contact_bst.delete(delete_name)
            st.success(f"Contact '{delete_name}' deleted!")
        else:
            st.error("Please enter a valid name.")
