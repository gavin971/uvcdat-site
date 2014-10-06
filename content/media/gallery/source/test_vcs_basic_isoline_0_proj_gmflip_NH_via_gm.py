
import sys,os
import vcs
import sys
import cdms2
import vtk
import os
import MV2
bg = not False
x=vcs.init()
x.setbgoutputdimensions(1200,1091,units="pixels")
x.setcolormap("rainbow")
gm = vcs.createisoline()

p = vcs.createprojection()
ptype = int('0')
p.type = ptype
gm.projection = p

xtra = {}
gm.datawc_y1=0.0
gm.datawc_y2=90.0

xtra["latitude"] = (90.0,0.0)


f=cdms2.open(os.path.join(sys.prefix,'sample_data','clt.nc'))
s=f("clt",**xtra)
x.plot(s,gm,bg=bg)



x.png('test_vcs_basic_isoline_0_proj_gmflip_NH_via_gm.png')
