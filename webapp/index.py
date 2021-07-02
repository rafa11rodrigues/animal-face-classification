import streamlit as st
import src.service as service


'''
# Animal Face Classification

This is a simple app to demonstrate how a machine learning can be used in production.

To get it to work, simply choose an image and submit it. You can either provide a image URL or upload an image file.

The app will tell you if the submitted image is either a cat, a dog or a wildlife animal.
'''

'''
## URL
Enter the image URL and press **Enter** to submit.
'''
url = st.text_input('Enter the image URL here')

if url:
    st.json(service.predict_from_url(url))

'''
## Image file
Choose an image file.
'''
img = st.file_uploader('Image', type=['jpg', 'png'])

if img:
    st.json(service.predict_from_file(img))
