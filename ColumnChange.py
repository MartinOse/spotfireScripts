from Spotfire.Dxp.Application.Visuals import TablePlot

# Get a handle to the Data table
# Tab is the (Visualization) parameter passed to the script specify the table to work on
dataTable= Tab.As[TablePlot]().Data.DataTableReference

# Get a handle to the Table plot
table = Tab.As[TablePlot]()

# Get the ColumnCollection for the Table plot
columns = table.TableColumns

if (Document.Properties["SelectedMetrics"] == "Cost" ):
 columns.Clear()
 # Add the relevant data table columns to the Table plots ColumnColleciton
 columns.Add(dataTable.Columns.Item["Cost"])

if (Document.Properties["SelectedMetrics"] == "Pincode" ):
 columns.Clear()
 # Add the relevant data table columns to the Table plots ColumnColleciton
 columns.Add(dataTable.Columns.Item["Pincode"])

if (Document.Properties["SelectedMetrics"] == "Customer_ID" ):
 columns.Clear()
 # Add the relevant data table columns to the Table plots ColumnColleciton
 columns.Add(dataTable.Columns.Item["Customer_ID"])
 columns.Add(dataTable.Columns.Item["Cost"])

if (Document.Properties["SelectedMetrics"] == "Phone No." ):
 columns.Clear()
 # Add the relevant data table columns to the Table plots ColumnColleciton
 columns.Add(dataTable.Columns.Item["Phone No."])