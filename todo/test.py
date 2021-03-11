# import xlsxwriter module 
import xlsxwriter 

# Workbook() takes one, non-optional, argument 
# which is the filename that we want to create. 
workbook = xlsxwriter.Workbook('hello.xlsx') 

R = ["code Fournisseur","nom fournisseur","code Fournisseur",
	"registre de commerce","telephone","fax","c correspondance",
	"site web","email","fichier","adresse banque","compte b",
	"adresse Fournisseur","adresse","adresse1","Remarque1",
	"Remarque2","flag"]

# The workbook object is then used to add new 
# worksheet via the add_worksheet() method. 
worksheet = workbook.add_worksheet() 

# Use the worksheet object to write 
# data via the write() method. 

for i in range(len(R)):
	worksheet.write('{}1 header'.format(chr(ord("A")+i)), R[i]) 

# Finally, close the Excel file 
# via the close() method. 
workbook.close() 
