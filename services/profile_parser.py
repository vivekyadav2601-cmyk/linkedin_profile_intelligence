from pypdf import PdfReader
def extract_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file); pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text: pages.append(text)
    return '\n'.join(pages)
def extract_profile_text(pasted_text, uploaded_file=None):
    if pasted_text and pasted_text.strip(): return pasted_text.strip()
    if uploaded_file is not None: return extract_pdf_text(uploaded_file).strip()
    return ''
