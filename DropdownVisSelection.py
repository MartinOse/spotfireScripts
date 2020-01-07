from Spotfire.Dxp.Application.Visuals import *
from Spotfire.Dxp.Data import *

if (Document.Properties["DropDownVis"] == "Bar Chart" ):
	vis.TypeId = VisualTypeIdentifiers.BarChart

if (Document.Properties["DropDownVis"] == "Line Chart" ):
	vis.TypeId = VisualTypeIdentifiers.LineChart

if (Document.Properties["DropDownVis"] == "Pie Chart" ):
	vis.TypeId = VisualTypeIdentifiers.PieChart
