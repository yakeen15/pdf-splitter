import pikepdf
def splitter(inp,ran):
	input_pdf = pikepdf.open(inp)
	file_path = inp.split("/")
	file_path.pop()
	a = max(1, min(ran[0], len(input_pdf.pages))) 
	b = max(1, min(ran[1], len(input_pdf.pages)))
	output_pdf = pikepdf.Pdf.new()
	for page_number in range(a - 1, b): 
	    page = input_pdf.pages[page_number]
	    output_pdf.pages.append(page)
	output_path = ''
	for part in file_path:
		output_path=output_path+part+"/"
	output_pdf.save(output_path+"/"+f'range_{a}_{b}.pdf')
	input_pdf.close()