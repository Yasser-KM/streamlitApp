import streamlit as st
import plotly.express as px
import base64
import pandas as pd
from plotly.subplots import make_subplots

# Function to check if the visitor is using a mobile device
def is_mobile():
    user_agent = st.request.headers.get("User-Agent", "")
    return "Mobi" in user_agent  # 'Mobi' is common in mobile User-Agent strings

# Function to add background only for non-mobile devices
def add_bg_from_local(image_file):
    '''Adds background image from local file for non-mobile devices.'''
    if not is_mobile():  # Only apply background if NOT on mobile
        with open(image_file, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;700&display=swap');
        .stApp {{
            font-family: 'IBM Plex Sans Arabic', sans-serif;
            text-align: right;
        }}
        h1, h2, h3, h4, h5, h6, p, div {{
            font-family: 'IBM Plex Sans Arabic', sans-serif !important;
        }}
        {" .stApp { background-image: url('data:image/png;base64," + encoded + "'); background-size: cover; } " if not is_mobile() else ""}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set Page Configurations
st.set_page_config(page_title="قصة البيانات")

# Apply background conditionally
add_bg_from_local('logo.png')

# Title and Subtitle
st.title("📊 قصة البيانات")
st.markdown("### سرد بصري باستخدام البيانات والمخططات")

# Section 1: Overview
st.header("📌 نظرة عامة")
st.write("يوفر هذا القسم مقدمة إلى مجموعة البيانات والرؤى الرئيسية.")

# Section 2: First Chart
st.header("📈 التصور البياني الأول")

# Sample data for gender distribution over the years
data = {
    "Year": ["2022", "2022", "2023", "2023", "2024", "2024", "2025", "2025"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Count": [4113, 2136, 7240, 3883, 9686, 5611, 16547, 10961]
}

df = pd.DataFrame(data)

# Create a subplot figure with 1 row, 4 columns
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("توزيع الجنس - 2022", "توزيع الجنس - 2023", "توزيع الجنس - 2024", "توزيع الجنس - 2025"),
    specs=[[{"type": "domain"}, {"type": "domain"}], [{"type": "domain"}, {"type": "domain"}]]
)

# Add pie charts to each subplot
for i, year in enumerate(["2022", "2023", "2024", "2025"]):
    pie_chart = px.pie(df[df["Year"] == year], names="Gender", values="Count")
    fig.add_trace(pie_chart.data[0], row=(i//2)+1, col=(i%2)+1)

# Update layout for better positioning
fig.update_layout(
    showlegend=True,
    legend=dict(x=1.1, y=0.5),
    width=1000,
    height=400
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Conclusion
st.header("📝 الخاتمة")
st.write("قم بتلخيص النقاط الرئيسية والرؤى المستخلصة من قصة البيانات.")

# Footer
st.markdown("---")
