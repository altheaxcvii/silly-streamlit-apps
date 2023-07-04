import streamlit as st
st.set_page_config(page_title='Rotting Mango Checker', page_icon='🥭')
st.title('Rotting Mango Checker 🥭')
st.write('Answer the questions below honestly to see if your mangoes are rotting from the inside 🤢')

# Check if the session state is already initialized
if 'state' not in st.session_state:
    st.session_state['state'] = 'first'

if 'history' not in st.session_state:
    st.session_state['history'] = []

if st.session_state['history']:
    for i in range(len(st.session_state['history'])):
        st.write(st.session_state['history'][i])

placeholder = st.empty()
placeholder.empty()

if st.session_state['state'] == 'first':
    with placeholder.container():
        st.write('Is your name Clarence?')
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Yes', key=1):
                st.session_state['history'].append('Is your name Clarence? > Yes')
                st.session_state['state'] = 'last'
                st.experimental_rerun()
        with col2:
            if st.button('No', key=2):
                st.session_state['history'].append('Is your name Clarence? > No')
                st.session_state['state'] = 'second'
                st.experimental_rerun()

if st.session_state['state'] == 'second':
    with placeholder.container():
        st.write('Did you get it for $1?')
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Yes', key=3):
                st.session_state['history'].append('Did you get it for $1? > Yes')
                st.session_state['state'] = 'last'
                st.experimental_rerun()
        with col2:
            if st.button('No', key=4):
                st.session_state['history'].append('Did you get it for $1? > No')
                st.session_state['state'] = 'third'
                st.experimental_rerun()

if st.session_state['state'] == 'third':
    with placeholder.container():
        st.write('Is it soft?')
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Yes', key=5):
                st.session_state['history'].append('Is it soft? > Yes')
                st.session_state['state'] = 'last'
                st.experimental_rerun()
        with col2:
            if st.button('No', key=6):
                st.session_state['history'].append('Is it soft? > No')
                st.session_state['state'] = 'safe'
                st.experimental_rerun()


if st.session_state['state'] == 'last':
    st.error('Mango definitely rotting', icon="⚠️")
    st.cache_resource.clear()

if st.session_state['state'] == 'safe':
    st.balloons()
    st.write('Your mango is probably safe')
    st.cache_resource.clear()