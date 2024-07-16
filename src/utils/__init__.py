from utils.logging_config import setup_logger, logger

def is_text_pdf(pdf_path):
    import fitz
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        if text.strip():  # 检查是否有文本内容
            return True
    return False

def hashstr(input_string, length=8):
    import hashlib
    hash = hashlib.md5(str(input_string).encode()).hexdigest()
    return hash[:length]