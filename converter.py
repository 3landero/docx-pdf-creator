#librerias necesarias
from pathlib import Path
from docxtpl import DocxTemplate
from docx2pdf import convert

#establece una ruta para llegar al archivo de la platilla
document_path = Path(__file__).parent / "plantilla.docx"
#se define ejecucion de la libreria sobre el documento deifnido en la ruta
doc = DocxTemplate(document_path)

#las variable DUMMY que se ejecutaran
id_associate = "001"
first_name = "Ramses"
last_name =   "Landero"
email = "eldeliciosorikolino@gmail.com"
rfc = "LAGR8307127EG1"
curp = "LAGR830727HTCNMM08"
interbank_key = 123456789987654321
created = "01.06.2022"
modified = "05.06.2022"
gender = "Hombre"
country =   "Mexico"
job_title = "Backend Dev"
status = "Active"

# los valores de arriba DEBEN definirse como variables que conecten con la plantilla
context = {
"id_associate" : id_associate,
"first_name" : first_name,
"last_name" : last_name,
"email" : email,
"rfc" : rfc,
"curp" : curp,
"interbank_key" : interbank_key,
"created" : created,
"modified" : modified,
"gender" : gender,
"country" : country,
"job_title" : job_title,
"status" : status
}

#renderiza las variables de arriba con los valores de la plantilla "RAM"
doc.render(context)
new_file = Path(__file__).parent / f"{id_associate}-contract.docx"
#guarda los cambios en un archivo nuevo
doc.save(Path(new_file))
#define el archivo docx para convertirlo a pdf
convert(new_file)