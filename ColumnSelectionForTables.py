from Spotfire.Dxp.Application.Visuals import *
from Spotfire.Dxp.Data import *

Tab.TypeId = VisualTypeIdentifiers.Table

Tab = Tab.As[TablePlot]()
columns = Tab.TableColumns

for col in columns:
	
	print(col.Name)

	if (Document.Properties["TableColSel"] == col.Name):
		columns.Add(Tab.Columns.Item[col.Name])
	elif (Document.Properties["TableColSel"] != col.Name):
		columns.Remove(Tab.Columns.Item[col.Name])