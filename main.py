import streamlit as st

#############################################################################################
#############################################################################################


##############################################################################################
##############################################################################################

# Below we are defining a streamlit webpage which will take user input and predict polarity of taken review

st.title("English-Hindi translater")
st.text("This is Deep-Learning based model,\nwhich translates english language input sentence to hindi language sentence.")
st.text("This model has some limitations:\n1.   one of them is number of words in input sentence should not be greater than 20 words.")


with st.form("input_form"):
    # st.write("Enter your english sentence below")
    review = st.text_input(label='Please enter your english sentence below')

    # Every form must have a submit button.
    submitted = st.form_submit_button("Translate")


# translated_sentence = predict(review)


if submitted:
    if review == '' or review == None:
        st.text(f"Please enter your english sentence below and press translate!")
    else:
        st.text(f"Your translated sentece will be shown here")
