# STEMSimPy
A Python Package for postprocessing Scanning Transmission Electron Microscopy (STEM) Simulations

Modern STEMs offer possibilities to create multidimensional data sets and due to the complicated scattering physics of fast electrons in materials, simulations facilitating the interpretation and development of such experiments are necessary. This Python package shall provide a convenient way to postprocess simulations of STEM experiments. The idea is to base the entire package around the zarr data format. So there shall be functionality to assemble the zarr file from several simulation runs as well as convenience functions to plot/view/investigate common signals and effects.


Default (alternative) units:

x, y, z:    angstrom
qx, qy:     1/angstrom (mrad)
dE:         eV (rad/s)
n:	    dimensionless



Data structure:

/
|__ data
|
|__ processed
|
|__ visualization


