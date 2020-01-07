from Spotfire.Dxp.Application.Visuals import *
from Spotfire.Dxp.Data import *

table = Tab.As[VisualContent]()
cols = table.Data.DataTableReference.Columns
selection = Document.Data.Properties.GetProperty(DataPropertyClass.Document, "TableColSel2").Value

colList = list()

for property in selection:
	for col in property.split(","):
		colList.append(str(col + "])"))

colList[0] = "Sum(["+colList[0]
colStr = ", Sum([".join(colList)


table.MeasureAxis.Expression = colStr