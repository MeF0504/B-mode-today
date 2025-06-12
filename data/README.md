# Experimental data directory

Each data is managed by JSON file.  
See `example.json` as an example.

## Keys of JSON file

- ell (list of float, required)  
    Multipoles (x-axis) of data points.
- d_ell (list of float, required)  
    Error bar length of x-axis of data points.
- Dl (list of float, required)  
    Power spectrum ($= \ell (\ell+1)/2\pi\ C_\ell$) values (y-axis) of data points.
    The unit is $\mathrm{[\mu K^2]}$.
- d_Dl_plus (list of float, required)  
    Upper side error bar length of y-axis of data points.
    The unit is $\mathrm{[\mu K^2]}$.
- d_Dl_minus (list of float, required)  
    Lower side error bar length of y-axis of data points.
    The unit is $\mathrm{[\mu K^2]}$.
- limit (list of bool, required)  
    If true, it is plotted as the upper limit value.
- ignore (bool)  
    If true, this data is not shown.
- color (string, optional)  
    Color name used in the plot. See [here](https://matplotlib.org/stable/gallery/color/named_colors.html) for available names.
- doi (string, optional)  
    The DOI link. This value is not used in the plot.
- ref (string, optional)  
    Other useful references. This value is not used in the plot.
