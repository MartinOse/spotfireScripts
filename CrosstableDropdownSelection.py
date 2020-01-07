from Spotfire.Dxp.Application.Visuals import *
from Spotfire.Dxp.Data import *


table = Tab.As[Visualization]()
cols = table.Data.DataTableReference.Columns

if (Document.Properties["CrossTableDropdown"] == "Cost" ):
	table.MeasureAxis.Expression = "Sum([Cost])"

if (Document.Properties["CrossTableDropdown"] == "Revenue" ):
	table.MeasureAxis.Expression = "Sum([Revenue])"

if (Document.Properties["CrossTableDropdown"] == "All" ):
	i = 0
	colStr = ""

	for col in cols:
		type = str(col.DataType)
		if((i<cols.Count-1) and (type=="Integer")):
			colStr += str("Sum([" + cols[str(col)].Name + "]), ")
		elif((i==cols.Count-1) and (type=="Integer")):
			colStr += str("Sum([" + cols[str(col)].Name + "])")
		i += 1
	
	if(colStr[-2]==','):
		colStr = colStr[:-2]

	table.MeasureAxis.Expression = colStr