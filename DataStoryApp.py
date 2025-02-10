import streamlit as st
import plotly.express as px
import base64
import plotly.io as pio
import json


def add_bg_from_local(image_file):
    '''Adds background image from local file.'''
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;700&display=swap');
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            font-family: 'IBM Plex Sans Arabic', sans-serif;
            text-align: right;
        }}
        h1, h2, h3, h4, h5, h6, p, div {{
            font-family: 'IBM Plex Sans Arabic', sans-serif !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set Page Configurations
st.set_page_config(page_title="قصة البيانات")

# Add background image (replace 'bg_image.jpg' with your image file)
add_bg_from_local('logo.png')

# Title and Subtitle
st.title("📊 قصة البيانات")
st.markdown("### سرد بصري باستخدام البيانات والمخططات")

# Section 1: Overview
st.header("📌 نظرة عامة")
st.write("يوفر هذا القسم مقدمة إلى مجموعة البيانات والرؤى الرئيسية.")

# Section 2: First Chart
st.header("📈 التصور البياني الأول")
# Load the Plotly figure from JSON file
with open("GenderDist.json", "r") as f:
    fig_json = json.load(f)

# Convert JSON back to Plotly figure
fig1 = pio.from_json(fig_json)
# Display the chart in Streamlit
st.plotly_chart(fig1, use_container_width=True)


# Section 3: Second Chart
st.header("📉 التصور البياني الثاني")
# Sample data for gender distribution over the years
data = {
    "Year": ["2022", "2022", "2023", "2023", "2024", "2024", "2025", "2025"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Count": [60, 40, 55, 45, 50, 50, 70, 30]  # Example percentages
}
import pandas as pd
from plotly.subplots import make_subplots

df = pd.DataFrame(data)

# Create a subplot figure with 1 row, 3 columns
fig = make_subplots(
    rows=1, cols=4,
    subplot_titles=("توزيع الجنس - 2022", "توزيع الجنس - 2023", "توزيع الجنس - 2024", "توزيع الجنس - 2025"),
    specs=[[{"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "domain"}]]
)

# Add pie charts to each subplot
fig.add_trace(px.pie(df[df["Year"] == "2022"], names="Gender", values="Count").data[0], row=1, col=1)
fig.add_trace(px.pie(df[df["Year"] == "2023"], names="Gender", values="Count").data[0], row=1, col=2)
fig.add_trace(px.pie(df[df["Year"] == "2024"], names="Gender", values="Count").data[0], row=1, col=3)
fig.add_trace(px.pie(df[df["Year"] == "2025"], names="Gender", values="Count").data[0], row=1, col=4)


# Ensure only one legend for all charts
fig.update_traces(showlegend=False)  # Hide legends for all
fig.data[-1].showlegend = True  # Enable legend only in the last chart

# Update layout for better positioning
fig.update_layout(
    showlegend=True,
    legend=dict(x=1.05, y=0.5),  # Position legend to the right
    width=900,  # Adjust width to fit all charts
    height=400
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
# Conclusion
st.header("📝 الخاتمة")
st.write("قم بتلخيص النقاط الرئيسية والرؤى المستخلصة من قصة البيانات.")

# Footer
st.markdown("---")

