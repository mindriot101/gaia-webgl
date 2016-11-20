#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import fitsio
import numpy as np


def convert_to_cartesian(ra, dec, dist_parsec):
    r = dist_parsec # np.log10(dist_parsec)
    theta = np.radians(ra)
    phi = np.radians(dec)

    x = r * np.cos(theta) * np.sin(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(phi)
    return x, y, z


def main():
    files = glob.iglob('gaia_data/Gaia/tgas_source/fits/*.fits')
    for filename in files:
        output_filename = os.path.splitext(
            os.path.basename(filename))[0] + '_cartesian.fits'
        if os.path.isfile(output_filename):
            continue

        print(filename, output_filename)
        with fitsio.FITS(filename) as infile:
            cat = infile[1]
            ra = cat['ra'].read()
            dec = cat['dec'].read()
            parallax = cat['parallax'].read()
            gmag = cat['phot_g_mean_mag'].read()

        dist_parsec = 1. / parallax
        ind = ((dist_parsec > 0) &
               (gmag > 0))
        assert ind.any()

        x, y, z = convert_to_cartesian(ra, dec, dist_parsec)

        with fitsio.FITS(output_filename, 'rw', clobber=True) as outfile:
            outfile.write({
                'x': x,
                'y': y,
                'z': z,
                'gmag': gmag,
            })


if __name__ == '__main__':
    main()
