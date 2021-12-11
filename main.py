import streamlit as st

#############################################################################################
#############################################################################################


##############################################################################################
##############################################################################################

# Below we are defining a streamlit webpage which will take user input and predict polarity of taken review

st.title("English-Hindi translater")
st.header("This is Deep-Learning based model, which translates english language input sentence to hindi language sentence. This model has some limitations and one of them is number of words in input sentence should not be greater than 20 words.")
# st.text_input(label="Enter your english sentence below")


with st.form("my_form"):
    # st.write("Enter your english sentence below")
    review = st.text_input(label='Please enter your english sentence below')

    # Every form must have a submit button.
    submitted = st.form_submit_button("Predict")


if submitted:
    if review == '':
        st.text(f"Please enter your english sentence below and press translate!")
    else:

        predicted_score = 0.6

        if predicted_score < 0.5:
            st.text(f"You've given negative review")
        else:
            st.text(f"You've given positive review")


