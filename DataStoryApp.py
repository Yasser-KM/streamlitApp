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

def add_bg_from_local_phone(image_file):
    '''Adds background image from local file and applies additional styling.'''
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
        }}
        /* Apply white background with orange outline to markdown texts */
        .stText, .stMarkdown,  .stTitle, .stHeader {{
            background-color: white !important;
            padding: 10px !important;
            border-radius: 5px !important;
            border: 2px solid #fe5d22 !important;
            
        }}
          .title1{{
            display: none;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Ask user to select device type before showing content
if "device_selected" not in st.session_state:
    st.session_state.device_selected = None

if st.session_state.device_selected is None:
    # st.markdown("# 👀من وين فاتح الصفحة؟")
    # st.markdown("لتجربة أفضل , أختر الجهاز الي فاتح به الصفحة")
    st.markdown('<h1 class="title1">👀من وين فاتح الصفحة؟</h1>', unsafe_allow_html=True)
    st.markdown('<p class="title1">لتجربة أفضل , أختر الجهاز الي فاتح به الصفحة</p>', unsafe_allow_html=True)
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
    add_bg_from_local_phone('logoPhone.png')


# Title and Subtitle
st.markdown( "# ماراثون الرياض: هل عندنا ثقافة الجري؟ 🏃‍♂️🏃‍♀️")
# st.markdown("### 🌍هل ماراثوننا عالمي؟")
st.title(" ")
st.write("""
!خلال اربعة سنين ماراثون الرياض صار حديث الناس، و عدد المشاركين في ازدياد
         
من محترفين، هواة،  سعوديين, اجانب الى ناس تبغى تخوض تجارب جديدة
         
!!والكل جاي يجري
         """)

# Section 2: First Chart


# Upload marathons data over the years
df22 = pd.read_csv("Cleaned Data/Clean_22.csv")
df23 = pd.read_csv("Cleaned Data/Clean_23.csv")
df24 = pd.read_csv("Cleaned Data/Clean_24.csv")
df25 = pd.read_csv("Cleaned Data/Clean_25.csv")

# Unifying the race types in df23
df23['Race Type'] = df23['Race Type'].replace({
    '4 km': '4KM FUN RUN',
    '10 km': '10KM RUN',
    'Half Marathon': 'HALF MARATHON',
    'Marathon': 'MARATHON',
    'Half Marathon Elite': 'HALF MARATHON ELITE',
    'Marathon Elite': 'MARATHON ELITE'
})

# Chart 1: Increase in participants over the years
st.markdown("### 💪الرياضة للجميع")
st.write(" !ثقافة الرياضة للجميع عندنا تنتشر! ماراثون الرياض بدا من 2022 ومن وقتها و اعداد المشاركين تزيد بشكل مجنوون ")
st.write("!بدا **ب 6 الاف** مشارك ووتضاعفت 4 مرات تقريبا ووصل **الى 27 الف** مشارك في  2025 ")

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

# Chart 2: Different nationalities of participants

st.markdown("### 🌍🤩ماراثون الرياض صار عالمي")
st.write("! متخيلين ان الماراثون صار عالمي")
st.write("!! **51.7%** من بدأ ماراثون الرياض الى أخر نسخة من الماراثون زادت عدد الجنسيات المختلفة المشاركة بنسبة")

# Create a dictionary of datasets for each year
datasets = {
    '2022': df22,
    '2023': df23,
    '2024': df24,
    '2025': df25
}

# Calculate sum of unique nationalities minus 1 for each year
unique_nationalities_per_year = {}
for year, df in datasets.items():
    unique_nationalities = df['Nationality'].nunique()
    unique_nationalities_per_year[year] = unique_nationalities - 1

# Convert to DataFrame for visualization
nationalities_df = pd.DataFrame(list(unique_nationalities_per_year.items()), columns=['Year', 'Unique Nationalities'])
nationalities_df.sort_values(by='Year', inplace=True)

# Create a bar chart to compare unique nationalities per year
bar_chart = px.bar(
    nationalities_df,
    x='Year',
    y='Unique Nationalities',
    title="Nationalities Participated Over the Years",
    color_discrete_sequence=["#fe5d22"]
)

# Update layout
bar_chart.update_layout(
    xaxis_title="Year",
    yaxis_title="Count of different nationalities participated",
    width=800,
    height=400
)
bar_chart.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=[2022, 2023, 2024, 2025]
    )
)
# Display the bar chart in Streamlit
st.plotly_chart(bar_chart, use_container_width=True)

# Chart 3: Saudies vs Non-Saudies

st.write(" الواضح لنا ان فيه اهتمام بماراثون الرياض من دول مختلفه ومن جنسيات مختلفة ")
st.write("بس ودنا نعرف هل هم يمثلون الأكثرية في الماراثون؟")
st.write("🌍خلونا نشوف كيف توزع السعوديين وغير السعوديين في المشاركين في الماراثون ")

# Function to count Saudis vs Non-Saudis
def count_saudi_vs_non_saudi(df):
    df['Saudi Status'] = df['Nationality'].apply(lambda x: 'Saudi' if x in ['SA', 'KSA'] else 'Non-Saudi')
    return df['Saudi Status'].value_counts().reset_index()

