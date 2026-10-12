import streamlit as st
from services.profile_parser import extract_profile_text
from services.profile_analyzer import ProfileAnalyzer

st.set_page_config(page_title='LinkedIn Profile Intelligence', page_icon='💼', layout='wide')
st.title('💼 LinkedIn Profile Intelligence')
st.caption('AI-powered professional profile analysis using LangChain + Gemini')

with st.sidebar:
    st.header('Input')
    input_method = st.radio('Choose input method', ['Paste Profile', 'Upload PDF'])

profile_text = ''
uploaded_file = None
if input_method == 'Paste Profile':
    profile_text = st.text_area('Paste LinkedIn profile text', height=400)
else:
    uploaded_file = st.file_uploader('Upload profile/resume PDF', type=['pdf'])

if st.button('🔍 Analyze Profile', type='primary'):
    source_text = extract_profile_text(profile_text, uploaded_file)
    if not source_text.strip():
        st.error('Please paste profile information or upload a PDF.')
    else:
        with st.spinner('Analyzing professional profile...'):
            try:
                profile = ProfileAnalyzer().analyze(source_text)
                st.session_state['profile'] = profile
                st.success('Profile analysis completed!')
            except Exception as exc:
                st.error(f'Analysis failed: {exc}')

if 'profile' in st.session_state:
    p = st.session_state['profile']
    st.divider(); st.header('Professional Profile')
    c1, c2 = st.columns(2)
    with c1:
        st.subheader(p.name or 'Unnamed Profile')
        st.write(f'**Headline:** {p.headline or "—"}')
        st.write(f'**Current Role:** {p.current_role or "—"}')
        st.write(f'**Company:** {p.current_company or "—"}')
        st.write(f'**Location:** {p.location or "—"}')
    with c2:
        st.subheader('Skills'); st.write(' • '.join(p.skills) if p.skills else 'No skills identified.')
    st.subheader('About'); st.write(p.about or 'No About section identified.')
    st.subheader('Experience')
    for e in p.experience:
        with st.expander(f'{e.role or "Role"} — {e.company or "Company"}'):
            st.write(f'**Duration:** {e.duration or "—"}'); st.write(e.description or 'No description available.')
    st.subheader('Education')
    for e in p.education:
        st.write(f'**{e.degree or "Degree"}** — {e.institution or "Institution"}')
        if e.field: st.write(f'Field: {e.field}')
        if e.year: st.write(f'Year: {e.year}')
    st.subheader('Achievements')
    for x in p.achievements: st.write(f'🏆 {x}')
    st.subheader('Certifications')
    for x in p.certifications: st.write(f'📜 {x}')
    st.subheader('Projects')
    for x in p.projects: st.write(f'🔹 {x}')
    st.subheader('Languages'); st.write(', '.join(p.languages) if p.languages else 'No languages identified.')
