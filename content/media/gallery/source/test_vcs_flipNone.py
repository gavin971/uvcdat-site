import vcs, cdms2, os, sys

x=vcs.init()

x.setbgoutputdimensions(1200,1091,units="pixels")

f=cdms2.open(os.path.join(sys.prefix,"sample_data","ta_ncep_87-6-88-4.nc"))


vr = "ta"
s=f(vr,slice(0,1),longitude=slice(90,91),squeeze=1,level=(0,10000))
x.plot(s,bg=1)
fnm = "test_vcs_flipNone.png"
x.png(fnm)