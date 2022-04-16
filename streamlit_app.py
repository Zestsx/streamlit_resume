import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Spencer Chew (Shi Xiang).
##### *Resume* 
''')

image = Image.open('Spencer.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)
col1.metric("Years of Working Experience", "5")
col2.metric("People Analytics Experience", "4")
col3.metric("Masters Graduate Date", "2024")

st.info('''
- Data Analyst with 4+ years of experience in people analytics. 
- Experienced in data analytics tools & techniques including statistical analysis, dashboarding and machine learning 
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/chew-shi-xiang-spencer-4a9a0582/" target="_blank">Spencer Chew</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Work Experience
''')

txt('**Senior People Analytics Analyst / People Analytics Analyst**, JLL, Singapore','Dec 2017 - Present')
st.markdown('''
- Architected and built global/ regional Tableau Dashboards to generate actionable human capital insights and metrics for JLL (Headcount of 100k) to reduce reporting time 
- Conducted Statistical Analysis using R on HR Research Projects to determine predictive validity and association 
- Built Proof of Concept Glassdoor Web Scraper using BeautifulSoup and Selenium Python packages to analyse sentiment 
- Synergised custom data sources for dashboarding from Workday Excel Reports and SQL Tables using R & Python 
- Partnered closely with Business Stakeholders to gather requirements and scope dashboarding/analytics project 
- Scripted SQL Queries through SQL Management Studio to improve team efficiencies 
- Wrote VBA Macros to expedite compilation and separation of spreadsheets resulting in time savings of 20 hours over 2 months 
- Configured and scheduled custom Workday reports for Stakeholders with Report Writer in Workday
''')

txt('**Associate – People Advisory Services**, ERNST & YOUNG, Singapore','Feb 2017 – Dec 2017')
st.markdown('''
- Developed a spreadsheet survey with Excel to poll opinions on generic skills relevancy for 100 job roles in a growing sector, alongside how-to-guide deck and communication plans to survey participants 
- Conducted Wage Study Analysis of 50 job roles in Singapore Food Service Sector using Excel formulas (Array, Averageif, Sumif, Percentile, Index & Match) 
- Analysed 2000 rows of data on training hours, manpower, dollar cost for an international aircraft company, to form recommendations on their learning & development landscape
- Synthesized research findings into presentation decks for perusal by consultants and managers, for the purposes of business development or internal circulation
''')



# txt('**Insert Role**, Insert Organisation, Country',
# 'Insert Timeframe')
# st.markdown('''
# - Insert Placeholder
# - Insert Placeholder
# - Insert Placeholder
# ''') 



#####################
st.markdown('''
## Education
''')

txt('**Master of Technology in Enterprise Business Analytics**, *National University of Singapore*, Singapore','2022-Current')
st.markdown('''

''')

txt('**Bachelors of Science (Economics)**, *Singapore Management University*, Singapore','2012-2016')
st.markdown('''
- GPA: `3.47 / 4.00`
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `VBA`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `dplyr`')
txt3('Data visualization', '`Tableau`, `Power BI`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Model deployment', '`streamlit`')
txt3('Microsoft Office', '`Excel`, `Powerpoint`, `Word`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/chew-shi-xiang-spencer-4a9a0582/')
txt2('GitHub', 'https://github.com/Zestsx')
txt2('Tableau', 'https://public.tableau.com/app/profile/spencer6275')
