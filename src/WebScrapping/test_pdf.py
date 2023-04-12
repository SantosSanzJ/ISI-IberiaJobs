import pdf
import os
import re

def test_remove_files_repeated():
    '''Test the function remove_files_repeated.'''
    folder = 'pdf_Files'
    open(folder + '/test(1).pdf', 'a').close() #Create a file for testing
    pdf.remove_files_repeated(folder)
    for file in os.listdir(folder):
        assert not re.search(r'\(\d+\)', file)

def test_normalize_pdf():
    '''Test the function normalize_pdf.'''
    pdf_files, remove_list = pdf.normalize_pdf()
    for pdf_file in pdf_files:
        assert not pdf_file['ID'].endswith('.pdf')
        assert pdf_file['Posicion'] is not None
        assert pdf_file['Descripcion'] is not None
        assert pdf_file['EsEspanol'] is not None

def test_add_files_to_db():
    '''Test the function add_files_to_db.'''
    pdf_files, remove_list = pdf.normalize_pdf()
    pdf.add_files_to_db(pdf_files, remove_list)
    for pdf_file in pdf_files:
        assert pdf_file['ID'] not in remove_list
