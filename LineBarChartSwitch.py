from Spotfire.Dxp.Application.Visuals import *
from Spotfire.Dxp.Data import *

if (vis.TypeId == VisualTypeIdentifiers.BarChart):
	vis.TypeId = VisualTypeIdentifiers.LineChart
	vis = vis.As[LineChart]()
	vis.XAxis.Expression = "[Column1]"

elif (vis.TypeId == VisualTypeIdentifiers.LineChart):
	vis.TypeId = VisualTypeIdentifiers.BarChart
	vis = vis.As[BarChart]()
	vis.XAxis.Expression = "[Column2]"