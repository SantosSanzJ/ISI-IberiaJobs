import os
import re
import PyPDF2
import bbdd

current_directory = os.path.dirname(os.path.abspath(__file__))

def remove_files_repeated(folder):
    '''Eliminate all the files in the folder pdf_Files that are repeated.'''
    for file in os.listdir(os.path.join(current_directory,  folder)):
        if re.search(r'\(\d+\)', file):
            os.remove(os.path.join(current_directory, folder, file))
    
def normalize_pdf(folder):
    '''Normalize the pdf files in the folder pdf_Files.'''
    pdf_files = []
    remove_list = []
    for file in os.listdir(os.path.join(current_directory,folder)):
        if file.endswith('.pdf'):
            pdf_files.append(file)
    pdf_files.sort()
    pdf_files = [{'ID': file.split('.')[0]} for file in pdf_files]
    for pdf_file in pdf_files:
        with open(os.path.join(current_directory,folder,pdf_file['ID']) + '.pdf', 'rb') as stream:
            if stream.seek(0, 2) == 0:
                remove_list.append(pdf_file['ID'])
                continue
            pdf_reader = PyPDF2.PdfReader(stream)
            #Extract as the title the text before the word General
            first_page = pdf_reader.pages[0].extract_text()
            if len(pdf_reader.pages) > 1:
                text = first_page + pdf_reader.pages[1].extract_text()
            else:
                text = first_page
            pdf_file['Posicion'] = first_page.splitlines()[-1]
            pdf_file['Descripcion'] = text.split('DESCRIPCION')[1].split('CONTENIDO ADICIONAL')[0]
            pdf_file['EsEspanol'] = True
            if 'Salario mínimo:' in text:
                pdf_file['Salario'] = text.split('Salario mínimo:')[1].split('\n')[0]
            if 'Salario máximo:' in text:
                pdf_file['Salario'] = text.split('Salario máximo:')[1].split('\n')[0]
            if 'Jornada:' in text:
                pdf_file['Jornada'] = text.split('Jornada:')[1].split('\n')[0]
            #if 'Experiencia mínima:' in text:
            #    pdf_file['TiempoExperiencia'] = text.split('Experiencia mínima:')[1].split('\n')[0] 
            if 'Lenguajes requeridos:' in text:
                pdf_file['Idiomas'] = text.split('Lenguajes requeridos:')[1].split('\n')[0]
    return pdf_files, remove_list
    
def add_files_to_db(pdf_files, remove_list, folder):
    '''Add the files in the folder pdf_Files to the database and remove the files that are repeated.'''
    for pdf_file in pdf_files:
        if pdf_file['ID'] in remove_list:
            os.remove(os.path.join(current_directory, folder, pdf_file['ID'] + '.pdf'))
            pdf_files.remove(pdf_file)
        bbdd.insert_dict_into_DDBB(pdf_file)

if __name__ == '__main__':
    folder = 'pdf_Files'
    remove_files_repeated(folder)
    pdf_files, remove_list = normalize_pdf(folder)
    add_files_to_db(pdf_files, remove_list,folder)
