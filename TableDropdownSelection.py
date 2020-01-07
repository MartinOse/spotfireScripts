from Spotfire.Dxp.Application.Visuals import *
from Spotfire.Dxp.Data import *

# Tab is the (Visualization) parameter passed to the script specify the table to work on
dataTable = Tab.As[TablePlot]().Data.DataTableReference

table = Tab.As[TablePlot]()

# Get the ColumnCollection for the Table plot
columns = table.TableColumns
cols = table.Data.DataTableReference.Columns

# Option 1 in dropdown
if (Document.Properties["TableDropdownSel"] == "Cost" ):
	columns.Clear()
	columns.Add(dataTable.Columns.Item["Cost"])
	columns.Add(dataTable.Columns.Item["Commision 1"])
 

# Option 2 in dropdown
if (Document.Properties["TableDropdownSel"] == "Pincode" ):
	columns.Clear()
	columns.Add(dataTable.Columns.Item["Pincode"])
	columns.Add(dataTable.Columns.Item["Phone No."])
	print(type(dataTable.Columns.Item["Phone No."]))

# Option 3 in dropdown, adds back ALL columns to table
if (Document.Properties["TableDropdownSel"] == "ALL" ):
	columns.Clear()
	for col in cols:
		columns.Add(cols[str(col)])