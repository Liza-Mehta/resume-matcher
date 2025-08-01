$pythonCode = @'
import PyPDF2
from docx import Document
from io import BytesIO

def extract_text_from_file(file):
    """Extract text from PDF or DOCX files"""
    content = file.read()
    
    if file.name.endswith('.pdf'):
        try:
            pdf_reader = PyPDF2.PdfReader(BytesIO(content))
            text = "\n".join([page.extract_text() for page in pdf_reader.pages])
            return text
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return ""
    
    elif file.name.endswith('.docx'):
        try:
            doc = Document(BytesIO(content))
            return "\n".join([para.text for para in doc.paragraphs])
        except Exception as e:
            print(f"Error reading DOCX: {e}")
            return ""
    
    return ""
'@

$pythonCode | Out-File -Encoding utf8 utils/text_extract.py