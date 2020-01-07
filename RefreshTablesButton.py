from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data.Import import *

# Refresh all tables

for t in Document.Data.Tables:
	if t.IsRefreshable:
		t.Refresh()