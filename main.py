import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sizino de Camargo Junior")
    content = """
As a passionate programmer with a focus on DevOps and expertise in Python, I bring a unique blend of technical proficiency and a collaborative mindset to every project I undertake. With a deep-seated love for programming, I find immense joy in crafting efficient and scalable solutions that contribute to the success of teams and organizations.

Driven by the desire to make a positive impact, I thrive in environments where collaboration and continuous learning are valued. My dedication to helping others and my eagerness to learn allow me to seamlessly integrate into any team, contributing my skills and gaining valuable experiences along the way.

I am excited about the opportunity to leverage my expertise in Python and DevOps to help propel your organization forward, tackle complex challenges, and drive innovation. Let's work together to build something amazing!
    """
    st.info(content)