# Count Saudi vs Non-Saudi for each year
saudi_counts_22 = count_saudi_vs_non_saudi(df22)
saudi_counts_23 = count_saudi_vs_non_saudi(df23)
saudi_counts_24 = count_saudi_vs_non_saudi(df24)
saudi_counts_25 = count_saudi_vs_non_saudi(df25)

# Rename columns for consistency
saudi_counts_22.columns = ['Saudi Status', 'Count']
saudi_counts_23.columns = ['Saudi Status', 'Count']
saudi_counts_24.columns = ['Saudi Status', 'Count']
saudi_counts_25.columns = ['Saudi Status', 'Count']

# Create a subplot figure with 2 rows, 2 columns
NationalityDisFig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("2022", 
                    "2023", 
                    "2024", 
                    "2025"),
    specs=[[{"type": "domain"}, {"type": "domain"}], [{"type": "domain"}, {"type": "domain"}]]
)

# Add pie charts for each year
for i, saudi_counts in enumerate([saudi_counts_22, saudi_counts_23, saudi_counts_24, saudi_counts_25]):
    pie_chart = px.pie(
        saudi_counts,
        names="Saudi Status",
        values="Count",
        color_discrete_sequence=["#fe5d22", "#dcdcdc"]
    )
    # Explicitly force the marker colors to orange and light gray.
    pie_chart.data[0].marker.colors = ["#fe5d22", "#dcdcdc"]
    NationalityDisFig.add_trace(pie_chart.data[0], row=(i // 2) + 1, col=(i % 2) + 1)

# Ensure only one legend
for trace in NationalityDisFig.data:
    trace.showlegend = False
NationalityDisFig.data[-1].showlegend = True

# Update layout
NationalityDisFig.update_layout(
    showlegend=True,
    legend=dict(x=1.1, y=0.5),
    width=1000,
    height=600
)

# Display the chart in Streamlit
st.plotly_chart(NationalityDisFig, use_container_width=True)

st.write("لاحظنا ان نسبة السعوديين المشاركين زادت من **53%** الى **65%** وهذا يدل على انتشار ثقافة الرياضة للجميع")

st.markdown("### 🙇‍♂️🙇‍♀️ هل في منافسة بين الجنسين؟") 
st.write("كل سنة نشوف زيادة في اعداد المشاركين لكن هل في توازن؟ اي الجنسين كان مهتم أكثر بالمشاركة في الماراثون؟")
# Chart 4: Gender Distribution of Participants Over the Years
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

st.write("الواضح ان في زيادة 5% لكن اعداد النساء تضاعفت 4 مرات خلال 4 سنوات وهذا يدل ان ثقافة الجري تنتشر بين العوائل ايضا")

# Chart 5: Females Participation in different race types Over the Years

# Function to count females in each race type
def count_females_per_race(df):
    return df[df['Gender'] == 'Female']['Race Type'].value_counts().reset_index()

# Count females per race type for each year
females_race_22 = count_females_per_race(df22)
females_race_23 = count_females_per_race(df23)
females_race_24 = count_females_per_race(df24)
females_race_25 = count_females_per_race(df25)

# Rename columns for consistency
females_race_22.columns = ['Race Type', 'Count']
females_race_23.columns = ['Race Type', 'Count']
females_race_24.columns = ['Race Type', 'Count']
females_race_25.columns = ['Race Type', 'Count']

# Add Year column to each DataFrame
females_race_22['Year'] = 2022
females_race_23['Year'] = 2023
females_race_24['Year'] = 2024
females_race_25['Year'] = 2025

# Concatenate all DataFrames
females_race_all_years = pd.concat([females_race_22, females_race_23, females_race_24, females_race_25])

# Create a line chart to compare females counts for each race type over the years
line_chart_females_race = px.line(
    females_race_all_years,
    x="Year",
    y="Count",
    color="Race Type",
    title="Females Participation in Different Race Types Over the Years",
    markers=True,
    color_discrete_sequence=px.colors.sequential.Sunset
)

# Update marker size and x-axis ticks
line_chart_females_race.update_traces(marker=dict(size=10))
line_chart_females_race.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=[2022, 2023, 2024, 2025]
    )
)

# Update layout
line_chart_females_race.update_layout(
    xaxis_title="Year",
    yaxis_title="Number of Female Participants",
    width=800,
    height=400
)

# Display the line chart in Streamlit
st.plotly_chart(line_chart_females_race, use_container_width=True)

st.markdown("### 🏆 بطل")
st.write("في حال كنت تعتقد أنك دخولك في الماراثون صعب ومستحيل تحقق أنجاز فحابين نوريك رحلة أحد المشاركين خلال النسخ الأربعة للماراثون")
# Chart 6: A champ 
champ_df = pd.read_csv("Cleaned Data/champ_df.csv")

# Create a line chart to display the improvement in speed between the race types
champ = px.line(champ_df, x='Race Type',
               y=['Total Rank', 'Rank'],
                 labels={'value': 'Rank', 'variable': 'Metric'},
                   title='Improvement in Speed Between Race Types',
                     markers=True,
                       color_discrete_sequence=['#fe5d22', '#dcdcdc'])

# Show the plot
st.plotly_chart(champ, use_container_width=True)

# Conclusion
st.markdown('''
            ## واخيراً
            هل بتشارك في الماراثون الجاي؟
            ''')
