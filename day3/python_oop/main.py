import streamlit as st
from libs import Library, Member

st.title("Library Management System")

if "library" not in st.session_state:
    st.session_state.library = Library("My Library")

page = st.sidebar.selectbox("Menu", ["Add Member", "Manage Membership", "View Members"])

if page == 'Add Member':
    st.write("### Add Member")
    name = st.text_input("Name: ")
    button = st.button("Add Member")

    if button:
        new_member = Member(name)
        st.session_state.library.register_member(new_member)
        st.rerun()

elif page == "Manage Membership":
    st.write("### Manage Membership")

    for index, member in enumerate(st.session_state.library.members):
        status = "Active" if member.is_active else "Deactive"
        st.write(f"{member.name} - {status}")
        deactivate_btn = st.button("Deactivate", key=f"deactivate_{index}")

        if deactivate_btn:
            member.deactivate()
            st.rerun()

elif page == "View Members":
    if not st.session_state.library.members:
        st.write('No Current Active Members')
    else:
        active_members = st.session_state.library.get_active_members()
        for member in active_members:
            st.write(member.name)