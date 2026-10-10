content = open('c:/Users/Sunil/OneDrive/Desktop/portfolio_ai/tempCodeRunnerFile.py').read()

# Replace the function
old = """#pdf extraction
def read_pdf(file_path: Path):

    reader = PdfReader(file_path)

    text = \"\"

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\\n"

    return text"""

new = """#word extraction
def read_docx(file_path: Path):

    document = Document(file_path)

    text = "\\n".join([paragraph.text for paragraph in document.paragraphs if paragraph.text.strip()])

    return text"""

if old in content:
    content = content.replace(old, new)
    open('c:/Users/Sunil/OneDrive/Desktop/portfolio_ai/tempCodeRunnerFile.py', 'w').write(content)
    print('Function replaced successfully')
else:
    print('Old function not found')