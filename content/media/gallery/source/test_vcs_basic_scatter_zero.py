
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
gm = vcs.createscatter()


xtra = {}
f=cdms2.open(os.path.join(sys.prefix,'sample_data','clt.nc'))
s=f("clt",**xtra)
s = s(latitude=(20,20,"cob"),longitude=(112,112,"cob"),squeeze=1)
s2=MV2.sin(s)
s2-=s2
s-=s
x.plot(s,s2,gm,bg=bg)



x.png('test_vcs_basic_scatter_zero.png')
