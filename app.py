import streamlit as st

def uiInput():
    st.subheader("UI Based Input")
    return None

def configInput():
    st.subheader("Config Based Input")

def main():
    st.title("Without Sample Sythetic Data Generation")

    input_config = "Config File (YAML)"
    input_ui = "UI"

    input_method = st.selectbox("Choose your preferred input method", [input_config, input_ui])

    config = {}

    
    if input_method == input_config:
        config = configInput()
    if input_method == input_ui:
        config = uiInput()

    if config:
        start_generate = st.button("Generate")

        if start_generate:

            # TODO: get data from generator and show the data, visualize and provide download
            pass

if __name__=="__main__":
    main()