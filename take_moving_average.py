"""
Author: Mikhail Schee
Created: 2022-06-17

This script is set up to take the moving average of Arctic Ocean profile data
that has been formatted into netcdfs by the `make_netcdf` function, adding
the variables 'ma_iT', 'ma_CT', 'ma_SP', 'ma_SA', and 'ma_sigma' to those files.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    1. Redistributions in source code must retain the accompanying copyright notice, this list of conditions, and the following disclaimer.
    2. Redistributions in binary form must reproduce the accompanying copyright notice, this list of conditions, and the following disclaimer in the documentation and/or other materials provided with the distribution.
    3. Names of the copyright holders must not be used to endorse or promote products derived from this software without prior written permission from the copyright holders.
    4. If any files are modified, you must cause the modified files to carry prominent notices stating that you changed the files and the date of any change.

Disclaimer

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS "AS IS" AND ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import os
import numpy as np
import pandas as pd
import xarray as xr
from datetime import datetime

import scipy.ndimage as ndimage
from scipy import interpolate

# Import the Thermodynamic Equation of Seawater 2010 (TEOS-10) from GSW
# For calculating density anomaly
import gsw

# The moving average window in dbar
c3 = 50#100

################################################################################
# Main execution
################################################################################
# Select the netcdfs to modify
ncs_to_modify = [
                #  'netcdfs/AIDJEX_BigBear.nc',
                #  'netcdfs/AIDJEX_BlueFox.nc',
                #  'netcdfs/AIDJEX_Caribou.nc',
                #  'netcdfs/AIDJEX_Snowbird.nc',
                 'netcdfs/ITP_010.nc',
                #  'netcdfs/ITP_33.nc',
                #  'netcdfs/ITP_34.nc',
                #  'netcdfs/ITP_35.nc',
                #  'netcdfs/ITP_41.nc',
                #  'netcdfs/ITP_42.nc',
                #  'netcdfs/ITP_43.nc',
                #  'netcdfs/SHEBA_Seacat.nc'
                 ]

# Get a list of all ITP netcdfs that have 3 digits in the file name
ncs_to_modify = [] 
ncs_available = os.listdir('netcdfs/')
for nc in ncs_available:
    itp_number = ''.join(filter(str.isdigit, nc))
    if len(itp_number) == 3 and 'ITP' in nc:
        ncs_to_modify.append('netcdfs/'+nc)
# print(ncs_to_modify)
# exit(0)

# Loop through the netcdfs to modify
for my_nc in ncs_to_modify:
    print('')
    print('Reading',my_nc)
    # Load in with xarray
    ds = xr.load_dataset(my_nc)

    gattrs_to_print = ['Last modified', 'Last modification', 'Moving average window']

    # See the variables before
    for attr in gattrs_to_print:
        print('\t',attr+':',ds.attrs[attr])

    print('making changes')

    ## Get the moving average profiles
    # Convert a subset of the dataset to a dataframe
    df = ds[['press','iT','CT','PT','SP','SA','prof_no']].squeeze().to_dataframe()
    # Get the original dimensions of the data to reshape the arrays later
    len0 = len(df.index.get_level_values(0).unique())
        # Had issues with ITP11, so I had to add `prof_no` to the dataframe and count
        #   the unique values
    len0 = len(list(set(df['prof_no'].values)))
    len1 = len(df.index.get_level_values(1).unique())
    # Use the pandas `rolling` function to get the moving average
    #   center=True makes the first and last window/2 of the profiles are masked
    #   win_type='boxcar' uses a rectangular window shape
    #   on='press' means it will take `press` as the index column
    #   .mean() takes the average of the rolling
    df1 = df.rolling(window=c3, center=True, win_type='boxcar', on='press').mean()
    # Put the moving average profiles for temperature, salinity, and density into the dataset
    ds['ma_iT'].values = df1['iT'].values.reshape((len0, len1))
    ds['ma_CT'].values = df1['CT'].values.reshape((len0, len1))
    ds['ma_PT'].values = df1['PT'].values.reshape((len0, len1))
    ds['ma_SP'].values = df1['SP'].values.reshape((len0, len1))
    ds['ma_SA'].values = df1['SA'].values.reshape((len0, len1))
    ds['ma_sigma'].values= gsw.sigma1(ds['ma_SP'], ds['ma_CT'])

    # Update the global variables:
    ds.attrs['Last modified'] = str(datetime.now())
    ds.attrs['Last modification'] = 'Added moving averages with '+str(c3)+' dbar window'
    ds.attrs['Moving average window'] = str(c3)+' dbar'

    # Write out to netcdf
    print('Writing data to',my_nc)
    ds.to_netcdf(my_nc, 'w')

    # Load in with xarray
    ds2 = xr.load_dataset(my_nc)

    # See the variables after
    for attr in gattrs_to_print:
        print('\t',attr+':',ds2.attrs[attr])
