#! /usr/bin/env python3

import argparse
from pathlib import Path
import json

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import camb
from camb import initialpower

mpl.rcParams['font.size'] = 14


def calc_dl(lmax: int, rs: list[float]):
    res_dl = []
    # https://camb.readthedocs.io/en/latest/CAMBdemo.html
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=67.66, ombh2=0.022, omch2=0.119, mnu=0.06,
                       omk=0, tau=0.06)
    pars.InitPower.set_params(As=2e-9, ns=0.965)
    pars.set_for_lmax(lmax, lens_potential_accuracy=1)
    pars.WantTensors = True
    results = camb.get_transfer_functions(pars)
    for r in rs:
        inflation_params = initialpower.InitialPowerLaw()
        inflation_params.set_params(ns=0.965, r=r)
        # warning OK here, not changing scalars
        results.power_spectra_from_transfer(inflation_params)
        dl = results.get_total_cls(lmax, CMB_unit='muK', raw_cl=False)
        # 0:TT, 1:EE, 2:BB, 3:TE
        res_dl.append(dl)
    return res_dl


def main(args: argparse.Namespace):
    # setting figure
    figsize = (8, 5)
    rect = (0.12, 0.12, 0.65, 0.83)
    fig1 = plt.figure(figsize=figsize)
    ax11 = fig1.add_axes(rect)

    # calculate the power spectrum
    dls = calc_dl(args.lmax, args.r)
    for r, dl in zip(args.r, dls):
        ax11.plot(np.arange(len(dl))[2:], dl[2:, 2],
                  label=r'$r={:.2f}$'.format(r))
    ax11.legend()

    # show observed results
    fig1.canvas.draw()
    text_pos = [rect[0]+rect[2]+0.01, rect[1]+rect[3]-0.02]
    for path in (Path(__file__).parent/'data').glob('*.json'):
        with open(path, 'r') as f:
            data = json.load(f)
        if "ignore" in data and data['ignore']:
            continue
        ell = np.array(data['ell'])
        d_ell = np.array(data['d_ell'])
        Cl = np.array(data['Cl'])
        d_Cl_plus = np.array(data['d_Cl_plus'])
        d_Cl_minus = np.array(data['d_Cl_minus'])
        limit = np.array(data['limit'], dtype=bool)
        if "name" in data:
            name = data['name']
        else:
            name = path.stem
        if "color" in data:
            color = data['color']
        else:
            color = 'black'
        notlim = np.logical_not(limit)
        ax11.errorbar(ell[notlim], Cl[notlim],
                      yerr=[d_Cl_minus[notlim], d_Cl_plus[notlim]],
                      xerr=d_ell[notlim],
                      label=None, fmt='o', color=color)
        lims = np.where(Cl[limit] > 0, Cl[limit] + d_Cl_plus[limit],
                        d_Cl_plus[limit])
        ax11.errorbar(ell[limit], lims, xerr=d_ell[limit],
                      label=None, color=color, marker='v', ls='None')
        txt = fig1.text(*text_pos, name, wrap=True, color=color,
                        ha='left', va='top')
        bbox = txt.get_window_extent()
        text_pos[1] = bbox.y0 / fig1.figbbox.y1 - 0.005

    # set the axes
    if not args.linear:
        ax11.set_xscale('log')
        ax11.set_yscale('log')
    ax11.set_xlabel(r'Multipole, $\ell$')
    ax11.set_ylabel(r'$(\ell(\ell+1)/2\pi)C_\ell\, \mathrm{[\mu K^2]}$')

    # save the figure
    output = Path(args.output)
    if not output.is_dir():
        output.mkdir(parents=True)
    plt.savefig(output/'B-mode-today.pdf')
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot CMB power spectrum data.')
    parser.add_argument('-r', help='set tensor-to-scalar ratio', nargs='*',
                        type=float, default=[0.0, 0.03])
    parser.add_argument('-lmax', help='maximum multipole',
                        type=int, default=2000)
    parser.add_argument('--linear', help='show the plot in linear scale',
                        action='store_true')
    parser.add_argument('-o', '--output', help='output directory',
                        type=str, default='output')
    args = parser.parse_args()
    main(args)
