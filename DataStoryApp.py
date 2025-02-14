import streamlit as st
import plotly.express as px
import base64
import pandas as pd
from plotly.subplots import make_subplots

# Set Page Configurations
st.set_page_config(page_title="ماراثون الرياض", layout="centered")

# Global CSS styling for the entire page
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;700&display=swap');
    .stApp {
        font-family: 'IBM Plex Sans Arabic', sans-serif;
        text-align: right;
    }
    h1, h2, h3, h4, h5, h6, p, div {
        font-family: 'IBM Plex Sans Arabic', sans-serif !important;
    }
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
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

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

if st.session_state.device_selected == "phone":
    add_bg_from_local('logoPhone.png')
    # Add white background to markdown texts for phone view
    st.markdown(
        """
        <style>
        .stMarkdown, .stTitle {
            background-color: white; /* White background for markdown texts and titles */
            padding: 10px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
# Title and Subtitle
st.title("ماراثون الرياض")
st.markdown("### 🌍هل ماراثوننا عالمي؟")

st.write("شفنا هالسنه في ترويج كبير للماراثون")

# Section 2: First Chart
st.header("🙇‍♂️🙇‍♀️ كيف توزع الجنسين للمشاركين؟") 

# Upload marathons data over the years
df22 = pd.read_csv("Cleaned Data/Clean_22.csv")
df23 = pd.read_csv("Cleaned Data/Clean_23.csv")
df24 = pd.read_csv("Cleaned Data/Clean_24.csv")
df25 = pd.read_csv("Cleaned Data/Clean_25.csv")

# Chart 1: Gender Distribution of Participants Over the Years
# Calculate gender counts for each year
gender_counts_22 = df22['Gender'].value_counts().reset_index()
gender_counts_23 = df23['Gender'].value_counts().reset_index()
gender_counts_24 = df24['Gender'].value_counts().reset_index()
gender_counts_25 = df25['Gender'].value_counts().reset_index()

# Rename columns for consistency
gender_counts_22.columns = ['Gender', 'Count']
gender_counts_23.columns = ['Gender', 'Count']
gender_counts_24.columns = ['Gender', 'Count']
gender_counts_25.columns = ['Gender', 'Count']

# Create a subplot figure with 2 rows, 2 columns
GenderDisFig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("توزيع الجنس - 2022", "توزيع الجنس - 2023", "توزيع الجنس - 2024", "توزيع الجنس - 2025"),
    specs=[[{"type": "domain"}, {"type": "domain"}], [{"type": "domain"}, {"type": "domain"}]]
)

# Add pie charts
for i, gender_counts in enumerate([gender_counts_22, gender_counts_23, gender_counts_24, gender_counts_25]):
    pie_chart = px.pie(
        gender_counts,
        names="Gender",
        values="Count",
        color_discrete_sequence=["orange", "white"]
    )
    # Explicitly force the marker colors to orange and white.
    pie_chart.data[0].marker.colors = ["#fe5d22", "#dcdcdc"]
    GenderDisFig.add_trace(pie_chart.data[0], row=(i // 2) + 1, col=(i % 2) + 1)

# Ensure only one legend
for trace in GenderDisFig.data:
    trace.showlegend = False
GenderDisFig.data[-1].showlegend = True

# Update layout
GenderDisFig.update_layout(
    showlegend=True,
    legend=dict(x=1.1, y=0.5),
    width=1000,
    height=400
)

# Display the chart in Streamlit
st.plotly_chart(GenderDisFig, use_container_width=True)

# Chart 2: Increase in participants over the years
st.header("📈 كيف زاد عدد المشاركين على مر السنين؟")
st.write("!!!!السنة هذي كانت نسخة أستثنائية , شفنا فيها زيادة كبيرة في عدد المشاركين لاربع أضعاف")
st.write(":شيك على الرسمه تحت")

totalPart_22 = df22.shape[0]
totalPart_23 = df23.shape[0]
totalPart_24 = df24.shape[0]
totalPart_25 = df25.shape[0]
# Create a DataFrame for total participants over the years
total_participants = pd.DataFrame({
    "Year": [2022, 2023, 2024, 2025],
    "Total Participants": [totalPart_22, totalPart_23, totalPart_24, totalPart_25]
})

# Create a line chart
line_chart = px.line(
    total_participants,
    x="Year",
    y="Total Participants",
    title="Number of the Marathon Participants Over the Years",
    markers=True
)

# Update marker size and x-axis ticks
line_chart.update_traces(marker=dict(size=10))
line_chart.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=[2022, 2023, 2024, 2025]
    )
)

# Update layout and line color
line_chart.update_traces(line=dict(color="#fe5d22"))
line_chart.update_layout(
    xaxis_title="Year",
    yaxis_title="Number of Participants",
    width=800,
    height=400
)

# Display the line chart in Streamlit
st.plotly_chart(line_chart, use_container_width=True)

# Conclusion
st.header("واخيراً")
st.write("هل بتشارك في الماراثون الجاي؟")

# Footer
st.markdown("---")