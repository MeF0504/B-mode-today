# B mode today!

Plot CMB B-mode power spectrum and data points.

## How to make plot
```shell
# show usage
python3 main.py -h
```
``` shell
# run by default settings
python3 main.py
```

## Requirements
- [python3](https://www.python.org/downloads/)
- [numpy](https://numpy.org/)
- [camb](https://camb.readthedocs.io/)
- [matplotlib](https://matplotlib.org/)

## experimental data
Data are maintained by `data.toml` file.
### Data format
- tag  
    Tag name to specify the data.
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


## Maintenance

### Adding new experiments data
これから整備します...

### Bug reports
これから整備します...

## ToDo
1. Add more experiments data
1. READMEの整備
1. データ追加方法の整備（pull req）
1. bug fix template の準備

## License
[MIT](https://github.com/MeF0504/B-mode-today/blob/main/LICENSE)

## Author
[MeF0504](https://github.com/MeF0504)

