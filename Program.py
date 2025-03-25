import streamlit as st
import google.generativeai as genai

st.title("Grammar Checker with Gemini AI")

# User enters their own API key
api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    try:
        # Configure Gemini API
        genai.configure(api_key=api_key)
        
        # Store API key in session state (for temporary use)
        st.session_state["gemini_api_key"] = api_key

        st.success("API Key Loaded Successfully (not displayed for security)")
    except Exception as e:
        st.error(f"Invalid API Key: {e}")

# Text input for user to check grammar
user_input = st.text_area("Enter your text:", height=150)

if st.button("Check Grammar"):
    if not api_key:
        st.error("Please enter a valid API Key first!")
    elif user_input.strip():
        try:
            # Using the correct available model
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            response = model.generate_content(f"Correct the grammar and explain the errors:\n{user_input}")
            
            if response and hasattr(response, 'text'):
                corrected_text = response.text  # Get response text

                st.subheader("Corrected Text:")
                st.write(corrected_text)
            else:
                st.error("Invalid response from Gemini API.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text.")
