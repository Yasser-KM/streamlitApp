import streamlit as st
import plotly.express as px
import base64
import pandas as pd
from plotly.subplots import make_subplots

st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;700&display=swap');
        .stApp {{
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

# Function to add background (only for Desktop View)
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
st.set_page_config(page_title="ماراثون الرياض", layout="wide")

# Ask user to select device type before showing content
if "device_selected" not in st.session_state:
    st.session_state.device_selected = None

if st.session_state.device_selected is None:
    st.title("👀من وين فاتح الصفحة؟")
    st.write("لتجربة أفضل , أختر الجهاز الي فاتح به الصفحة")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📱 جوال"):
            st.session_state.device_selected = "phone"

    with col2:
        if st.button("💻 لاب توب او ديسك توب"):
            st.session_state.device_selected = "desktop"

    st.stop()  # Stop execution until the user selects a device

# Apply background only if "Desktop View" is selected
if st.session_state.device_selected == "desktop":
    add_bg_from_local('logo.png')

# if st.session_state.device_selected == "phone":
#    add_bg_from_local('logoPhone.png')

# Title and Subtitle
st.title("ماراثون الرياض 🏃‍♂️")
st.markdown("### 🌍هل ماراثوننا عالمي؟")

st.write(" شفنا هالسنه في ترويج كبير للماراثون ")

# Section 2: First Chart
st.header("📈 التصور البياني الأول")

# Sample data for gender distribution over the years
GenderDist = {
    "Year": ["2022", "2022", "2023", "2023", "2024", "2024", "2025", "2025"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Count": [4113, 2136, 7240, 3883, 9686, 5611, 16547, 10961]
}

GenderDis = pd.DataFrame(GenderDist)

# Create a subplot figure with 2 rows, 2 columns
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("توزيع الجنس - 2022", "توزيع الجنس - 2023", "توزيع الجنس - 2024", "توزيع الجنس - 2025"),
    specs=[[{"type": "domain"}, {"type": "domain"}], [{"type": "domain"}, {"type": "domain"}]]
)

# Add pie charts
for i, year in enumerate(["2022", "2023", "2024", "2025"]):
    pie_chart = px.pie(GenderDis[GenderDis["Year"] == year], names="Gender", values="Count")
    fig.add_trace(pie_chart.data[0], row=(i//2)+1, col=(i%2)+1)

# Ensure only one legend
for trace in fig.data:
    trace.showlegend = False
fig.data[-1].showlegend = True

# Update layout
fig.update_layout(
    showlegend=True,
    legend=dict(x=1.1, y=0.5),
    width=1000,
    height=400
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Conclusion
st.header("واخيراً")
st.write("هل بتشارك في الماراثون الجاي؟")

# Footer
st.markdown("---")
