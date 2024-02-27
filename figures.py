"""
Author: Mikhail Schee
Created: 2022-08-18

This script is set up to make figures of Arctic Ocean profile data that has been
formatted into netcdfs by the `make_netcdf` function.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    1. Redistributions in source code must retain the accompanying copyright notice, this list of conditions, and the following disclaimer.
    2. Redistributions in binary form must reproduce the accompanying copyright notice, this list of conditions, and the following disclaimer in the documentation and/or other materials provided with the distribution.
    3. Names of the copyright holders must not be used to endorse or promote products derived from this software without prior written permission from the copyright holders.
    4. If any files are modified, you must cause the modified files to carry prominent notices stating that you changed the files and the date of any change.

Disclaimer

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS "AS IS" AND ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

"""
Note: You unfortunately cannot pickle plots with parasite axes. So, the pickling
functionality won't work if you try to make a plot with the box and whisker plot
in an inset.

The Jupyter notebook Create_Figures.ipynb offers detailed explanations of each 
plot created by this script.

NOTE: BEFORE YOU RUN THIS SCRIPT

This script expects that the following files exist:
netcdfs/ITP_2.nc
netcdfs/ITP_3.nc

and that they have been created by running the following scripts in this order:
make_netcdf.py
take_moving_average.py
cluster_data.py
"""

# For custom analysis functions
import analysis_helper_functions as ahf

# BGOS_S_range = [34.1, 34.76]
BGOS_S_range = [34.366, 34.9992]
LHW_S_range = [34.366, 35.5]
test_S_range = [34.4, 34.6]
AIDJEX_S_range = [34.366, 35.0223]

# Axis limits
x_ax_lims_SA = {'x_lims':[LHW_S_range[0], 35.01]}

### Filters for reproducing plots from Timmermans et al. 2008
ITP2_p_range = [185,300]
ITP2_S_range = [34.05,34.75]
ITP2_m_pts = 170
# Timmermans 2008 Figure 4 depth range
T2008_fig4_y_lims = {'y_lims':[260,220]}
# Timmermans 2008 Figure 4 shows profile 185
T2008_fig4_pfs = [183, 185, 187]
# Filters used in Timmermans 2008 T-S and aT-BS plots
T2008_p_range = [180,300]
T2008_fig5a_x_lims  = {'x_lims':[34.05,34.75]}
T2008_fig5a_ax_lims = {'x_lims':[34.05,34.75], 'y_lims':[-1.3,0.5]}
T2008_fig6a_ax_lims = {'x_lims':[0.027002,0.027042], 'y_lims':[-13e-6,3e-6]}
# The actual limits are above, but need to adjust the x lims for some reason
T2008_fig6a_ax_lims = {'x_lims':[0.026838,0.026878], 'y_lims':[-13e-6,3e-6]}

# A list of many profiles to plot from ITP2
start_pf = 1
import numpy as np
n_pfs_to_plot = 50
ITP2_some_pfs = list(np.arange(start_pf, start_pf+(n_pfs_to_plot*2), 2))

# For showing multiple layers grouped into one cluster
ITP2_some_pfs_0 = [87, 89, 95, 97, 99, 101, 103, 105, 109, 111]
ITP2_some_pfs_ax_lims_0 = {'y_lims':[245,220]}
# For showing one layer split into multiple clusters
ITP2_some_pfs_1 = [67, 69, 73, 75, 81, 83, 91, 93, 97, 99]
ITP2_some_pfs_ax_lims_1 = {'y_lims':[295,270]}

# For showing examples of shallow profiles
ITP35_some_pfs0 = [7,15,23,47,55,63,71]
# For showing examples of middle incomplete profiles
ITP35_some_pfs1 = [3,11,19,27,51,59,67]
# For showing examples of full profiles
ITP35_some_pfs2 = [1,9,17,25,49,57,65,73]

### Filters for reproducing plots from Lu et al. 2022
Lu2022_p_range = [200,355]
Lu2022_T_range = [-1.0,0.9]
Lu2022_S_range = [34.21,34.82]
Lu2022_m_pts = 580

################################################################################
# Make dictionaries for what data to load in and analyze
################################################################################

# All profiles from all sources in this study
# all_sources = {'AIDJEX_BigBear':'all','AIDJEX_BlueFox':'all','AIDJEX_Caribou':'all','AIDJEX_Snowbird':'all','ITP_2':'all','ITP_3':'all'}
all_sources = {'AIDJEX_BigBear':'all','AIDJEX_BlueFox':'all','AIDJEX_Caribou':'all','AIDJEX_Snowbird':'all','ITP_33':'all','ITP_34':'all','ITP_35':'all','ITP_41':'all','ITP_42':'all','ITP_43':'all','SHEBA_Seacat':'all'}

# All profiles from all ITPs in this study
all_ITPs = {'ITP_2':'all','ITP_3':'all','ITP_35':'all','ITP_41':'all','ITP_42':'all','ITP_43':'all'}
all_ITPs = {'ITP_001':'all',
            'ITP_002':'all',
            'ITP_003':'all',
            'ITP_004':'all',
            'ITP_005':'all',
            'ITP_006':'all',
            'ITP_007':'all',
            'ITP_008':'all',
            'ITP_009':'all',
            'ITP_010':'all',
            'ITP_011':'all',
            'ITP_012':'all',
            # 'ITP_013':'all',
            # 'ITP_014':'all',
            # 'ITP_015':'all',
            # 'ITP_016':'all',
            # 'ITP_017':'all',
            # 'ITP_018':'all',
            # 'ITP_019':'all',
            # 'ITP_021':'all',
            # 'ITP_022':'all',
            # 'ITP_023':'all',
            # 'ITP_024':'all',
            # 'ITP_025':'all',
            # 'ITP_026':'all',
            # 'ITP_027':'all',
            # 'ITP_028':'all',
            # 'ITP_029':'all',
            # 'ITP_030':'all',
            # 'ITP_032':'all',
            # 'ITP_033':'all',
            # 'ITP_034':'all',
            # 'ITP_035':'all',
            # 'ITP_036':'all',
            # 'ITP_037':'all',
            # 'ITP_038':'all',
            # 'ITP_041':'all',
            # 'ITP_042':'all',
            # 'ITP_043':'all',
            # 'ITP_047':'all',
            # 'ITP_048':'all',
            # 'ITP_049':'all',
            # 'ITP_051':'all',
            # 'ITP_052':'all',
            # 'ITP_053':'all',
            # 'ITP_054':'all',
            # 'ITP_055':'all',
            # 'ITP_056':'all',
            # 'ITP_057':'all',
            # 'ITP_058':'all',
            # 'ITP_059':'all',
            # 'ITP_060':'all',
            # 'ITP_061':'all',
            # 'ITP_062':'all',
            # 'ITP_063':'all',
            # 'ITP_064':'all',
            # 'ITP_065':'all',
            # 'ITP_068':'all',
            # 'ITP_069':'all',
            # 'ITP_070':'all',
            # 'ITP_072':'all',
            # 'ITP_073':'all',
            # 'ITP_074':'all',
            # 'ITP_075':'all',
            # 'ITP_076':'all',
            # 'ITP_077':'all',
            # 'ITP_078':'all',
            # 'ITP_079':'all',
            # 'ITP_080':'all',
            # 'ITP_081':'all',
            # 'ITP_082':'all',
            # 'ITP_083':'all',
            # 'ITP_084':'all',
            # 'ITP_085':'all',
            # 'ITP_086':'all',
            # 'ITP_087':'all',
            # 'ITP_088':'all',
            # 'ITP_089':'all',
            # 'ITP_090':'all',
            # 'ITP_091':'all',
            # 'ITP_092':'all',
            # 'ITP_094':'all',
            # 'ITP_095':'all',
            # 'ITP_097':'all',
            # 'ITP_098':'all',
            # 'ITP_099':'all',
            # 'ITP_100':'all',
            # 'ITP_101':'all',
            # 'ITP_102':'all',
            # 'ITP_103':'all',
            # 'ITP_104':'all',
            # 'ITP_105':'all',
            # 'ITP_107':'all',
            # 'ITP_108':'all',
            # 'ITP_109':'all',
            # 'ITP_110':'all',
            # 'ITP_111':'all',
            # 'ITP_113':'all',
            # 'ITP_114':'all',
            # 'ITP_116':'all'
            }
all_BGOS = {'ITP_33':'all','ITP_34':'all','ITP_35':'all','ITP_41':'all','ITP_42':'all','ITP_43':'all'}

# Sets of ITPs within the CB that appear within certain time ranges
## 2004-08-20 00:00:01 to 2004-09-29 00:00:05
CB_ITPs_0a = {'ITP_002':'all'}
## 2005-08-16 06:00:01 to 
CB_ITPs_0b = {'ITP_001':'all',
            #   'ITP_002':'all', # Not in this time range
              'ITP_003':'all',
              'ITP_004':'all',
              'ITP_005':'all',
              'ITP_006':'all',
            #   'ITP_007':'all', # Not in CB
              'ITP_008':'all',
            #   'ITP_009':'all', # Not in CB
            #   'ITP_010':'all', # Not in CB
              'ITP_011':'all', # can't time slice? but only sometimes
            #   'ITP_012':'all', # Not in CB
            #   'ITP_013':'all',  # something weird is going on here
            #   'ITP_014':'all', # Not in CB
            #   'ITP_015':'all', # Not in CB
            #   'ITP_016':'all', # Not in CB
            #   'ITP_017':'all', # Not in CB
              'ITP_018':'all',
            #   'ITP_019':'all', # Not in CB
              'ITP_021':'all',
              'ITP_022':'all',
              'ITP_023':'all',
            #   'ITP_024':'all', # Not in CB
              'ITP_025':'all',
              'ITP_026':'all',
              'ITP_027':'all',
              'ITP_028':'all',
              'ITP_029':'all',
              'ITP_030':'all',
              'ITP_032':'all',
              'ITP_033':'all',
              'ITP_034':'all',
              'ITP_035':'all',
              'ITP_036':'all',
              'ITP_037':'all',
              'ITP_038':'all',
              }

# Sets of ITPs within the BGR that appear within certain time ranges
## 2004-08-20 00:00:01 to 2004-09-29 00:00:05, duration: 41 days
BGR_ITPs_0a = {'ITP_002':'all'}
## 2005-08-16 06:00:01 to 2009-08-31 00:00:08, gap: 320 days, duration: 1477 days
BGR_ITPs_0x = { 'ITP_001':'all',
                # 'ITP_002':'all', # Not in this time range
                'ITP_003':'all',
                'ITP_004':'all',
                'ITP_005':'all',
                'ITP_006':'all',
                # 'ITP_007':'all', # Not in BGR
                'ITP_008':'all',
                # 'ITP_009':'all', # Not in BGR
                # 'ITP_010':'all', # Not in BGR
                'ITP_011':'all', # can't time slice? but only sometimes
                # 'ITP_012':'all', # Not in BGR
                'ITP_013':'all',  # something weird is going on here
                # 'ITP_014':'all', # Not in BGR
                # 'ITP_015':'all', # Not in BGR
                # 'ITP_016':'all', # Not in BGR
                # 'ITP_017':'all', # Not in BGR
                'ITP_018':'all',
                # 'ITP_019':'all', # Not in BGR
                'ITP_021':'all',
                # 'ITP_022':'all', # Not in BGR
                # 'ITP_023':'all', # Not in BGR
                # 'ITP_024':'all', # Not in BGR
                'ITP_025':'all', 
                # 'ITP_026':'all', # Not in BGR
                # 'ITP_027':'all', # Not in BGR
                # 'ITP_028':'all', # Not in BGR
                # 'ITP_029':'all', # Not in BGR
                'ITP_030':'all',
                }
## 2005-08-16 06:00:01 to 2007-01-08 18:00:03, gap: 320 days, duration: 511 days
BGR_ITPs_0b = { 'ITP_001':'all',
                # 'ITP_002':'all', # Not in this time range
                'ITP_003':'all'
                }
## 2006-09-03 06:00:01 to 2008-05-13 00:00:02, overlap: 128 days, duration: 619 days
BGR_ITPs_0c = { 'ITP_004':'all',
                'ITP_005':'all',
                'ITP_006':'all'
                }
## 2007-08-13 00:00:01 to 2008-09-15 00:00:04, overlap: 275 days, duration: 400 days
BGR_ITPs_0d = { # 'ITP_007':'all', # Not in BGR
                'ITP_008':'all',
                # 'ITP_009':'all', # Not in BGR
                # 'ITP_010':'all', # Not in BGR
                # 'ITP_011':'all', # Not in this time period, can't time slice
                # 'ITP_012':'all', # Not in BGR
                'ITP_013':'all',  # Can't time slice
                # 'ITP_014':'all', # Not in BGR
                # 'ITP_015':'all', # Not in BGR
                # 'ITP_016':'all', # Not in BGR
                # 'ITP_017':'all', # Not in BGR
                'ITP_018':'all',
                # 'ITP_019':'all', # Not in BGR
                'ITP_021':'all',
                # 'ITP_022':'all', # Not in BGR
                # 'ITP_023':'all', # Not in BGR
                # 'ITP_024':'all', # Not in BGR
                # 'ITP_025':'all', # Not in this time period
                # 'ITP_026':'all', # Not in BGR
                # 'ITP_027':'all', # Not in BGR
                # 'ITP_028':'all', # Not in BGR
                # 'ITP_029':'all', # Not in BGR
                'ITP_030':'all',
                }
## 2008-09-21 00:00:05 to 2009-08-31 00:00:08, gap: 7 days, duration: 345 days
BGR_ITPs_0e = { 'ITP_008':'all',
                # 'ITP_009':'all', # Not in BGR
                # 'ITP_010':'all', # Not in BGR
                'ITP_011':'all', # Can't time slice
                # 'ITP_012':'all', # Not in BGR
                # 'ITP_013':'all',  # Not in this time period, can't time slice
                # 'ITP_014':'all', # Not in BGR
                # 'ITP_015':'all', # Not in BGR
                # 'ITP_016':'all', # Not in BGR
                # 'ITP_017':'all', # Not in BGR
                # 'ITP_018':'all', # Not in this time period
                # 'ITP_019':'all', # Not in BGR
                'ITP_021':'all', 
                # 'ITP_022':'all', # Not in BGR
                # 'ITP_023':'all', # Not in BGR
                # 'ITP_024':'all', # Not in BGR
                'ITP_025':'all', 
                # 'ITP_026':'all', # Not in BGR
                # 'ITP_027':'all', # Not in BGR
                # 'ITP_028':'all', # Not in BGR
                # 'ITP_029':'all', # Not in BGR
                # 'ITP_030':'all', # Not in this time period
                }
## 2009-10-04 06:00:02 to 2010-06-08 00:00:07, gap: 33 days, duration: 248 days
BGR_ITPs_0f = { 'ITP_032':'all',
                'ITP_033':'all',
                'ITP_034':'all',
                'ITP_035':'all',
                }
## 2010-06-16 00:00:06 to 2013-08-12 00:00:06, duration: 1154 days
BGR_ITPs_0y = { 'ITP_033':'all',
                # 'ITP_036':'all', # Not in BGR
                # 'ITP_037':'all', # Not in BGR
                # 'ITP_038':'all', # Not in BGR
                'ITP_041':'all',
                'ITP_042':'all',
                'ITP_043':'all',
                # 'ITP_047':'all', # Not in BGR
                # 'ITP_048':'all', # Not in BGR
                # 'ITP_049':'all', # Not in BGR
                # 'ITP_051':'all', # Not in BGR
                'ITP_052':'all',
                'ITP_053':'all',
                'ITP_054':'all',
                'ITP_055':'all',
                # 'ITP_056':'all', ?
                # 'ITP_057':'all', ?
                # 'ITP_058':'all', ?
                # 'ITP_059':'all',?
                # 'ITP_060':'all',?
                # 'ITP_061':'all',?
                'ITP_062':'all',
                # 'ITP_063':'all',?
                'ITP_064':'all',
                'ITP_065':'all',
                }
## 2010-06-16 00:00:06 to 2011-06-08 00:00:06, gap: 8 days, duration: 358 days
BGR_ITPs_0g = { 'ITP_033':'all',
                # 'ITP_036':'all', # Not in BGR
                # 'ITP_037':'all', # Not in BGR
                # 'ITP_038':'all', # Not in BGR
                'ITP_041':'all',
                'ITP_042':'all',
                'ITP_043':'all'
                }
## 2011-06-11 00:00:05 to 2012-08-06 06:00:05, gap: 2 days, duration: 423 days
BGR_ITPs_0h = { 'ITP_041':'all',
                # 'ITP_042':'all', # Not in this time period
                # 'ITP_043':'all', # Not in this time period
                # 'ITP_047':'all', # Not in BGR
                # 'ITP_048':'all', # Not in BGR
                # 'ITP_049':'all', # Not in BGR
                # 'ITP_051':'all', # Not in BGR
                'ITP_052':'all',
                'ITP_053':'all',
                'ITP_054':'all',
                'ITP_055':'all'
                }
## 2012-08-08 00:00:07 to 2013-08-23 12:02:02, gap: 1 day, duration: 381 days
BGR_ITPs_0i = { 'ITP_041':'all',
                # 'ITP_042':'all', # Not in this time period
                # 'ITP_043':'all', # Not in this time period
                # 'ITP_047':'all', # Not in BGR
                # 'ITP_048':'all', # Not in BGR
                # 'ITP_049':'all', # Not in BGR
                # 'ITP_051':'all', # Not in BGR
                # 'ITP_052':'all', # Not in this time period
                # 'ITP_053':'all', # Not in this time period
                # 'ITP_054':'all', # Not in this time period
                # 'ITP_055':'all', # Not in this time period
                # 'ITP_056':'all', # Not in BGR
                # 'ITP_057':'all', # Not in BGR
                # 'ITP_058':'all', # Not in BGR
                # 'ITP_059':'all', # Not in BGR
                # 'ITP_060':'all', # Not in BGR
                # 'ITP_061':'all', # Not in BGR
                'ITP_062':'all',
                # 'ITP_063':'all', # Not in BGR
                'ITP_064':'all',
                'ITP_065':'all',
                }
## 2013-08-22 00:02:02 to 2016-05-02 00:02:01, duration: 985 days
BGR_ITPs_0z = { 'ITP_064':'all',
                # 'ITP_065':'all', # Doesn't appear in this time period
                'ITP_068':'all',
                'ITP_069':'all',
                'ITP_070':'all',
                # 'ITP_072':'all', # Not in BGR
                # 'ITP_073':'all', # Not in BGR
                # 'ITP_074':'all', # Not in BGR
                # 'ITP_075':'all', # Not in BGR
                # 'ITP_076':'all', # Not in BGR
                'ITP_077':'all',
                'ITP_078':'all',
                'ITP_079':'all',
                'ITP_080':'all',
                'ITP_081':'all',
                'ITP_082':'all',
                # 'ITP_083':'all', # Not in BGR
                'ITP_084':'all',
                'ITP_085':'all',
                'ITP_086':'all',
                'ITP_087':'all',
                'ITP_088':'all',
                'ITP_089':'all',
                # 'ITP_090':'all', # Not in BGR
                # 'ITP_091':'all', # Not in BGR
                # 'ITP_092':'all', # Not in BGR
                # 'ITP_094':'all', # Not in BGR
                # 'ITP_095':'all', # Not in BGR
                }
## 2013-08-26 00:02:01 to 2014-10-01 00:02:01, gap: 2 days, duration: 402 days
BGR_ITPs_0j = { 'ITP_068':'all',
                'ITP_069':'all',
                'ITP_070':'all',
                # 'ITP_072':'all', # Not in BGR
                # 'ITP_073':'all', # Not in BGR
                # 'ITP_074':'all', # Not in BGR
                # 'ITP_075':'all', # Not in BGR
                # 'ITP_076':'all', # Not in BGR
                'ITP_077':'all',
                'ITP_078':'all',
                'ITP_079':'all'
                }
## 2014-08-14 00:02:01 to 2015-09-04 00:02:00, overlap: 49 days, duration: 387 days
BGR_ITPs_0k = { 'ITP_080':'all',
                'ITP_081':'all',
                'ITP_082':'all',
                # 'ITP_083':'all', # Not in BGR
                'ITP_084':'all',
                'ITP_085':'all',
                'ITP_086':'all',
                'ITP_087':'all'
                }
## 2015-09-06 00:02:01 to 2016-05-02 00:02:01, gap: 1 day, duration: 240 days
BGR_ITPs_0l = { 'ITP_082':'all',
                # 'ITP_083':'all', # Not in BGR
                # 'ITP_084':'all', # Not in this time period
                # 'ITP_085':'all', # Not in this time period
                # 'ITP_086':'all', # Not in this time period
                # 'ITP_087':'all', # Not in this time period
                'ITP_088':'all',
                'ITP_089':'all',
                # 'ITP_090':'all', # Not in BGR
                # 'ITP_091':'all', # Not in BGR
                # 'ITP_092':'all', # Not in BGR
                # 'ITP_094':'all', # Not in BGR
                # 'ITP_095':'all', # Not in BGR
                }
## 2016-10-03 00:02:02 to 2017-08-04 00:02:01, gap: 153 days, duration: 306 days
BGR_ITPs_0m = { 'ITP_097':'all',
                # 'ITP_098':'all', # Just barely outside BGR
                'ITP_099':'all',
                }
## 2017-09-17 00:02:02 to 2018-07-21 00:02:02, gap: 43 days, duration: 308 days
BGR_ITPs_0n = { 'ITP_097':'all',
                'ITP_100':'all',
                'ITP_101':'all',
                # 'ITP_102':'all', # Not in BGR
                # 'ITP_103':'all', # Not in this time period
                # 'ITP_104':'all', # Not in this time period
                # 'ITP_105':'all', # Not in this time period
                # 'ITP_107':'all', # Not in this time period
                'ITP_108':'all',
                }
## 2018-09-19 00:02:03 to 2019-04-14 00:02:02, gap: 59 days, duration: 208 days
BGR_ITPs_0o = { 'ITP_103':'all',
                'ITP_104':'all',
                'ITP_105':'all',
                'ITP_107':'all',
                # 'ITP_108':'all', # Not in this time period
                'ITP_109':'all',
                'ITP_110':'all',
                }
## 2019-05-01 00:02:02 to 2019-08-31 00:02:03, gap: 16 days, duration: 123 days
BGR_ITPs_0p = { 'ITP_103':'all',
                # 'ITP_104':'all', # Not in this time period
                'ITP_105':'all',
                'ITP_107':'all',
                # 'ITP_108':'all', # Not in this time period
                # 'ITP_109':'all', # Not in this time period
                'ITP_110':'all',
                # 'ITP_111':'all', # Not in BGR
                }
## 2019-09-20 00:02:03 to 2020-04-02 17:33:46, gap: 19 days, duration: 196 days
BGR_ITPs_0q = { 'ITP_113':'all',
                'ITP_114':'all',
                # 'ITP_116':'all', # Not in BGR
                'ITP_117':'all',
                'ITP_118':'all',
                }
## 2020-05-20 17:33:46 to 2021-08-31 00:02:02, gap: 47 days, duration: 469 days
BGR_ITPs_0r = { 'ITP_113':'all',
                'ITP_114':'all',
                # 'ITP_116':'all', # Not in BGR
                # 'ITP_117':'all', # Not in this time period
                # 'ITP_118':'all', # Not in this time period
                'ITP_120':'all',
                'ITP_121':'all',
                }
## 
BGR_ITPs_0s = { 'ITP_113':'all',
                'ITP_114':'all',
                # 'ITP_116':'all', # Not in BGR
                'ITP_117':'all',
                'ITP_118':'all',
                'ITP_120':'all',
                'ITP_121':'all',
                'ITP_122':'all',
                'ITP_123':'all',
                'ITP_125':'all',
                'ITP_128':'all',
                }

## All
BGR_ITPs_all = {**BGR_ITPs_0a, **BGR_ITPs_0b, **BGR_ITPs_0c, **BGR_ITPs_0d, **BGR_ITPs_0e, **BGR_ITPs_0f, **BGR_ITPs_0g, **BGR_ITPs_0h, **BGR_ITPs_0i, **BGR_ITPs_0j, **BGR_ITPs_0k, **BGR_ITPs_0l, **BGR_ITPs_0m, **BGR_ITPs_0n, **BGR_ITPs_0o, **BGR_ITPs_0p, **BGR_ITPs_0q, **BGR_ITPs_0r, **BGR_ITPs_0s}

# Sets of ITPs within the BGR by year-long time periods
## 2004-08-20 00:00:01 to 2004-09-29 00:00:05, duration: 41 days
BGRITPs04   = {'ITP_002':'all'}
## 2005-08-16 06:00:01 to 2006-08-14 18:00:03, gap: 320 days, duration: 
BGRITPs0506 = { 'ITP_001':'all',
                # 'ITP_002':'all', # Not in this time range
                'ITP_003':'all',
                }
## 2006-08-15 06:00:02 to 2007-08-14 12:00:02, gap: 1 day, duration: 
BGRITPs0607 = { 'ITP_001':'all',
                # 'ITP_002':'all', # Not in this time range
                'ITP_003':'all',
                'ITP_004':'all',
                'ITP_005':'all',
                'ITP_006':'all',
                # 'ITP_007':'all', # Not in BGR
                'ITP_008':'all',
                # 'ITP_009':'all', # Not in BGR
                # 'ITP_010':'all', # Not in BGR
                # 'ITP_011':'all', # Not in this time range
                # 'ITP_012':'all', # Not in BGR
                'ITP_013':'all',  
                # 'ITP_014':'all', # Not in BGR
                # 'ITP_015':'all', # Not in BGR
                # 'ITP_016':'all', # Not in BGR
                # 'ITP_017':'all', # Not in BGR
                }
## 2007-08-15 00:00:01 to 2008-08-14 00:24:17, gap: 1 day, duration: 
BGRITPs0708 = { 'ITP_004':'all',
                'ITP_005':'all',
                'ITP_006':'all',
                # 'ITP_007':'all', # Not in BGR
                'ITP_008':'all',
                # 'ITP_009':'all', # Not in BGR
                # 'ITP_010':'all', # Not in BGR
                # 'ITP_011':'all', # Not in this time period
                # 'ITP_012':'all', # Not in BGR
                'ITP_013':'all',
                # 'ITP_014':'all', # Not in BGR
                # 'ITP_015':'all', # Not in BGR
                # 'ITP_016':'all', # Not in BGR
                # 'ITP_017':'all', # Not in BGR
                'ITP_018':'all',
                # 'ITP_019':'all', # Not in BGR
                'ITP_021':'all',
                # 'ITP_022':'all', # Not in BGR
                # 'ITP_023':'all', # Not in BGR
                # 'ITP_024':'all', # Not in BGR
                # 'ITP_025':'all', # Not in this time period
                # 'ITP_026':'all', # Not in BGR
                # 'ITP_027':'all', # Not in BGR
                # 'ITP_028':'all', # Not in BGR
                # 'ITP_029':'all', # Not in BGR
                'ITP_030':'all',
                }
## 2008-08-15 00:00:03 to 2009-08-12 00:00:07, gap: 1 day, duration: 
BGRITPs0809 = { 'ITP_008':'all',
                # 'ITP_009':'all', # Not in BGR
                # 'ITP_010':'all', # Not in BGR
                'ITP_011':'all',
                # 'ITP_012':'all', # Not in BGR
                # 'ITP_013':'all', # Not in this time period
                # 'ITP_014':'all', # Not in BGR
                # 'ITP_015':'all', # Not in BGR
                # 'ITP_016':'all', # Not in BGR
                # 'ITP_017':'all', # Not in BGR
                'ITP_018':'all',
                # 'ITP_019':'all', # Not in BGR
                'ITP_021':'all',
                # 'ITP_022':'all', # Not in BGR
                # 'ITP_023':'all', # Not in BGR
                # 'ITP_024':'all', # Not in BGR
                'ITP_025':'all',
                # 'ITP_026':'all', # Not in BGR
                # 'ITP_027':'all', # Not in BGR
                # 'ITP_028':'all', # Not in BGR
                # 'ITP_029':'all', # Not in BGR
                'ITP_030':'all',
                }
## 2009-08-19 00:00:07 to 2010-08-14 00:00:06
BGRITPs0910 = { 'ITP_021':'all',
                # 'ITP_022':'all', # Not in BGR
                # 'ITP_023':'all', # Not in BGR
                # 'ITP_024':'all', # Not in BGR
                # 'ITP_025':'all', # Not in this time period
                # 'ITP_026':'all', # Not in BGR
                # 'ITP_027':'all', # Not in BGR
                # 'ITP_028':'all', # Not in BGR
                # 'ITP_029':'all', # Not in BGR
                # 'ITP_030':'all', # Not in this time period
                'ITP_032':'all',
                'ITP_033':'all',
                'ITP_034':'all',
                'ITP_035':'all',
                # 'ITP_036':'all', # Not in BGR
                # 'ITP_037':'all', # Not in BGR
                # 'ITP_038':'all', # Not in BGR
                }
## 2010-08-15 00:00:06 to 2011-08-14 00:00:06
BGRITPs1011 = { 'ITP_033':'all',
                # 'ITP_034':'all', # Not in this time period
                # 'ITP_035':'all', # Not in this time period
                # 'ITP_036':'all', # Not in BGR
                # 'ITP_037':'all', # Not in BGR
                # 'ITP_038':'all', # Not in BGR
                'ITP_041':'all',
                'ITP_042':'all',
                'ITP_043':'all',
                }
## 2011-08-15 00:00:01 to 2012-08-14 00:00:07
BGRITPs1112 = { 'ITP_041':'all',
                # 'ITP_042':'all', # Not in this time period
                # 'ITP_043':'all', # Not in this time period
                # 'ITP_047':'all', # Not in BGR
                # 'ITP_048':'all', # Not in BGR
                # 'ITP_049':'all', # Not in BGR
                # 'ITP_051':'all', # Not in BGR
                'ITP_052':'all',
                'ITP_053':'all',
                'ITP_054':'all',
                'ITP_055':'all',
                }
## 2012-08-15 00:00:06 to 2013-08-12 00:00:06
BGRITPs1213 = { 'ITP_041':'all',
                # 'ITP_042':'all', # Not in this time period
                # 'ITP_043':'all', # Not in this time period
                # 'ITP_052':'all', # Not in this time period
                # 'ITP_053':'all', # Not in this time period
                # 'ITP_054':'all', # Not in this time period
                # 'ITP_055':'all', # Not in this time period
                # 'ITP_056':'all', # Not in BGR
                # 'ITP_057':'all', # Not in BGR
                # 'ITP_058':'all', # Not in BGR
                # 'ITP_059':'all', # Not in BGR
                # 'ITP_060':'all', # Not in BGR
                # 'ITP_061':'all', # Not in BGR
                'ITP_062':'all',
                # 'ITP_063':'all', # Not in BGR
                'ITP_064':'all',
                'ITP_065':'all',
                }
## 2013-08-22 00:02:02 to 2014-08-14 00:02:02
BGRITPs1314 = { 'ITP_064':'all',
                # 'ITP_065':'all', # Not in BGR
                'ITP_068':'all',
                'ITP_069':'all',
                'ITP_070':'all',
                # 'ITP_072':'all', # Not in BGR
                # 'ITP_073':'all', # Not in BGR
                # 'ITP_074':'all', # Not in BGR
                # 'ITP_075':'all', # Not in BGR
                # 'ITP_076':'all', # Not in BGR
                'ITP_077':'all',
                'ITP_078':'all',
                'ITP_079':'all',
                'ITP_080':'all',
                }
## 2014-08-15 00:02:02 to 2015-08-14 00:02:02
BGRITPs1415 = { 'ITP_077':'all',
                # 'ITP_078':'all', # Not in this time period
                'ITP_079':'all',
                'ITP_080':'all',
                'ITP_081':'all',
                'ITP_082':'all',
                # 'ITP_083':'all', # Not in BGR
                'ITP_084':'all',
                'ITP_085':'all',
                'ITP_086':'all',
                'ITP_087':'all',
                }
## 2015-08-15 00:02:01 to 2016-05-02 00:02:01
BGRITPs1516 = { 'ITP_082':'all',
                # 'ITP_083':'all', # Not in BGR
                # 'ITP_084':'all', # Not in this time period
                'ITP_085':'all',
                'ITP_086':'all',
                # 'ITP_087':'all', # Not in this time period
                'ITP_088':'all',
                'ITP_089':'all',
                # 'ITP_090':'all', # Not in BGR
                # 'ITP_091':'all', # Not in BGR
                # 'ITP_092':'all', # Not in BGR
                # 'ITP_094':'all', # Not in BGR
                # 'ITP_095':'all', # Not in BGR
                }
## 2016-10-03 00:02:02 to 2017-08-04 00:02:01
BGRITPs1617 = { 'ITP_097':'all',
                # 'ITP_098':'all', # Not in BGR
                'ITP_099':'all',
                }
## 2017-09-17 00:02:02 to 2018-07-21 00:02:02
BGRITPs1718 = { 'ITP_097':'all',
                # 'ITP_098':'all', # Not in BGR
                # 'ITP_099':'all', # Not in this time period
                'ITP_100':'all',
                'ITP_101':'all',
                # 'ITP_102':'all', # Not in BGR
                # 'ITP_103':'all', # Not in this time period
                # 'ITP_104':'all', # Not in this time period
                # 'ITP_105':'all', # Not in this time period
                # 'ITP_107':'all', # Not in this time period
                'ITP_108':'all',
                }
## 2018-09-19 00:02:03 to 2019-08-14 00:02:02
BGRITPs1819 = { 'ITP_103':'all',
                'ITP_104':'all',
                'ITP_105':'all',
                'ITP_107':'all',
                # 'ITP_108':'all', # Not in this time period
                'ITP_109':'all',
                'ITP_110':'all',
                }
## 2019-08-16 00:02:01 to 2020-08-14 17:33:46
BGRITPs1920 = { 'ITP_105':'all',
                # 'ITP_107':'all', # Not in this time period
                # 'ITP_108':'all', # Not in this time period
                # 'ITP_109':'all', # Not in this time period
                # 'ITP_110':'all', # Not in this time period
                # 'ITP_111':'all',
                'ITP_113':'all',
                'ITP_114':'all',
                # 'ITP_116':'all', # Not in BGR
                'ITP_117':'all',
                'ITP_118':'all',
                }
## 2020-08-18 17:33:46 to 2021-08-14 00:02:02
BGRITPs2021 = { 'ITP_113':'all',
                'ITP_114':'all',
                # 'ITP_116':'all', # Not in BGR
                # 'ITP_117':'all', # Not in this time period
                # 'ITP_118':'all', # Not in this time period
                'ITP_120':'all',
                'ITP_121':'all',
                }
## 2021-08-15 00:02:02 to 2022-08-11 12:02:02
BGRITPs2122 = { 'ITP_120':'all',
                'ITP_121':'all',
                'ITP_122':'all',
                'ITP_123':'all',
                # 'ITP_125':'all',
                # 'ITP_128':'all',
                }
## 2022-08-21 12:02:02 to 2022-12-23 00:02:02
BGRITPs2223 = { 'ITP_122':'all',
                # 'ITP_123':'all',
                # 'ITP_125':'all',
                # 'ITP_128':'all',
                }

## All
BGRITPs0508 = {**BGRITPs0506, **BGRITPs0607, **BGRITPs0708}
BGRITPs0511  = {**BGRITPs0506, **BGRITPs0607, **BGRITPs0708, **BGRITPs0809, **BGRITPs0910, **BGRITPs1011}
BGRITPsAll  = {**BGRITPs0506, **BGRITPs0607, **BGRITPs0708, **BGRITPs0809, **BGRITPs0910, **BGRITPs1011, **BGRITPs1112, **BGRITPs1213, **BGRITPs1314, **BGRITPs1415, **BGRITPs1516, **BGRITPs1617, **BGRITPs1718, **BGRITPs1819, **BGRITPs1920, **BGRITPs2021, **BGRITPs2122, **BGRITPs2223}

## Pre-clustered files
# Single time periods
BGRa_m110 = {'BGRa_mpts_110':'all'}
BGRb_m380 = {'BGRb_mpts_380':'all'}
BGRf_m310 = {'BGRf_mpts_310':'all'}
BGRm_m410 = {'BGRm_mpts_410':'all'}
BGRn_m240 = {'BGRn_mpts_240':'all'}
BGRo_m390 = {'BGRo_mpts_390':'all'}
ITP3t = {'ITP3t':'all'}
# by year
# BGR04   = {'BGR04':'all'}
# BGR0506 = {'BGR0506':'all'}
# BGR0607 = {'BGR0607':'all'}
# BGR0708 = {'BGR0708':'all'}
# With minimal variables to reduce size
BGR04   = {'minimal_BGR04':'all'}
BGR0506 = {'minimal_BGR0506':'all'}
BGR0607 = {'minimal_BGR0607':'all'}
BGR0708 = {'minimal_BGR0708':'all'}
BGR0809 = {'minimal_BGR0809':'all'}
BGR0910 = {'minimal_BGR0910':'all'}
BGR1011 = {'minimal_BGR1011':'all'}

# With m_pts fixed manually
# BGR04   = {'BGRm250_04':'all'}
# BGR0506 = {'BGRm350_0506':'all'}
# BGR0607 = {'BGRm350_0607':'all'}
# BGR0708 = {'BGRm350_0708':'all'}
# BGR05060708 = {'BGRm350_0506':'all', 'BGRm350_0607':'all', 'BGRm350_0708':'all'}
# BGR_all = {'BGRm350_0506':'all','BGRm350_0607':'all','BGRm350_0708':'all'}

# With m_pts fixed manually
# BGR04   = {'BGR04_clstrd':'all'}
# BGR04_clstrs_456 = {'BGR04_clstrs_456':'all'}
BGR0506 = {'BGR0506_clstrd':'all'}
BGR0607 = {'BGR0607_clstrd':'all'}
BGR0708 = {'BGR0708_clstrd':'all'}
BGR0809 = {'BGR0809_clstrd':'all'}
BGR0910 = {'BGR0910_clstrd':'all'}
BGR1011 = {'BGR1011_clstrd':'all'}

BGR0508 = {'BGR0508':'all'}
BGR050607 = {'BGR0506_clstrd':'all', 'BGR0607_clstrd':'all'}
BGR05060708 = {'BGR0506_clstrd':'all', 'BGR0607_clstrd':'all', 'BGR0708_clstrd':'all'}
BGR05060708_clstrs_456 = {'BGR05060708_clstrs_456':'all'}
BGR_all = {
            # 'BGR04_clstrd':'all',
            'BGR0506_clstrd':'all',
            'BGR0607_clstrd':'all',
            'BGR0708_clstrd':'all',
            'BGR0809_clstrd':'all',
            'BGR0910_clstrd':'all',
            'BGR1011_clstrd':'all',
        }

# With m_pts fixed automatically
BGR0506 = {'mpts_auto_BGR0506_clstrd':'all'}
BGR0607 = {'mpts_auto_BGR0607_clstrd':'all'}
BGR0708 = {'mpts_auto_BGR0708_clstrd':'all'}
BGR0809 = {'mpts_auto_BGR0809_clstrd':'all'}
BGR0910 = {'mpts_auto_BGR0910_clstrd':'all'}
BGR1011 = {'mpts_auto_BGR1011_clstrd':'all'}
BGR_all = {
            'mpts_auto_BGR0506_clstrd':'all',
            'mpts_auto_BGR0607_clstrd':'all',
            'mpts_auto_BGR0708_clstrd':'all',
            'mpts_auto_BGR0809_clstrd':'all',
            'mpts_auto_BGR0910_clstrd':'all',
            'mpts_auto_BGR1011_clstrd':'all',
        }

# Comparing time periods
BGRmn = {'BGRm_mpts_410':'all','BGRn_mpts_240':'all'}
BGRno = {'BGRn_mpts_240':'all','BGRo_mpts_390':'all'}
BGRmno = {'BGRm_mpts_410':'all','BGRn_mpts_240':'all','BGRo_mpts_390':'all'}

# # All profiles from certain ITPs
ITP2_all  = {'ITP_2':'all'}
ITP002_all  = {'ITP_002':'all'}
ITP003_all  = {'ITP_003':'all'}
# ITP33_all = {'ITP_33':'all'}
# ITP34_all = {'ITP_34':'all'}
# ITP35_all = {'ITP_35':'all'}
# ITP41_all = {'ITP_41':'all'}
# ITP42_all = {'ITP_42':'all'}
# ITP43_all = {'ITP_43':'all'}

# A list of many profiles to plot from ITP3
start_pf = 1331
import numpy as np
n_pfs_to_plot = 5
ITP3_some_pfs_1 = list(np.arange(start_pf, start_pf+(n_pfs_to_plot*2), 2))
ITP3_pfs1  = {'ITP_3':ITP3_some_pfs_1}
ITP35_pfs0 = {'ITP_35':ITP35_some_pfs0}
ITP35_pfs1 = {'ITP_35':ITP35_some_pfs1}
ITP35_pfs2 = {'ITP_35':ITP35_some_pfs2}

# Example profiles
# Coincident_pfs0 = {'AIDJEX_Snowbird':[138,140,142], 'SHEBA_Seacat':['SH36200'], 'ITP_33':[779, 781, 783]}
# ex_pfs1 = {'ITP_002':[188, 189, 208, 209]}

## Example profiles that appeared in other studies
ex_pfs1 = {
            'ITP_001':[1257],               # Shibley2017 Figure 3b, 800-0 m, 235-200 m
            # 'ITP_002':[113],                # Bebieva2019a Figure 1, 750-0 m, 385-230 m
            # 'ITP_002':[185],                # Timmermans2008 Figure 4, 260-220 m
            'ITP_003':[1073],               # Timmermans2008 Figure 2, 740-0 m, 290-240 m
            'ITP_004':[453],                # Lu2022 Figure 2, 750-0 m, 350-270 m
            'ITP_006':[475, 747],           # Toole2011 Figure 6, 300-0 m
            # 'ITP_008':[1301],               # Shibley2017 Figure 3a, 800-0 m, 260-230 m
            'ITP_041':[515],                # Bebieva2017(unpub) Figure 1, 750-0 m, 390-230 m
            'ITP_064':[377],                # vanderBoog2021a Figure A1, 750-250 m
          }
ex_pfs1_zoom_range = [280,250]

## Example profiles spaced roughly evenly in time
ex_pfs2 = {
            'ITP_001':[1,365,1457],
            'ITP_003':[701,1057],
            'ITP_004':[331,693],
            'ITP_005':[205],
            'ITP_006':[505],
            'ITP_008':[739],
            'ITP_011':[949,1345],
            'ITP_013':[209,621],
            'ITP_018':[389],
            'ITP_021':[391,747],
            'ITP_033':[263,441,625],
            'ITP_035':[297],
            'ITP_041':[271,449,631],
            'ITP_042':[83],
          }
## test quarterly slices
dfs1_q = ahf.Data_Filters(date_range=['2011/05/14 18:00:00','2011/05/16 00:00:00'])

ITP2_ex_pfs   = {'ITP_002':ITP2_some_pfs}
BGR04_ex_pfs  = {'BGR04':ITP2_some_pfs}

ITP2_ex_pfs_0 = {'ITP_002':ITP2_some_pfs_0}

################################################################################
# Create data filtering objects
print('- Creating data filtering objects')
################################################################################

dfs_all = ahf.Data_Filters(keep_black_list=True, cast_direction='any')
dfs0 = ahf.Data_Filters()
this_min_press = 400
dfs1 = ahf.Data_Filters(min_press=this_min_press)
dfs2 = ahf.Data_Filters(min_press_CT_max=400)

dfs_CB = ahf.Data_Filters(geo_extent='CB', keep_black_list=True, cast_direction='any')
dfs1_CB_0a = ahf.Data_Filters(geo_extent='CB', min_press=this_min_press)
dfs1_CB_0b = ahf.Data_Filters(geo_extent='CB', min_press=this_min_press)#, date_range=['2005/08/15 00:00:00','2010/07/22 00:00:00'])

# Beaufort Gyre Region
dfs1_BGR_0d = ahf.Data_Filters(min_press=this_min_press, date_range=['2007/08/11 00:00:00','2008/09/18 00:00:00'])
dfs1_BGR_0e = ahf.Data_Filters(min_press=this_min_press, date_range=['2008/09/18 00:00:00','2009/09/01 00:00:00'])
dfs1_BGR_0f = ahf.Data_Filters(min_press=this_min_press, date_range=['2009/08/31 00:00:08','2010/06/11 00:00:00'])
dfs1_BGR_0g = ahf.Data_Filters(min_press=this_min_press, date_range=['2010/06/11 00:00:00','2011/06/09 00:00:00'])
dfs1_BGR_0h = ahf.Data_Filters(min_press=this_min_press, date_range=['2011/06/09 00:00:00','2012/08/07 00:00:00'])
dfs1_BGR_0i = ahf.Data_Filters(min_press=this_min_press, date_range=['2012/08/07 00:00:00','2013/08/25 00:00:00'])
dfs1_BGR_0j = ahf.Data_Filters(min_press=this_min_press, date_range=['2013/08/25 00:00:00','2014/10/10 00:00:00'])
dfs1_BGR_0k = ahf.Data_Filters(min_press=this_min_press, date_range=['2013/08/25 00:00:00','2015/09/05 00:00:00'])
dfs1_BGR_0l = ahf.Data_Filters(min_press=this_min_press, date_range=['2015/09/05 00:00:00','2016/07/10 00:00:00'])
dfs1_BGR_0m = ahf.Data_Filters(min_press=this_min_press, date_range=['2016/07/10 00:00:00','2017/08/29 00:00:00'])
dfs1_BGR_0n = ahf.Data_Filters(min_press=this_min_press, date_range=['2017/08/29 00:00:00','2018/08/17 00:00:00'])
dfs1_BGR_0o = ahf.Data_Filters(min_press=this_min_press, date_range=['2018/08/17 00:00:00','2019/04/23 00:00:00'])
dfs1_BGR_0p = ahf.Data_Filters(min_press=this_min_press, date_range=['2019/04/23 00:00:00','2019/09/10 00:00:00'])
dfs1_BGR_0q = ahf.Data_Filters(min_press=this_min_press, date_range=['2019/09/10 00:00:00','2020/04/22 00:00:00'])
dfs1_BGR_0r = ahf.Data_Filters(min_press=this_min_press, date_range=['2020/04/22 00:00:00','2021/09/03 00:00:00'])
dfs1_BGR_0s = ahf.Data_Filters(min_press=this_min_press, date_range=['2020/07/01 00:00:00','2022/01/01 00:00:00'])

# Different time periods
dfs1_BGR0506 = ahf.Data_Filters(min_press=this_min_press, date_range=['2005/08/15 00:00:00','2006/08/15 00:00:00'])
dfs1_BGR0607 = ahf.Data_Filters(min_press=this_min_press, date_range=['2006/08/15 00:00:00','2007/08/15 00:00:00'])
dfs1_BGR0708 = ahf.Data_Filters(min_press=this_min_press, date_range=['2007/08/15 00:00:00','2008/08/15 00:00:00'])
dfs1_BGR0809 = ahf.Data_Filters(min_press=this_min_press, date_range=['2008/08/15 00:00:00','2009/08/15 00:00:00'])
dfs1_BGR0910 = ahf.Data_Filters(min_press=this_min_press, date_range=['2009/08/15 00:00:00','2010/08/15 00:00:00'])
dfs1_BGR1011 = ahf.Data_Filters(min_press=this_min_press, date_range=['2010/08/15 00:00:00','2011/08/15 00:00:00'])
dfs1_BGR1112 = ahf.Data_Filters(min_press=this_min_press, date_range=['2011/08/15 00:00:00','2012/08/15 00:00:00'])
dfs1_BGR1213 = ahf.Data_Filters(min_press=this_min_press, date_range=['2012/08/15 00:00:00','2013/08/15 00:00:00'])
dfs1_BGR1314 = ahf.Data_Filters(min_press=this_min_press, date_range=['2013/08/15 00:00:00','2014/08/15 00:00:00'])
dfs1_BGR1415 = ahf.Data_Filters(min_press=this_min_press, date_range=['2014/08/15 00:00:00','2015/08/15 00:00:00'])
dfs1_BGR1516 = ahf.Data_Filters(min_press=this_min_press, date_range=['2015/08/15 00:00:00','2016/08/15 00:00:00'])
dfs1_BGR1617 = ahf.Data_Filters(min_press=this_min_press, date_range=['2016/08/15 00:00:00','2017/08/15 00:00:00'])
dfs1_BGR1718 = ahf.Data_Filters(min_press=this_min_press, date_range=['2017/08/15 00:00:00','2018/08/15 00:00:00'])
dfs1_BGR1819 = ahf.Data_Filters(min_press=this_min_press, date_range=['2018/08/15 00:00:00','2019/08/15 00:00:00'])
dfs1_BGR1920 = ahf.Data_Filters(min_press=this_min_press, date_range=['2019/08/15 00:00:00','2020/08/15 00:00:00'])
dfs1_BGR2021 = ahf.Data_Filters(min_press=this_min_press, date_range=['2020/08/15 00:00:00','2021/08/15 00:00:00'])
dfs1_BGR2122 = ahf.Data_Filters(min_press=this_min_press, date_range=['2021/08/15 00:00:00','2022/08/15 00:00:00'])
dfs1_BGR2223 = ahf.Data_Filters(min_press=this_min_press, date_range=['2022/08/15 00:00:00','2023/08/15 00:00:00'])

## combo
dfs1_BGR0508 = ahf.Data_Filters(min_press=this_min_press, date_range=['2005/08/15 00:00:00','2008/08/15 00:00:00'])
dfs1_BGR0511 = ahf.Data_Filters(min_press=this_min_press, date_range=['2005/08/15 00:00:00','2011/08/15 00:00:00'])

# To filter pre-clustered files to just certain cluster labels
# dfs_clstr_lbl = ahf.Data_Filters(clstr_labels=[[-1, 0, 1, 2]])
dfs_clstr_lbl = ahf.Data_Filters(clstr_labels=[[16],[18],[14]])
dfs_clstr_lbl = ahf.Data_Filters(clstr_labels=[[29],[17],[20]])
# fg corresponding
dfs_clstr_lbl = ahf.Data_Filters(clstr_labels=[[16],[18]])
# fg NOT corresponding
dfs_clstr_lbl = ahf.Data_Filters(clstr_labels=[[16],[17]])
# fg 3 clusters
dfs_clstr_lbl = ahf.Data_Filters(clstr_labels=[[12,13,17]])
dfs_clstr_lbl1 = ahf.Data_Filters(clstr_labels=[[11,12,13]])
# No noise points
dfs_no_noise = ahf.Data_Filters(clstr_labels='no_noise')

################################################################################
# Create data sets by combining filters and the data to load in
print('- Creating data sets')
################################################################################

# ds_all_sources_all  = ahf.Data_Set(all_sources, dfs_all)
# ds_all_sources_up   = ahf.Data_Set(all_sources, dfs0)
# ds_all_sources_pmin = ahf.Data_Set(all_sources, dfs1)

## Example profiles
# ds_all_sources_ex_pfs = ahf.Data_Set(Coincident_pfs0, dfs_all)

## ITP

# ds_all_BGOS = ahf.Data_Set(all_BGOS, dfs_all)
# ds_all_BGOS = ahf.Data_Set(all_BGOS, dfs0)
# ds_BGOS = ahf.Data_Set(all_BGOS, dfs1)

# ds_all_ITP = ahf.Data_Set(all_ITPs, dfs_all)
# ds_all_ITP = ahf.Data_Set(all_ITPs, dfs_CB)

# ds_ITP = ahf.Data_Set(all_ITPs, dfs1_CB)

# ds_ITP2 = ahf.Data_Set(ITP002_all, dfs1)
# ds_ITP3 = ahf.Data_Set(ITP003_all, dfs1)
# ds_this_BGR = ds_ITP2

# ds_ITP_test = ahf.Data_Set({'ITP_098':'all'}, dfs_all)

## CB ITP datasets, by time period
# ds_CB_ITPs_0a = ahf.Data_Set(CB_ITPs_0a, dfs1_CB_0a)
# ds_CB_ITPs_0b = ahf.Data_Set(CB_ITPs_0b, dfs1_CB_0b)
# ds_CB_ITPs_0b = ahf.Data_Set(CB_ITPs_0a, dfs1_CB_0b)

## BGR ITP datasets, by time period
# ds_BGR_ITPs_all = ahf.Data_Set(BGR_ITPs_all, dfs1)
# ds_BGR_ITPs_0a = ahf.Data_Set(BGR_ITPs_0a, dfs1)
# ds_BGR_ITPs_0b = ahf.Data_Set(BGR_ITPs_0b, dfs1)
# ds_BGR_ITPs_0c = ahf.Data_Set(BGR_ITPs_0c, dfs1)
# ds_BGR_ITPs_0d = ahf.Data_Set(BGR_ITPs_0d, dfs1_BGR_0d)
# ds_BGR_ITPs_0e = ahf.Data_Set(BGR_ITPs_0e, dfs1_BGR_0e)
# ds_BGR_ITPs_0f = ahf.Data_Set(BGR_ITPs_0f, dfs1_BGR_0f)
# ds_BGR_ITPs_0g = ahf.Data_Set(BGR_ITPs_0g, dfs1_BGR_0g)
# ds_BGR_ITPs_0h = ahf.Data_Set(BGR_ITPs_0h, dfs1_BGR_0h)
# ds_BGR_ITPs_0i = ahf.Data_Set(BGR_ITPs_0i, dfs1_BGR_0i)
# ds_BGR_ITPs_0j = ahf.Data_Set(BGR_ITPs_0j, dfs1_BGR_0j)
# ds_BGR_ITPs_0k = ahf.Data_Set(BGR_ITPs_0k, dfs1_BGR_0k)
# ds_BGR_ITPs_0l = ahf.Data_Set(BGR_ITPs_0l, dfs1_BGR_0l)
# ds_BGR_ITPs_0m = ahf.Data_Set(BGR_ITPs_0m, dfs1_BGR_0m)
# ds_BGR_ITPs_0n = ahf.Data_Set(BGR_ITPs_0n, dfs1_BGR_0n)
# ds_BGR_ITPs_0o = ahf.Data_Set(BGR_ITPs_0o, dfs1_BGR_0o)
# ds_BGR_ITPs_0p = ahf.Data_Set(BGR_ITPs_0p, dfs1_BGR_0p)
# ds_BGR_ITPs_0q = ahf.Data_Set(BGR_ITPs_0q, dfs1_BGR_0q)
# ds_BGR_ITPs_0r = ahf.Data_Set(BGR_ITPs_0r, dfs1_BGR_0r)

# by different time periods
# ds_BGR04   = ahf.Data_Set(BGRITPs04, dfs1)
# ds_BGR0506 = ahf.Data_Set(BGRITPs0506, dfs1_BGR0506)
# ds_BGR0607 = ahf.Data_Set(BGRITPs0607, dfs1_BGR0607)
# ds_BGR0708 = ahf.Data_Set(BGRITPs0708, dfs1_BGR0708)
# ds_BGR0809 = ahf.Data_Set(BGRITPs0809, dfs1_BGR0809)
# ds_BGR0910 = ahf.Data_Set(BGRITPs0910, dfs1_BGR0910)
# ds_BGR1011 = ahf.Data_Set(BGRITPs1011, dfs1_BGR1011)
# ds_BGR1112 = ahf.Data_Set(BGRITPs1112, dfs1_BGR1112)
# ds_BGR1213 = ahf.Data_Set(BGRITPs1213, dfs1_BGR1213)
# ds_BGR1314 = ahf.Data_Set(BGRITPs1314, dfs1_BGR1314)
# ds_BGR1415 = ahf.Data_Set(BGRITPs1415, dfs1_BGR1415)
# ds_BGR1516 = ahf.Data_Set(BGRITPs1516, dfs1_BGR1516)
# ds_BGR1617 = ahf.Data_Set(BGRITPs1617, dfs1_BGR1617)
# ds_BGR1718 = ahf.Data_Set(BGRITPs1718, dfs1_BGR1718)
# ds_BGR1819 = ahf.Data_Set(BGRITPs1819, dfs1_BGR1819)
# ds_BGR1920 = ahf.Data_Set(BGRITPs1920, dfs1_BGR1920)
# ds_BGR2021 = ahf.Data_Set(BGRITPs2021, dfs1_BGR2021)
# ds_BGR2122 = ahf.Data_Set(BGRITPs2122, dfs1_BGR2122)

# ds_this_BGR = ahf.Data_Set(BGRITPs0506, dfs1_BGR0506)
ds_this_BGR = ahf.Data_Set(BGRITPs0511, dfs1_BGR0511)

# ds_this_BGR = ahf.Data_Set(BGRITPsAll, dfs1)

# Data Sets without filtering based on CT_max
# ds_ITP22_all  = ahf.Data_Set(ITP22_all, dfs_all)
# ds_ITP23_all  = ahf.Data_Set(ITP23_all, dfs_all)
# ds_ITP32_all  = ahf.Data_Set(ITP32_all, dfs_all)
# ds_ITP33_all  = ahf.Data_Set(ITP33_all, dfs_all)
# ds_ITP34_all  = ahf.Data_Set(ITP34_all, dfs_all)
# ds_ITP35_all  = ahf.Data_Set(ITP35_all, dfs_all)
# ds_ITP41_all  = ahf.Data_Set(ITP41_all, dfs_all)
# ds_ITP42_all  = ahf.Data_Set(ITP42_all, dfs_all)
# ds_ITP43_all  = ahf.Data_Set(ITP43_all, dfs_all)

# Data Sets filtered based on CT_max
# ds_ITP2 = ahf.Data_Set(ITP2_all, dfs0)

# ds_ITP33 = ahf.Data_Set(ITP33_all, dfs1)
# ds_ITP34 = ahf.Data_Set(ITP34_all, dfs1)
# ds_ITP35 = ahf.Data_Set(ITP35_all, dfs1)
# ds_ITP41 = ahf.Data_Set(ITP41_all, dfs1)
# ds_ITP42 = ahf.Data_Set(ITP42_all, dfs1)
# ds_ITP43 = ahf.Data_Set(ITP43_all, dfs1)
# 
# ds_ITP35_some_pfs0 = ahf.Data_Set(ITP35_pfs0, dfs0)
# ds_ITP35_some_pfs1 = ahf.Data_Set(ITP35_pfs1, dfs0)
# ds_ITP35_some_pfs2 = ahf.Data_Set(ITP35_pfs2, dfs0)

## Pre-clustered
dfs_to_use = dfs_all
# dfs_to_use = dfs1_q
# dfs_to_use = dfs_clstr_lbl
# Single time periods
# ds_BGRa_m110 = ahf.Data_Set(BGRa_m110, dfs_to_use)
# ds_BGRb_m380 = ahf.Data_Set(BGRb_m380, dfs_to_use)
# ds_BGRf_m310 = ahf.Data_Set(BGRf_m310, dfs_to_use)
# ds_BGRm_m410 = ahf.Data_Set(BGRm_m410, dfs_to_use)
# ds_BGRn_m240 = ahf.Data_Set(BGRn_m240, dfs_clstr_lbl1)# dfs_to_use)
# ds_BGRo_m390 = ahf.Data_Set(BGRo_m390, dfs_to_use)
# ds_ITP3t = ahf.Data_Set(ITP3t, dfs_to_use)
# By year
# ds_BGR04   = ahf.Data_Set(BGR04, dfs_to_use)
# ds_BGR0506 = ahf.Data_Set(BGR0506, dfs_to_use)
# ds_BGR0607 = ahf.Data_Set(BGR0607, dfs_to_use)
# ds_BGR0708 = ahf.Data_Set(BGR0708, dfs_to_use)
# ds_BGR0809 = ahf.Data_Set(BGR0809, dfs_to_use)
# ds_BGR0910 = ahf.Data_Set(BGR0910, dfs_to_use)
# ds_BGR1011 = ahf.Data_Set(BGR1011, dfs_to_use)

# ds_this_BGR = ahf.Data_Set(BGR0506, dfs_to_use)


# ds_BGR04_clstrs_456 = ahf.Data_Set(BGR04_clstrs_456, dfs_to_use)
# ds_BGR0508 = ahf.Data_Set(BGR0508, dfs_to_use)
# ds_BGR050607 = ahf.Data_Set(BGR050607, dfs_to_use)
# ds_BGR05060708 = ahf.Data_Set(BGR05060708, dfs_to_use)
# ds_BGR05060708_no_noise = ahf.Data_Set(BGR05060708, dfs_no_noise)
# ds_BGR05060708_clstrs_456 = ahf.Data_Set(BGR05060708_clstrs_456, dfs_all)
# ds_BGR_all = ahf.Data_Set(BGR_all, dfs_to_use)

# ds_this_BGR = ahf.Data_Set(BGR_all, dfs_to_use)

# Comparing time periods
# ds_BGRmn = ahf.Data_Set(BGRmn, dfs_to_use)
# ds_BGRno = ahf.Data_Set(BGRno, dfs_to_use)
# ds_BGRmno = ahf.Data_Set(BGRmno, dfs_to_use)
# ds_BGRmno_no_noise = ahf.Data_Set(BGRmno, dfs_no_noise)

################################################################################
# Create profile filtering objects
print('- Creating profile filtering objects')
################################################################################

pfs_0 = ahf.Profile_Filters()
pfs_1 = ahf.Profile_Filters(SA_range=[34.4,34.8])#ITP2_S_range)
pfs_2 = ahf.Profile_Filters(p_range=[400,200])

# # AIDJEX Operation Area (AOA)
# lon_AOA = [-152.9,-133.7]
# lat_AOA = [72.6,77.4]
# pfs_AOA = ahf.Profile_Filters(lon_range=lon_AOA,lat_range=lat_AOA)
# pfs_AOA1 = ahf.Profile_Filters(lon_range=lon_AOA,lat_range=lat_AOA, p_range=[1000,5])
# Canada Basin (CB), see Peralta-Ferriz2015
lon_CB = [-155,-130]
lat_CB = [72,84]
pfs_CB = ahf.Profile_Filters(lon_range=lon_CB,lat_range=lat_CB)
pfs_CB1 = ahf.Profile_Filters(lon_range=lon_CB,lat_range=lat_CB, p_range=[1000,5])
# Beaufort Gyre Region (BGR), see Shibley2022
lon_BGR = [-160,-130]
lat_BGR = [73,81.5]
pfs_BGR = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR)
pfs_BGR1 = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR, p_range=[1000,5], SA_range=test_S_range, lt_pCT_max=True)
pfs_BGR1_n = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR, p_range=[1000,5], SA_range=test_S_range, lt_pCT_max=True, every_nth_row=12)

pfs_BGR_test = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR, p_range=[1000,5], SA_range=test_S_range, lt_pCT_max=True)

pfs_test = ahf.Profile_Filters(every_nth_row=4)

# Profile filters
test_p_range = [400,200]
pfs_ell_10  = ahf.Profile_Filters(p_range=test_p_range, m_avg_win=10)
pfs_ell_50  = ahf.Profile_Filters(p_range=test_p_range, m_avg_win=50)
pfs_ell_100 = ahf.Profile_Filters(p_range=test_p_range, m_avg_win=100)
pfs_ell_150 = ahf.Profile_Filters(p_range=test_p_range, m_avg_win=150)

# Finding coincident profiles
# lon_coin = [-148.9,-147.8]
# lat_coin = [74.9,75.5]
# pfs_coin = ahf.Profile_Filters(lon_range=lon_coin,lat_range=lat_coin)
# pfs_coin_fltrd = ahf.Profile_Filters(lon_range=lon_coin,lat_range=lat_coin, SA_range=LHW_S_range, lt_pCT_max=True)

# Finding close example profiles
# lon_ex_pfs = [-145.2,-144.53]
# lat_ex_pfs = [75.962,76.06]
# pfs_ex_pfs = ahf.Profile_Filters(lon_range=lon_ex_pfs, lat_range=lat_ex_pfs)
# pfs_ex_pfs_fltrd = ahf.Profile_Filters(lon_range=lon_ex_pfs, lat_range=lat_ex_pfs, SA_range=LHW_S_range, lt_pCT_max=True)
# 
# pfs_ITP2  = ahf.Profile_Filters(SA_range=ITP2_S_range)
# pfs_ITP3  = ahf.Profile_Filters(SA_range=Lu2022_S_range)
# pfs_BGOS  = ahf.Profile_Filters(lon_range=lon_AOA,lat_range=lat_AOA,SA_range=BGOS_S_range)
# pfs_fltrd = ahf.Profile_Filters(lon_range=lon_AOA, lat_range=lat_AOA, SA_range=LHW_S_range, lt_pCT_max=True)
# pfs_fltrd_ss = ahf.Profile_Filters(lon_range=lon_AOA, lat_range=lat_AOA, SA_range=LHW_S_range, lt_pCT_max=True, subsample=True)
# pfs_fltrd = ahf.Profile_Filters(SA_range=LHW_S_range)#, lt_pCT_max=True)
# 
# pfs_subs = ahf.Profile_Filters(SA_range=ITP2_S_range, subsample=True)
# pfs_regrid = ahf.Profile_Filters(SA_range=ITP2_S_range, regrid_TS=['CT',0.01,'SP',0.005])
# pfs_ss_rg = ahf.Profile_Filters(SA_range=ITP2_S_range, subsample=True, regrid_TS=['CT',0.01,'SP',0.005])
# 
# pfs_AIDJEX = ahf.Profile_Filters(SA_range=AIDJEX_S_range)

################################################################################
# Create plotting parameter objects

# print('- Creating plotting parameter objects')
################################################################################

# Use these things
pfs_this_BGR = pfs_0
# pfs_this_BGR = pfs_BGR1
# pfs_this_BGR = pfs_BGR_test
# pfs_this_BGR = pfs_BGR1_n
# pfs_this_BGR = pfs_test

# ds_this_BGR = ds_ITP2
# ds_this_BGR = ds_ITP3
# ds_this_BGR = ds_BGR_ITPs_all
# ds_this_BGR = ds_BGR_ITPs_0a
# ds_this_BGR = ds_BGR_ITPs_0b
# ds_this_BGR = ds_BGR_ITPs_0c
# ds_this_BGR = ds_BGR_ITPs_0d
# ds_this_BGR = ds_BGR_ITPs_0e
# ds_this_BGR = ds_BGR_ITPs_0f
# ds_this_BGR = ds_BGR_ITPs_0g
# ds_this_BGR = ds_BGR_ITPs_0h
# ds_this_BGR = ds_BGR_ITPs_0i
# ds_this_BGR = ds_BGR_ITPs_0j
# ds_this_BGR = ds_BGR_ITPs_0k
# ds_this_BGR = ds_BGR_ITPs_0l
# ds_this_BGR = ds_BGR_ITPs_0m
# ds_this_BGR = ds_BGR_ITPs_0n
# ds_this_BGR = ds_BGR_ITPs_0o
# ds_this_BGR = ds_BGR_ITPs_0p
# ds_this_BGR = ds_BGR_ITPs_0q
# ds_this_BGR = ds_BGR_ITPs_0r

# by year
# ds_this_BGR = ds_BGR04
# ds_this_BGR = ds_BGR04_clstrs_456
# ds_this_BGR = ds_BGR0506
# ds_this_BGR = ds_BGR0607
# ds_this_BGR = ds_BGR0708
# ds_this_BGR = ds_BGR_all
# ds_this_BGR = ds_BGR0508
# ds_this_BGR = ds_BGR050607
# ds_this_BGR = ds_BGR05060708
# ds_this_BGR = ds_BGR05060708_clstrs_456

################################################################################
################################################################################
### Figures
################################################################################
################################################################################

################################################################################
## Basic TS plots
################################################################################
# TS plot
if False:
    print('')
    print('- Creating TS plot')
    # Make the Plot Parameters
    pp_TS = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='clr_all_same')
    # Make the Analysis Group
    group_TS_plot = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_TS)
    # Make the figure
    ahf.make_figure([group_TS_plot])

## TS plot by instrument
if False:
    print('')
    print('- Creating TS plot, colored by instrument')
    # Make the Plot Parameters
    pp_TS_instrmt = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['CT'], clr_map='instrmt')
    # Make the Analysis Group pfs_fltrd pfs_AOA1
    group_TS_plot = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_TS_instrmt)
    # Make the figure
    ahf.make_figure([group_TS_plot])

################################################################################
## Overviews
################################################################################
# ITP number vs time
if False:
    print('')
    print('- Creating plot of ITP number vs time')
    # Make the Plot Parameters
    pp_ITP_vs_time = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['instrmt'], clr_map='instrmt', legend=False)
    # Make the Analysis Group
    group_ITP_vs_time = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_ITP_vs_time)
    # Make the figure
    ahf.make_figure([group_ITP_vs_time])

# Output summary
if False:
    # Make the Plot Parameters
    pp_test = ahf.Plot_Parameters(extra_args={'extra_vars_to_keep':['dt_start']})
    # Make the Analysis Group
    group_test = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_test)
    ahf.txt_summary([group_test])

# Cluster stats
if False:
    # Make the Plot Parameters
    pp_test = ahf.Plot_Parameters(extra_args={'extra_vars_to_keep':['SA','cluster']})
    # Make the Analysis Group
    group_test = ahf.Analysis_Group(ds_BGRmn, pfs_0, pp_test)
    ahf.cluster_stats([group_test], stat_vars=['SA'])

################################################################################
## Maps and distances
################################################################################
pp_map = ahf.Plot_Parameters(plot_type='map', clr_map='instrmt', extra_args={'map_extent':'Western_Arctic'})
pp_map_full_Arctic = ahf.Plot_Parameters(plot_type='map', clr_map='instrmt', extra_args={'map_extent':'Full_Arctic'})#, legend=False, add_grid=False)
pp_map_by_date = ahf.Plot_Parameters(plot_type='map', clr_map='dt_start', extra_args={'map_extent':'Western_Arctic'})
## Map of all profiles for all sources
if False:
    print('')
    print('- Creating a map of all profiles from all sources')
    # Make the subplot groups
    group_map_full_Arctic = ahf.Analysis_Group(ds_all_ITP, pfs_0, pp_map_full_Arctic, plot_title='')
    group_map = ahf.Analysis_Group(ds_all_ITP, pfs_0, pp_map, plot_title='')
    # Make the figure
    ahf.make_figure([group_map_full_Arctic, group_map], use_same_x_axis=False, use_same_y_axis=False, filename='Figure_1.pickle')
## Map of just in the Beaufort Gyre Region
if False:
    print('')
    print('- Creating a map of profiles in the Beaufort Gyre Region')
    # Make the subplot groups
    group_map = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_map, plot_title='')
    # Make the figure
    ahf.make_figure([group_map], use_same_x_axis=False, use_same_y_axis=False)#, filename='Figure_1.pickle')
## Map of all upgoing profiles for all sources
if False:
    print('')
    print('- Creating a map of all upgoing profiles from all sources')
    # Make the subplot groups
    group_map_full_Arctic = ahf.Analysis_Group(ds_all_sources_up, pfs_0, pp_map_full_Arctic, plot_title='')
    group_map = ahf.Analysis_Group(ds_all_sources_up, pfs_0, pp_map, plot_title='')
    # Make the figure
    ahf.make_figure([group_map_full_Arctic, group_map], use_same_x_axis=False, use_same_y_axis=False)#, filename='Figure_1.pickle')
## Map of all upgoing profiles for all sources with a max pressure > 400 dbar
if False:
    print('')
    print('- Creating a map of all upgoing profiles from all sources that go below 400 dbar')
    # Make the subplot groups
    group_map_full_Arctic = ahf.Analysis_Group(ds_all_sources_pmin, pfs_0, pp_map_full_Arctic, plot_title='')
    group_map = ahf.Analysis_Group(ds_all_sources_pmin, pfs_0, pp_map, plot_title='')
    # Make the figure
    ahf.make_figure([group_map_full_Arctic, group_map], use_same_x_axis=False, use_same_y_axis=False)#, filename='Figure_1.pickle') 
### Date and Distance spans
## Map of all BGR profiles
if False:
    print('')
    print('- Creating map all BGR profiles')
    # Make the subplot groups
    group_BGR_map_by_date = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_map_by_date)
    # Make the figure
    ahf.make_figure([group_BGR_map_by_date], use_same_x_axis=False, use_same_y_axis=False)
    # Find the maximum distance between any two profiles for each data set in the group
    # ahf.find_max_distance([group_BGR_map_by_date])

################################################################################
## Isopycnal tracking
################################################################################
# For these plots, I'm specifically not using a pre-clustered file so that I can
#   use all the points (including noise) to track isopycnals

# Plotting density on a pressure vs. time plot
if True:
    print('')
    print('- Creating test plots of sigma')
    lat_lon_groups_to_plot = []
    hist_groups_to_plot = []
    press_vs_time_uncorr = []
    press_vs_time_corrtd = []
    sig_ranges = [[32.3325, 32.33], [32.335, 32.33], [32.34, 32.33]]
    for this_sig_range in sig_ranges:
        that_title = r'$\sigma_1=[$'+str(min(this_sig_range))+r', '+str(max(this_sig_range))+r'$]$'
        # Make profile filters
        pfs_sigma_test = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR, p_range=[1000,5], SA_range=test_S_range, lt_pCT_max=True, sig_range=this_sig_range)
        # Make the Plot Parameters
        pp_lat_lon_sigma = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='press', legend=True, extra_args={'plot_slopes':True, 'extra_vars_to_keep':['sigma']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR})
        pp_sigma_hist = ahf.Plot_Parameters(x_vars=['hist'], y_vars=['press'], legend=True, extra_args={'plot_slopes':False, 'extra_vars_to_keep':['sigma']})
        pp_p_v_lat = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['press'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['sigma']})
        pp_minus_fit = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['press-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['sigma'], 'fit_vars':['lon','lat']})
        # Make the subplot groups
        # lat_lon_groups_to_plot.append(ahf.Analysis_Group(ds_this_BGR, pfs_sigma_test, pp_lat_lon_sigma, plot_title=that_title))
        # hist_groups_to_plot.append(ahf.Analysis_Group(ds_this_BGR, pfs_sigma_test, pp_sigma_hist, plot_title=that_title))
        press_vs_time_uncorr.append(ahf.Analysis_Group(ds_this_BGR, pfs_sigma_test, pp_p_v_lat, plot_title=r'Uncorrected '+that_title))
        press_vs_time_corrtd.append(ahf.Analysis_Group(ds_this_BGR, pfs_sigma_test, pp_minus_fit, plot_title=r'Corrected '+that_title))
    # Make the figure
    # ahf.make_figure(lat_lon_groups_to_plot + hist_groups_to_plot)
    ahf.make_figure(press_vs_time_uncorr + press_vs_time_corrtd)

################################################################################
## Density ratio plots
################################################################################
# Map and histogram of vertical density ratio per profile NOT WORKING CURRENTLY
if False:
    print('')
    print('- Creating map of vertical density ratio')
    # Make the Plot Parameters
    pp_map_R_rho = ahf.Plot_Parameters(plot_type='map', clr_map='R_rho', ax_lims={'c_lims':[0,10]}, extra_args={'map_extent':'Western_Arctic'})
    pp_hist_R_rho = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['R_rho'], y_vars=['hist'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA']})
    # Make the subplot groups
    # group_map_R_rho = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_map_R_rho)
    group_hist_R_rho = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_hist_R_rho)
    # Make the figure
    # ahf.make_figure([group_map_R_rho, group_hist_R_rho])
    ahf.make_figure([group_hist_R_rho])

################################################################################
## Basic plots
################################################################################
# TS 
if False:
    print('')
    print('- Creating TS plot')
    # Make the Plot Parameters
    pp_TS = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['CT'], clr_map='press', ax_lims={'c_lims':[180,240]})
    # Make the subplot groups
    group_TS = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_TS)
    # Make the figure
    ahf.make_figure([group_TS])

# SA vs time
if False:
    print('')
    print('- Creating TS plot')
    # Make the Plot Parameters
    pp_SA_vs_time = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['SA'], clr_map='instrmt')
    # Make the subplot groups
    group_SA_vs_time = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_SA_vs_time)
    # Make the figure
    ahf.make_figure([group_SA_vs_time], row_col_list=[1,1, 0.27, 1.0])
# TS and map
if False:
    print('')
    print('- Creating TS plot')
    # Make the Plot Parameters
    pp_TS = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='clr_all_same')
    # Make the subplot groups
    group_TS = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_TS)
    group_map = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_map)
    # Make the figure
    ahf.make_figure([group_TS, group_map], row_col_list=[1,2, 0.31, 1.1])

################################################################################
## Filter effects
################################################################################
# Profiles filtered out by p_max > 400 dbar
if False:
    print('')
    print('- Creating figure for profiles eliminated by p_max > 400 dbar filter')
    # Make the data set
    # ds_pmax_lt_400 = ahf.Data_Set(pmax_lt_400_ITP_35, dfs_all) # So many profiles
    ds_pmax_lt_400 = ahf.Data_Set(pmax_lt_400_ITP_41, dfs_all) # A lot of profiles
    # ds_pmax_lt_400 = ahf.Data_Set(pmax_lt_400_ITP_42, dfs_all) # A few profiles
    # Make the Plot Parameters
    # pp_pmax_lt_400 = ahf.Plot_Parameters(x_vars=['SA','CT'], y_vars=['press'], plot_type='profiles')
    pp_pmax_lt_400 = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['CT'], clr_map='press')
    # Make the Analysis Group
    group_pmax_lt_400 = ahf.Analysis_Group(ds_pmax_lt_400, pfs_0, pp_pmax_lt_400, plot_title=r'Profiles with $p_{max} < 400$ dbar')
    # Make the figure
    ahf.make_figure([group_pmax_lt_400])
## Histograms of pressure max
if False:
    print('')
    print('- Creating histograms of pressure max in each profile')
    # Define the Profile Filters
    pfs_BGR1_all = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR, p_range=[1000,5])#, SA_range=test_S_range, lt_pCT_max=False)
    # Make the Plot Parameters
    pp_max_press_hist = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['max_press'], y_vars=['hist'], clr_map='clr_all_same')
    # Make the subplot groups
    group_all_pfs    = ahf.Analysis_Group(ds_ITP3, pfs_BGR1_all, pp_max_press_hist, plot_title=r'All profiles')
    group_lt_pCT_max = ahf.Analysis_Group(ds_ITP3, pfs_BGR1, pp_max_press_hist, plot_title=r'Profiles with $p < p(\Theta_{max})$')
    # Make the figure
    ahf.make_figure([group_all_pfs, group_lt_pCT_max])
    # ahf.make_figure([group_lt_pCT_max])
## Histograms of CT_max data
if False:
    print('')
    print('- Creating histograms of pressure at temperature max in each profile')
    # Make the Plot Parameters
    pp_press_CT_max_hist = ahf.Plot_Parameters(x_vars=['press_CT_max'], y_vars=['hist'], clr_map='clr_all_same')
    # Make the subplot groups
    group_press_CT_max_hist = ahf.Analysis_Group(ds_ITP3, pfs_0, pp_press_CT_max_hist)
    # # Make the figure
    ahf.make_figure([group_press_CT_max_hist])
## Plots of SA_CT_max vs press_CT_max
if False:
    print('')
    print('- Creating plots of the info about CT_max')
    # Make the Plot Parameters
    pp_SA_CT_max = ahf.Plot_Parameters(x_vars=['SA_CT_max'], y_vars=['press_CT_max'], clr_map='CT_max')
    # Make the subplot groups
    group_SA_CT_max = ahf.Analysis_Group(ds_ITP3, pfs_0, pp_SA_CT_max)
    # # Make the figure
    ahf.make_figure([group_SA_CT_max])

################################################################################
## Plots in la_CT vs. SA space with different values of ell
################################################################################
# BGR
if False:
    print('')
    print('- Creating plots in la_CT--SA space with different values of ell')
    # Select the dataset to use
    this_ds = ds_this_BGR
    # Make the profile filter objects for the different values of ell
    pfs_ell_010 = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR, p_range=[1000,5], SA_range=test_S_range, lt_pCT_max=True, m_avg_win=10)
    pfs_ell_050 = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR, p_range=[1000,5], SA_range=test_S_range, lt_pCT_max=True, m_avg_win=50)
    pfs_ell_100 = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR, p_range=[1000,5], SA_range=test_S_range, lt_pCT_max=True, m_avg_win=100)
    pfs_ell_150 = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR, p_range=[1000,5], SA_range=test_S_range, lt_pCT_max=True, m_avg_win=150)
    # Make the Plot Parameters
    pp_TS = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='clr_all_same')
    # Make the subplot groups
    group_test1 = ahf.Analysis_Group(this_ds, pfs_ell_010, pp_TS, plot_title=r'ell = 10')
    group_test2 = ahf.Analysis_Group(this_ds, pfs_ell_050, pp_TS, plot_title=r'ell = 50')
    group_test3 = ahf.Analysis_Group(this_ds, pfs_ell_100, pp_TS, plot_title=r'ell = 100')
    group_test4 = ahf.Analysis_Group(this_ds, pfs_ell_150, pp_TS, plot_title=r'ell = 150')
    # # Make the figure
    ahf.make_figure([group_test1, group_test2, group_test3, group_test4], use_same_y_axis=True)
# ITP2 (NOTE: using SP instead of SA)
if False:
    print('')
    print('- Creating plots in la_CT--SA space with different values of ell')
    # Select the dataset to use
    this_ds = ds_ITP2
    # Make the profile filter objects for the different values of ell
    pfs_ell_010 = ahf.Profile_Filters(p_range=[1000,5], SP_range=ITP2_S_range, m_avg_win=10)
    pfs_ell_050 = ahf.Profile_Filters(p_range=[1000,5], SP_range=ITP2_S_range, m_avg_win=50)
    pfs_ell_100 = ahf.Profile_Filters(p_range=[1000,5], SP_range=ITP2_S_range, m_avg_win=100)
    pfs_ell_150 = ahf.Profile_Filters(p_range=[1000,5], SP_range=ITP2_S_range, m_avg_win=150)
    # Make the Plot Parameters
    pp_TS = ahf.Plot_Parameters(x_vars=['SP'], y_vars=['la_CT'], clr_map='clr_all_same')
    # Make the subplot groups
    group_1 = ahf.Analysis_Group(this_ds, pfs_ell_010, pp_TS, plot_title=r'ITP2 $\ell=10$ dbar')
    group_2 = ahf.Analysis_Group(this_ds, pfs_ell_050, pp_TS, plot_title=r'ITP2 $\ell=50$ dbar')
    group_3 = ahf.Analysis_Group(this_ds, pfs_ell_100, pp_TS, plot_title=r'ITP2 $\ell=100$ dbar')
    group_4 = ahf.Analysis_Group(this_ds, pfs_ell_150, pp_TS, plot_title=r'ITP2 $\ell=150$ dbar')
    # # Make the figure
    ahf.make_figure([group_1, group_2, group_3, group_4])
# ITP2, clustered (NOTE: using SP instead of SA)
if False:
    print('')
    print('- Creating clustered plots in la_CT--SA space with different values of ell')
    # Select the dataset to use
    this_ds = ds_ITP2
    # Make the profile filter objects for the different values of ell
    pfs_ell_010 = ahf.Profile_Filters(p_range=[1000,5], SP_range=ITP2_S_range, m_avg_win=10)
    pfs_ell_050 = ahf.Profile_Filters(p_range=[1000,5], SP_range=ITP2_S_range, m_avg_win=50)
    pfs_ell_100 = ahf.Profile_Filters(p_range=[1000,5], SP_range=ITP2_S_range, m_avg_win=100)
    pfs_ell_150 = ahf.Profile_Filters(p_range=[1000,5], SP_range=ITP2_S_range, m_avg_win=150)
    # Make the Plot Parameters
    #   Note: values of m_pts determined from parameter sweep, see Figure S.4
    pp_ell_010 = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':230, 'b_a_w_plt':False, 'extra_vars_to_keep':['press']}, legend=True)
    pp_ell_050 = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':200, 'b_a_w_plt':False, 'extra_vars_to_keep':['press']}, legend=True)
    pp_ell_100 = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':170, 'b_a_w_plt':False, 'sort_clstrs':False, 'extra_vars_to_keep':['press']}, legend=True)
    pp_ell_150 = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':140, 'b_a_w_plt':False, 'extra_vars_to_keep':['press']}, legend=True)
    # Make the Analysis Groups
    group_ell_010 = ahf.Analysis_Group(this_ds, pfs_ell_010, pp_ell_010, plot_title=r'ITP2 $\ell=10$ dbar')
    group_ell_050 = ahf.Analysis_Group(this_ds, pfs_ell_050, pp_ell_050, plot_title=r'ITP2 $\ell=50$ dbar')
    group_ell_100 = ahf.Analysis_Group(this_ds, pfs_ell_100, pp_ell_100, plot_title=r'ITP2 $\ell=100$ dbar')
    group_ell_150 = ahf.Analysis_Group(this_ds, pfs_ell_150, pp_ell_150, plot_title=r'ITP2 $\ell=150$ dbar')
    # Make the figure
    ahf.make_figure([group_ell_010, group_ell_050, group_ell_100, group_ell_150])

################################################################################
## Example profile plots
################################################################################
# Example profile plots, CT and SA, full and zoomed
if False:
    print('')
    print('- Creating figure of an example profile')
    # Make the data set
    ds_ITP_ex_pfs = ahf.Data_Set(ex_pfs2, dfs_all)
    # Make the Plot Parameters
    pp_pfs_full = ahf.Plot_Parameters(x_vars=['CT','SA'], y_vars=['press'], plot_type='profiles', extra_args={'plot_pts':False}, legend=False)
    pp_pfs_zoom = ahf.Plot_Parameters(x_vars=['SA','CT'], y_vars=['press'], plot_type='profiles', extra_args={'plot_pts':False})#, ax_lims={'y_lims':ex_pfs1_zoom_range})
    # Make the Analysis Groups
    group_example_profiles1 = ahf.Analysis_Group(ds_ITP_ex_pfs, pfs_0, pp_pfs_full, plot_title='')
    group_example_profiles2 = ahf.Analysis_Group(ds_ITP_ex_pfs, pfs_BGR_test, pp_pfs_zoom, plot_title='')
    # Make the figure
    ahf.make_figure([group_example_profiles1, group_example_profiles2], use_same_y_axis=False, row_col_list=[2,1, 0.45, 1.4])
# Example profile plot, iT and SP, full and zoomed
if False:
    print('')
    print('- Creating figure of an example profile')
    # Make the data set
    ds_ITP_ex_pfs = ahf.Data_Set(ex_pfs1, dfs_all)
    # Make the Plot Parameters
    pp_pfs_full = ahf.Plot_Parameters(x_vars=['iT','SP'], y_vars=['press'], plot_type='profiles', extra_args={'shift_pfs':True})
    pp_pfs_zoom = ahf.Plot_Parameters(x_vars=['iT','SP'], y_vars=['press'], plot_type='profiles', ax_lims={'y_lims':ex_pfs1_zoom_range})
    # Make the Analysis Groups
    group_example_profiles1 = ahf.Analysis_Group(ds_ITP_ex_pfs, pfs_0, pp_pfs_full, plot_title='')
    group_example_profiles2 = ahf.Analysis_Group(ds_ITP_ex_pfs, pfs_0, pp_pfs_zoom, plot_title='')
    # Make the figure
    ahf.make_figure([group_example_profiles1, group_example_profiles2], use_same_y_axis=False)
# Clustering a single example profile plot
if False:
    print('')
    print('- Creating figure of an example profile')
    # Make the data set
    ds_ITP_ex_pfs = ahf.Data_Set(ex_pfs1, dfs_all)
    # Make the Plot Parameters
    zoom_range = [260,220]
    this_m_pts = 4
    pp_pfs_clstr = ahf.Plot_Parameters(x_vars=['CT'], y_vars=['SA'], clr_map='cluster', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':this_m_pts, 'b_a_w_plt':False, 'plot_centroid':False})
    pp_pfs_zoomed = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['press'], plot_type='profiles', clr_map='cluster', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':this_m_pts, 'b_a_w_plt':False, 'plot_centroid':False})#, ax_lims={'y_lims':zoom_range}, add_grid=False)
    # Make the Analysis Group
    this_ds = ds_ITP_ex_pfs
    group_example_profiles1 = ahf.Analysis_Group(this_ds, pfs_1, pp_pfs_clstr)#, plot_title='')
    group_example_profiles2 = ahf.Analysis_Group(this_ds, pfs_1, pp_pfs_zoomed)#, plot_title='')
    # Make the figure
    ahf.make_figure([group_example_profiles1, group_example_profiles2])
## Example profiles with clustering marked
if False:
    print('')
    print('- Creating figure of clustered example profiles')
    # Make the Plot Parameters
    pp_pfs_SA = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['press'], clr_map='cluster', plot_type='profiles', extra_args={'plot_pts':True, 'extra_vars_to_keep':['dt_start'], 'dts_to_plot':['2005-08-16 06:00:01', '2006-08-15 06:00:03', '2005-11-15 06:00:03', '2006-05-15 06:00:02', '2006-02-15 06:00:03']}, legend=False)
    pp_pfs_CT = ahf.Plot_Parameters(x_vars=['CT'], y_vars=['press'], clr_map='cluster', plot_type='profiles', extra_args={'plot_pts':True, 'extra_vars_to_keep':['dt_start'], 'dts_to_plot':['2005-08-16 06:00:01', '2006-08-15 06:00:03', '2005-11-15 06:00:03', '2006-05-15 06:00:02', '2006-02-15 06:00:03']}, legend=False)
    # Make the Analysis Groups
    group_ex_pfs_SA = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_pfs_SA, plot_title='')
    group_ex_pfs_CT = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_pfs_CT, plot_title='')
    # Make the figure
    ahf.make_figure([group_ex_pfs_SA, group_ex_pfs_CT], use_same_y_axis=False, row_col_list=[2,1, 0.45, 1.4])

################################################################################
## Waterfall plots
################################################################################
# ITP2 Example profiles waterfall plot
if False:
    print('')
    print('- Creating a waterfall figure of example profiles')
    # Define the Profile Filters
    pfs_2 = ahf.Profile_Filters(p_range=[600,200])
    # Make the data set
    ds_ITP_ex_pfs = ahf.Data_Set(ITP2_ex_pfs, dfs_all)
    # Make the Plot Parameters
    pp_pfs_full = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['press'], plot_type='waterfall', extra_args={'plot_pts':False}, legend=False)
    # Make the Analysis Groups pfs_BGR1 pfs_0
    group_example_profiles1 = ahf.Analysis_Group(ds_ITP_ex_pfs, pfs_2, pp_pfs_full)
    # Make the figure
    ahf.make_figure([group_example_profiles1])
# ITP2 Waterfall plot with cluster points colored
if False:
    print('')
    print('- Creating figure of an example profile')
    # Define the Profile Filters
    # pfs_2 = ahf.Profile_Filters(p_range=[220,210])
    # Make the data set
    ds_ex_pfs = ahf.Data_Set(BGR04_ex_pfs, dfs_all)
    # Make the Plot Parameters
    pp_pfs_full = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['press'], clr_map='cluster', plot_type='waterfall', legend=False, add_grid=False)
    # Make the Analysis Groups pfs_BGR1 pfs_0
    group_example_profiles1 = ahf.Analysis_Group(ds_ex_pfs, pfs_2, pp_pfs_full)
    # Make the figure
    ahf.make_figure([group_example_profiles1], row_col_list=[1,1, 0.8, 1.5])
# BGR Example profiles waterfall plot
if False:
    print('')
    print('- Creating a waterfall figure of example profiles')
    # Define the Profile Filters
    pfs_2 = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR, p_range=[410,210], lt_pCT_max=True)#, SA_range=test_S_range)
    # Make the data set
    # ds_ex_pfs2 = ahf.Data_Set(ex_pfs2, dfs_all)
    # Make the Plot Parameters
    pp_pfs_full = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['press-fit'], clr_map='cluster', plot_type='waterfall', extra_args={'plot_pts':True, 'extra_vars_to_keep':['dt_start'], 'dts_to_plot':[13011.250011574075, 13375.250034722223, 13102.250034722223, 13283.250023148148, 13194.250034722223, 13559.000104166667, 13740.00019675926, 13467.000023148148, 13648.000023148148, 14106.000034722223, 14379.016851851851, 14198.016863425926, 13832.016863425926, 14014.016863425926, 13924.016863425926, 14468.00008101852, 14290.00008101852, 14744.000069444444, 14836.000069444444, 14655.000069444444, 14563.00162037037, 15109.00008101852, 15200.000069444444, 15020.00008101852, 14928.00008101852], 'fit_vars':['lon','lat']}, legend=False)
    # pp_pfs_full = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['dt_start'], y_vars=['prof_no'], clr_map='instrmt', legend=True)
    # Make the Analysis Groups 
    group_example_profiles2 = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_pfs_full)
    # group_example_profiles2 = ahf.Analysis_Group(ds_ex_pfs2, pfs_2, pp_pfs_full)
    # Make the figure
    ahf.make_figure([group_example_profiles2])

    # # Make the data set
    # ds_ITP_ex_pfs = ahf.Data_Set(ex_pfs2, dfs_all)
    # # Make the Plot Parameters
    # pp_pfs_full = ahf.Plot_Parameters(x_vars=['CT','SA'], y_vars=['press'], plot_type='profiles', extra_args={'plot_pts':False}, legend=False)
    # pp_pfs_zoom = ahf.Plot_Parameters(x_vars=['SA','CT'], y_vars=['press'], plot_type='profiles', extra_args={'plot_pts':False})#, ax_lims={'y_lims':ex_pfs1_zoom_range})
    # pp_pfs_map  = ahf.Plot_Parameters(plot_type='map', clr_map='instrmt', extra_args={'map_extent':'Western_Arctic'})#, ax_lims={'y_lims':ex_pfs1_zoom_range})
    # # Make the Analysis Groups
    # group_example_profiles1 = ahf.Analysis_Group(ds_ITP_ex_pfs, pfs_0, pp_pfs_full, plot_title='')
    # group_example_profiles2 = ahf.Analysis_Group(ds_ITP_ex_pfs, pfs_BGR_test, pp_pfs_zoom, plot_title='')
    # group_example_profiles3 = ahf.Analysis_Group(ds_ITP_ex_pfs, pfs_BGR_test, pp_pfs_map, plot_title='')
    # # Make the figure
    # ahf.make_figure([group_example_profiles1, group_example_profiles2, group_example_profiles3], use_same_y_axis=False)

################################################################################
## Subsampling
################################################################################
## Subsampling ITP data
# Histograms of the first differences for data sets
if False:
    print('')
    print('- Creating histograms of first differences in pressures')
    # Make the Plot Parameters
    pp_first_dfs_press = ahf.Plot_Parameters(x_vars=['press'], y_vars=['hist'], clr_map='clr_all_same', first_dfs=[True,False])
    # Make the subplot groups
    group_first_dfs_press_hist = ahf.Analysis_Group(ds_ITP3, pfs_BGR1, pp_first_dfs_press)
    # # Make the figure
    ahf.make_figure([group_first_dfs_press_hist])#, use_same_x_axis=False, use_same_y_axis=False)
# Comparing ITP3 to ssITP3
if False:
    print('')
    print('- Creating TS plots to compare full profiles vs. subsampled')
    # Define the Profile Filters
    every_n = 12
    pfs_BGR1_n = ahf.Profile_Filters(lon_range=lon_BGR,lat_range=lat_BGR, p_range=[1000,5], SA_range=test_S_range, lt_pCT_max=True, every_nth_row=every_n)
    # Make the Plot Parameters
    m_pts1 = 'auto'#500
    m_pts2 = 'auto'#100
    these_pfs = [313,315,317,319,321]
    pp_TS1 = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['CT'], clr_map='cluster', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':m_pts1, 'b_a_w_plt':True, 'plot_centroid':True})
    pp_TS2 = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['CT'], clr_map='cluster', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':m_pts2, 'b_a_w_plt':True, 'plot_centroid':True})
    pp_pfs1 = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['press'], plot_type='profiles', ax_lims={'y_lims':[240,225]}, clr_map='cluster', extra_args={'pfs_to_plot':these_pfs, 'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':m_pts1, 'b_a_w_plt':False})
    pp_pfs2 = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['press'], plot_type='profiles', ax_lims={'y_lims':[240,225]}, clr_map='cluster', extra_args={'pfs_to_plot':these_pfs, 'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':m_pts2, 'b_a_w_plt':False})
    # Make the subplot groups
    group_ITP3_full = ahf.Analysis_Group(ds_ITP3, pfs_BGR1, pp_TS1, plot_title=r'ITP3 full')
    group_ITP3_ss = ahf.Analysis_Group(ds_ITP3, pfs_BGR1_n, pp_TS2, plot_title=r'ITP3 subsampled, every '+str(every_n))
    group_ITP3_full_pfs = ahf.Analysis_Group(ds_ITP3, pfs_BGR1, pp_pfs1, plot_title=r'ITP3 full')
    group_ITP3_ss_pfs = ahf.Analysis_Group(ds_ITP3, pfs_BGR1_n, pp_pfs2, plot_title=r'ITP3 subsampled, every '+str(every_n))
    # # Make the figure
    ahf.make_figure([group_ITP3_full, group_ITP3_ss, group_ITP3_full_pfs, group_ITP3_ss_pfs], use_same_x_axis=False)

################################################################################
## Clustering parameter sweeps
################################################################################
# Parameter sweep for BGR ITP data
if False:
    print('')
    print('- Creating clustering parameter sweep for BGR ITP data')
    test_mpts = 360
    # Make the Plot Parameters
    pp_mpts_param_sweep = ahf.Plot_Parameters(x_vars=['m_pts'], y_vars=['n_clusters','DBCV'], clr_map='clr_all_same', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':test_mpts, 'm_cls':1000, 'cl_ps_tuple':[10,110,10]}) #[10,721,10]
    # pp_ell_param_sweep  = ahf.Plot_Parameters(x_vars=['ell_size'], y_vars=['n_clusters','DBCV'], clr_map='clr_all_same', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':test_mpts, 'cl_ps_tuple':[10,271,10]}) 
    # Make the subplot groups
    group_mpts_param_sweep = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_mpts_param_sweep)#, plot_title='BGR04')
    # group_ell_param_sweep  = ahf.Analysis_Group(ds_BGOS, pfs_fltrd, pp_ell_param_sweep, plot_title='BGR04')
    # # Make the figure
    # ahf.make_figure([group_mpts_param_sweep, group_ell_param_sweep], filename='test_param_sweep_BGR.pickle')
    ahf.make_figure([group_mpts_param_sweep])#, filename='BGRa_ps.pickl')
## Parameter sweep for 4 different ell values
if False:
    print('')
    print('- Creating TS plots')
    # Make the Plot Parameters
    pp_mpts_ps = ahf.Plot_Parameters(x_vars=['m_pts'], y_vars=['n_clusters','DBCV'], clr_map='clr_all_same', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':100, 'cl_ps_tuple':[10,721,10]})
    # Make the Analysis Groups
    group_ell_010 = ahf.Analysis_Group(ds_ITP2, pfs_ell_10, pp_mpts_ps, plot_title=r'ITP2 $\ell=10$ dbar')
    group_ell_050 = ahf.Analysis_Group(ds_ITP2, pfs_ell_50, pp_mpts_ps, plot_title=r'ITP2 $\ell=50$ dbar')
    group_ell_100 = ahf.Analysis_Group(ds_ITP2, pfs_ell_100,pp_mpts_ps, plot_title=r'ITP2 $\ell=100$ dbar')
    group_ell_150 = ahf.Analysis_Group(ds_ITP2, pfs_ell_150,pp_mpts_ps, plot_title=r'ITP2 $\ell=150$ dbar')
    # Make the figure
    ahf.make_figure([group_ell_010, group_ell_050, group_ell_100, group_ell_150], filename='4_ell_value_ps.pickle')

################################################################################
## Test clustering (live)
################################################################################
# test clustering
if False:
    print('')
    print('- Creating clustering plot')
    # ds_this_BGR = ds_BGR05060708_no_noise
    # Make the Plot Parameters
    # pp_live_clstr = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':190, 'm_cls':'auto', 'b_a_w_plt':True, 'relab_these':{1:2, 2:3, 5:6}, 'extra_vars_to_keep':['CT', 'ma_CT']})
    pp_live_clstr = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'cl_x_var':'SA', 'cl_y_var':'la_CT', 'm_pts':'auto', 'm_cls':'auto', 'b_a_w_plt':True, 'extra_vars_to_keep':['CT', 'ma_CT']})
    # Make the subplot groups
    group_clstrd = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_live_clstr)
    # Make the figure
    ahf.make_figure([group_clstrd])#, filename='test_clstr.pickle')

################################################################################
################################################################################
## Plotting clusterings from pre-clustered files
################################################################################
################################################################################

################################################################################
## Pre-clustered la_CT vs. SA plots
################################################################################
# Make the Plot Parameters
pp_pre_clstrd = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'b_a_w_plt':True})
# relab_these_test = {2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:13,13:14}
relab_these_test = {}
# BGR ITP clustering
if False:
    print('')
    print('- Creating plot of pre-clustered BGR ITP data')
    # pp_pre_clstrd = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'sort_clstrs':False, 'b_a_w_plt':True, 'relab_these':relab_these_test}, ax_lims={'x_lims':test_S_range})
    pp_pre_clstrd = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'sort_clstrs':False, 'b_a_w_plt':True}, ax_lims={'x_lims':test_S_range})
    # Make the subplot groups
    group_pre_clstrd = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_pre_clstrd)
    # Plot the figure
    ahf.make_figure([group_pre_clstrd], use_same_y_axis=False)
# Multiple BGR ITP clustering
if False:
    print('')
    print('- Creating plots of pre-clustered BGR ITP data')
    pp_pre_clstrd = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'b_a_w_plt':True}, ax_lims={'x_lims':test_S_range}, legend=True)
    # Make the subplot groups
    # group_pre_clstrd_0 = ahf.Analysis_Group(ds_BGR04, pfs_0, pp_pre_clstrd)
    group_pre_clstrd_1 = ahf.Analysis_Group(ds_BGR0506, pfs_0, pp_pre_clstrd)
    group_pre_clstrd_2 = ahf.Analysis_Group(ds_BGR0607, pfs_0, pp_pre_clstrd)
    group_pre_clstrd_3 = ahf.Analysis_Group(ds_BGR0708, pfs_0, pp_pre_clstrd)
    # Plot the figure
    ahf.make_figure([group_pre_clstrd_1, group_pre_clstrd_2, group_pre_clstrd_3])

################################################################################
## Pre-clustered plots vs. time
################################################################################
# Salinity vs. time
if False:
    print('')
    print('- Creating plots of salinity vs time')
    # Make the Plot Parameters
    pp_SA_vs_dt = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['SA'], clr_map='cluster', extra_args={'plt_noise':True})
    # Make the subplot groups ds_BGOS_m280_e050 ds_BGOS
    group_SA_vs_dt = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_SA_vs_dt)
    # Make the figure
    ahf.make_figure([group_SA_vs_dt])
# Temperature vs. time and pressure vs. time
if False:
    print('')
    print('- Creating plots of temperature and pressure vs time')
    # Make the Plot Parameters
    pp_CT_vs_dt = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['CT'], clr_map='cluster', extra_args={'plt_noise':False, 'extra_vars_to_keep':['SA','cluster']}, legend=False)
    pp_press_vs_dt = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['press'], clr_map='cluster', extra_args={'plt_noise':False, 'extra_vars_to_keep':['SA','cluster']}, legend=False)
    # Make the subplot groups ds_BGOS_m280_e050 ds_BGOS
    group_CT_vs_dt = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_CT_vs_dt)
    group_press_vs_dt = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_press_vs_dt)
    # Make the figure
    ahf.make_figure([group_CT_vs_dt, group_press_vs_dt], row_col_list=[2,1, 0.45, 1.4])

################################################################################
# cRL and nir_SA for all clusters
if False:
    print('')
    print('- Creating plots of lateral density ratio and normalized intercluster range vs pressure')
    # Make the Plot Parameters
    pp_nir_SA = ahf.Plot_Parameters(x_vars=['nir_SA'], y_vars=['ca_press'], clr_map='cluster', extra_args={'b_a_w_plt':False, 'plot_noise':False})
    pp_cRL = ahf.Plot_Parameters(x_vars=['cRL'], y_vars=['ca_press'], clr_map='cluster', extra_args={'b_a_w_plt':False, 'plot_noise':False, 'plot_slopes':True})
    # Make the subplot groups
    group_nir_SA = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_nir_SA)
    group_cRL = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_cRL)
    # Make the figure
    ahf.make_figure([group_cRL, group_nir_SA])

################################################################################
## Pre-clustered spans and averages in variables
################################################################################
# Spans in pressure, individual time periods
if False:
    print('')
    print('- Creating plots of cluster span in pressure')
    # Make the Plot Parameters
    pp_clstr_span = ahf.Plot_Parameters(x_vars=['pcs_press'], y_vars=['pca_press'], clr_map='cluster', extra_args={'plt_noise':False, 'extra_vars_to_keep':['SA']}, legend=True) 
    # Make the subplot groups
    group_clstrs_0 = ahf.Analysis_Group(ds_BGR04, pfs_0, pp_clstr_span)
    group_clstrs_1 = ahf.Analysis_Group(ds_BGR0506, pfs_0, pp_clstr_span)
    group_clstrs_2 = ahf.Analysis_Group(ds_BGR0607, pfs_0, pp_clstr_span)
    group_clstrs_3 = ahf.Analysis_Group(ds_BGR0708, pfs_0, pp_clstr_span)
    # # Make the figure
    ahf.make_figure([group_clstrs_0, group_clstrs_1, group_clstrs_2, group_clstrs_3])
# Spans in pressure, all time periods
if False:
    print('')
    print('- Creating plots of cluster span in pressure')
    # Make the Plot Parameters
    pp_clstr_span = ahf.Plot_Parameters(x_vars=['pcs_press'], y_vars=['pca_press'], clr_map='cluster', extra_args={'plt_noise':False, 'extra_vars_to_keep':['SA']}, legend=True) 
    # Make the subplot groups
    group_clstrs_0 = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_clstr_span)
    # # Make the figure
    ahf.make_figure([group_clstrs_0])

################################################################################
## Pre-clustered comparing clusters across time periods
################################################################################
# BGR ITP clustering, comparing specific clusters
if False:
    print('')
    print('- Creating SA-Time plot to look at a single cluster across different periods')
    # Define the profile filters
    pfs_these_clstrs = ahf.Profile_Filters(clstrs_to_plot=[4,5,6])
    # Make the Plot Parameters
    # pp_these_clstrs = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['lat'], clr_map='cluster', legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']})#, 'clstrs_to_plot':[4,5,6]}) 
    pp_these_clstrs = ahf.Plot_Parameters(x_vars=['BSA'], y_vars=['aCT'], clr_map='cluster', legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['cluster']})#, 'clstrs_to_plot':[4,5,6]}) 
    # Make the subplot groups
    group_these_clstrs = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_these_clstrs)
    # # Make the figure
    ahf.make_figure([group_these_clstrs])
################################################################################
## Pre-clustered comparing single clusters across time periods
################################################################################
# Define the profile filters
pfs_these_clstrs = ahf.Profile_Filters(clstrs_to_plot=[6])
# Just one cluster in SA vs. la_CT space
if False:
    print('')
    print('- Creating plot of pre-clustered BGR ITP data for just one cluster')
    pp_pre_clstrd = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'sort_clstrs':False, 'b_a_w_plt':True}, ax_lims={'x_lims':test_S_range})
    # Make the subplot groups
    group_pre_clstrd = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_pre_clstrd)
    # Plot the figure
    ahf.make_figure([group_pre_clstrd], use_same_y_axis=False)
# Just one cluster plotting SA, CT, lon, and lat vs. time
if False:
    print('')
    print('- Creating plots across time to look at a single cluster across different periods')
    # Make the Plot Parameters
    pp_SA_and_CT = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['SA','CT'], legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster']})#, 'clstrs_to_plot':[4,5,6]}) 
    pp_lat_and_lon = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['lon','lat'], legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster']})#, 'clstrs_to_plot':[4,5,6]}) 
    # Make the subplot groups
    group_SA_and_CT = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_SA_and_CT)
    group_lat_and_lon = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_lat_and_lon)
    # # Make the figure
    ahf.make_figure([group_SA_and_CT, group_lat_and_lon], row_col_list=[2,1, 0.45, 1.4])
# Just one cluster plotting SA, CT, and press vs. time with trend lines
if False:
    print('')
    print('- Creating plots across time to look at a single cluster across different periods')
    # Make the Plot Parameters
    pp_SA = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['SA'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']})#, 'clstrs_to_plot':[4,5,6]}) 
    pp_CT = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['CT'], legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']})
    pp_press = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['press'], legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']})
    # Make the subplot groups
    group_SA = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_SA)
    group_CT = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_CT)
    group_press = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_press)
    # Make the figure
    ahf.make_figure([group_SA, group_CT, group_press], row_col_list=[3,1, 0.45, 1.4])
# Just one cluster plotting SA, CT, and press vs. longitude with trend lines
if False:
    print('')
    print('- Creating plots across longitude to look at a single cluster across different periods')
    # Make the Plot Parameters
    pp_SA = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['SA'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR})#, 'clstrs_to_plot':[4,5,6]}) 
    pp_CT = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['CT'], legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR})
    pp_press = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['press'], legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR})
    # Make the subplot groups
    group_SA = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_SA)
    group_CT = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_CT)
    group_press = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_press)
    # Make the figure
    ahf.make_figure([group_SA, group_CT, group_press], row_col_list=[3,1, 0.45, 1.4])
# Just one cluster plotting SA, CT, and press vs. latitude with trend lines
if False:
    print('')
    print('- Creating plots across latitude to look at a single cluster across different periods')
    # Make the Plot Parameters
    pp_SA = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['SA'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lat_BGR})#, 'clstrs_to_plot':[4,5,6]}) 
    pp_CT = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['CT'], legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lat_BGR})
    pp_press = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['press'], legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lat_BGR})
    # Make the subplot groups
    group_SA = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_SA)
    group_CT = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_CT)
    group_press = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_press)
    # Make the figure
    ahf.make_figure([group_SA, group_CT, group_press], row_col_list=[3,1, 0.45, 1.4])
# Maps and histograms of one cluster's profile averages in SA, CT, and press
if False:
    print('')
    print('- Creating maps of one cluster`s profile averages in SA, CT, and press')
    # Make the Plot Parameters
    pp_map_SA = ahf.Plot_Parameters(plot_type='map', clr_map='pca_SA', legend=False, extra_args={'map_extent':'Western_Arctic', 'extra_vars_to_keep':['SA','cluster']})
    pp_map_CT = ahf.Plot_Parameters(plot_type='map', clr_map='pca_CT', legend=False, extra_args={'map_extent':'Western_Arctic', 'extra_vars_to_keep':['SA','cluster']})
    pp_map_press = ahf.Plot_Parameters(plot_type='map', clr_map='pca_press', legend=False, extra_args={'map_extent':'Western_Arctic', 'extra_vars_to_keep':['SA','cluster']})
    pp_hist_SA = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['hist'], y_vars=['pca_SA'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']})
    pp_hist_CT = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['hist'], y_vars=['pca_CT'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']})
    pp_hist_press = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['hist'], y_vars=['pca_press'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']})
    # Make the subplot groups
    group_map_SA = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_map_SA)
    group_map_CT = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_map_CT)
    group_map_press = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_map_press)
    group_hist_SA = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_hist_SA)
    group_hist_CT = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_hist_CT)
    group_hist_press = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_hist_press)
    # # Make the figure
    ahf.make_figure([group_map_SA, group_map_CT, group_map_press, group_hist_SA, group_hist_CT, group_hist_press])#, row_col_list=[2,1, 0.45, 1.4])
# Maps and histograms of one cluster's profile spans in SA, CT, and press
if False:
    print('')
    print('- Creating maps of one cluster`s profile spans in SA, CT, and press')
    # Make the Plot Parameters
    pp_map_SA = ahf.Plot_Parameters(plot_type='map', clr_map='pcs_SA', legend=False, extra_args={'map_extent':'Western_Arctic', 'extra_vars_to_keep':['SA','cluster']})
    pp_map_CT = ahf.Plot_Parameters(plot_type='map', clr_map='pcs_CT', legend=False, extra_args={'map_extent':'Western_Arctic', 'extra_vars_to_keep':['SA','cluster']})
    pp_map_press = ahf.Plot_Parameters(plot_type='map', clr_map='pcs_press', legend=False, extra_args={'map_extent':'Western_Arctic', 'extra_vars_to_keep':['SA','cluster']})
    pp_hist_SA = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['hist'], y_vars=['pcs_SA'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']})
    pp_hist_CT = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['hist'], y_vars=['pcs_CT'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']})
    pp_hist_press = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['hist'], y_vars=['pcs_press'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']})
    # Make the subplot groups
    group_map_SA = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_map_SA)
    group_map_CT = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_map_CT)
    group_map_press = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_map_press)
    group_hist_SA = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_hist_SA)
    group_hist_CT = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_hist_CT)
    group_hist_press = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_hist_press)
    # # Make the figure
    ahf.make_figure([group_map_SA, group_map_CT, group_map_press, group_hist_SA, group_hist_CT, group_hist_press])#, row_col_list=[2,1, 0.45, 1.4])
# Maps and histograms of one cluster's profile averages and spans in sigma
if False:
    print('')
    print('- Creating maps of one cluster`s profile averages and spans in sigma')
    # Make the Plot Parameters
    pp_press_vs_sigma = ahf.Plot_Parameters(x_vars=['sigma'], y_vars=['press'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']})
    pp_map_sigma_pca = ahf.Plot_Parameters(plot_type='map', clr_map='pca_sigma', legend=False, extra_args={'map_extent':'Western_Arctic', 'extra_vars_to_keep':['SA','cluster']})
    pp_map_sigma_pcs = ahf.Plot_Parameters(plot_type='map', clr_map='pcs_sigma', legend=False, extra_args={'map_extent':'Western_Arctic', 'extra_vars_to_keep':['SA','cluster']})
    pp_hist_sigma = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['hist'], y_vars=['sigma'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']})
    pp_hist_sigma_pca = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['hist'], y_vars=['pca_sigma'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']})
    pp_hist_sigma_pcs = ahf.Plot_Parameters(plot_scale='by_pf', x_vars=['hist'], y_vars=['pcs_sigma'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']})
    # Make the subplot groups
    group_p_vs_sig = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_press_vs_sigma)
    group_map_sigma_pca = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_map_sigma_pca)
    group_map_sigma_pcs = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_map_sigma_pcs)
    group_hist_sigma = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_hist_sigma)
    group_hist_sigma_pca = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_hist_sigma_pca)
    group_hist_sigma_pcs = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_hist_sigma_pcs)
    # # Make the figure
    ahf.make_figure([group_p_vs_sig, group_map_sigma_pca, group_map_sigma_pcs, group_hist_sigma, group_hist_sigma_pca, group_hist_sigma_pcs])#, row_col_list=[2,1, 0.45, 1.4])

################################################################################
## Pre-clustered correcting single clusters with polyfit2d for salinity
################################################################################
# Plotting across lat-lon a cluster's salinity, polyfit2d, and residual
if False:
    print('')
    print('- Creating lat-lon plots for one cluster`s salinity, polyfit2d, and residual') 
    SA_lims = [34.4925,34.4700]
    res_lims = [-0.01125,0.01125]
    # Make the Plot Parameters
    pp_2d = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='SA', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':SA_lims})
    pp_2d_hist = ahf.Plot_Parameters(x_vars=['hist'], y_vars=['SA'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'y_lims':SA_lims})

    pp_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='SA', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':SA_lims})
    pp_og_vs_res = ahf.Plot_Parameters(x_vars=['fit_SA'], y_vars=['SA'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'fit_vars':['lon','lat'], 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':SA_lims, 'y_lims':SA_lims})

    pp_res = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='SA-fit', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'fit_vars':['lon','lat'], 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':res_lims})
    pp_res_hist = ahf.Plot_Parameters(x_vars=['hist'], y_vars=['SA-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'fit_vars':['lon','lat'], 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'y_lims':res_lims})
    # Make the subplot groups
    group_2d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_2d, plot_title='Cluster 6')
    group_2d_hist = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_2d_hist, plot_title='Cluster 6')
    group_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_fit, plot_title='Polynomial Fit')
    group_og_vs_res = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_og_vs_res, plot_title='Original vs. Fit')
    group_res = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_res, plot_title='Residuals')
    group_res_hist = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_res_hist, plot_title='Residuals')
    # # Make the figure
    ahf.make_figure([group_2d, group_fit, group_res, group_2d_hist, group_og_vs_res, group_res_hist])
    # ahf.make_figure([group_2d])
# Plotting a cluster across lat-lon with a polyfit2d in salinity in 2D / 3D
if False:
    print('')
    print('- Creating plot for one cluster with a lat-lon-SA polyfit2d') 
    # Make the Plot Parameters
    pp_2d = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='SA', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':[34.4925,34.4700]})
    pp_3d_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], z_vars=['SA'], clr_map='SA', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'z_lims':[34.4925,34.4700]})
    # Make the subplot groups
    group_2d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_2d)
    group_3d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_3d_fit)
    # # Make the figure
    ahf.make_figure([group_2d, group_3d])
# Plotting a cluster's salinity-polyfit2d across lat-lon in 2D / 3D
if False:
    print('')
    print('- Creating plot for one cluster SA minus lat-lon-SA polyfit2d') 
    # Make the Plot Parameters
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='SA-fit', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR})
    pp_minus_fit3d = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], z_vars=['SA-fit'], clr_map='SA-fit', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'z_lims':[-0.011,0.011]})
    # Make the subplot groups
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit)
    group_minus_fit3d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit3d)
    # # Make the figure
    ahf.make_figure([group_minus_fit, group_minus_fit3d])
# Comparing plots along time for salinity and salinity-polyfit2d with trendlines
if False:
    print('')
    print('- Comparing plots along longitude for one cluster SA minus lat-lon-SA polyfit2d') 
    # Make the Plot Parameters
    pp_p_v_lat = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['SA'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']})
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['SA-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']})
    # Make the subplot groups
    group_p_v_lat = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_p_v_lat, plot_title='Uncorrected')
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit, plot_title='Corrected by lat-lon-SA polyfit2d')
    # # Make the figure
    # ahf.make_figure([group_p_v_lat])
    ahf.make_figure([group_p_v_lat, group_minus_fit], row_col_list=[2,1, 0.45, 1.4])
# Comparing plots along longitude for salinity and salinity-polyfit2d with trendlines
if False:
    print('')
    print('- Comparing plots along longitude for one cluster SA minus lat-lon-SA polyfit2d') 
    # Make the Plot Parameters
    pp_p_v_lat = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['SA'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR})
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['SA-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lon_BGR})
    # Make the subplot groups
    group_p_v_lat = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_p_v_lat, plot_title='Uncorrected')
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit, plot_title='Corrected by lat-lon-SA polyfit2d')
    # # Make the figure
    # ahf.make_figure([group_p_v_lat])
    ahf.make_figure([group_p_v_lat, group_minus_fit], row_col_list=[2,1, 0.45, 1.4])
# Comparing plots along latitude for salinity and salinity-polyfit2d with trendlines
if False:
    print('')
    print('- Comparing plots along latitude for one cluster SA minus lat-lon-SA polyfit2d') 
    # Make the Plot Parameters
    pp_p_v_lat = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['SA'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lat_BGR})
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['SA-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lat_BGR})
    # Make the subplot groups
    group_p_v_lat = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_p_v_lat, plot_title='Uncorrected')
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit, plot_title='Corrected by lat-lon-SA polyfit2d')
    # # Make the figure
    # ahf.make_figure([group_p_v_lat])
    ahf.make_figure([group_p_v_lat, group_minus_fit], row_col_list=[2,1, 0.45, 1.4])
################################################################################
## Pre-clustered correcting single clusters with polyfit2d for temperature
################################################################################
# Plotting across lat-lon a cluster's temperature, polyfit2d, and residual
if False:
    print('')
    print('- Creating lat-lon plots for one cluster`s temperature, polyfit2d, and residual') 
    CT_lims = [-0.83,-0.48]
    res_lims = [.175,-.175]
    # Make the Plot Parameters
    pp_2d = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='CT', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':CT_lims})
    pp_2d_hist = ahf.Plot_Parameters(x_vars=['hist'], y_vars=['CT'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'y_lims':CT_lims})

    pp_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='CT', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':CT_lims})
    pp_og_vs_res = ahf.Plot_Parameters(x_vars=['fit_CT'], y_vars=['CT'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'fit_vars':['lon','lat'], 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':CT_lims, 'y_lims':CT_lims})

    pp_res = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='CT-fit', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'fit_vars':['lon','lat'], 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':res_lims})
    pp_res_hist = ahf.Plot_Parameters(x_vars=['hist'], y_vars=['CT-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'fit_vars':['lon','lat'], 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'y_lims':res_lims})
    # Make the subplot groups
    group_2d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_2d, plot_title='Cluster 6')
    group_2d_hist = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_2d_hist, plot_title='Cluster 6')
    group_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_fit, plot_title='Polynomial Fit')
    group_og_vs_res = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_og_vs_res, plot_title='Original vs. Fit')
    group_res = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_res, plot_title='Residuals')
    group_res_hist = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_res_hist, plot_title='Residuals')
    # # Make the figure
    ahf.make_figure([group_2d, group_fit, group_res, group_2d_hist, group_og_vs_res, group_res_hist])
    # ahf.make_figure([group_2d])
# Plotting a cluster across lat-lon with a polyfit2d in temperature in 2D / 3D
if False:
    print('')
    print('- Creating plot for one cluster with a lat-lon-CT polyfit2d') 
    # Make the Plot Parameters
    pp_2d = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='CT', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['CT','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':[-1.1,-0.45]})
    pp_3d_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], z_vars=['CT'], clr_map='CT', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'z_lims':[-1.1,-0.45]})
    # Make the subplot groups
    group_2d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_2d)
    group_3d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_3d_fit)
    # # Make the figure
    ahf.make_figure([group_2d, group_3d])
# Plotting a cluster's temperature-polyfit2d across lat-lon in 2D / 3D
if False:
    print('')
    print('- Creating plot for one cluster CT minus lat-lon-CT polyfit2d') 
    # Make the Plot Parameters
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='CT-fit', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR})
    pp_minus_fit3d = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], z_vars=['CT-fit'], clr_map='CT-fit', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'z_lims':[-0.42,0.12]})
    # Make the subplot groups
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit)
    group_minus_fit3d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit3d)
    # # Make the figure
    ahf.make_figure([group_minus_fit, group_minus_fit3d])
# Comparing plots along time for temperature and temperature-polyfit2d with trendlines
if False:
    print('')
    print('- Comparing plots along longitude for one cluster CT minus lat-lon-CT polyfit2d') 
    # Make the Plot Parameters
    pp_p_v_lat = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['CT'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']})
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['CT-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']})
    # Make the subplot groups
    group_p_v_lat = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_p_v_lat, plot_title='Uncorrected')
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit, plot_title='Corrected by lat-lon-CT polyfit2d')
    # # Make the figure
    # ahf.make_figure([group_p_v_lat])
    ahf.make_figure([group_p_v_lat, group_minus_fit], row_col_list=[2,1, 0.45, 1.4])
# Comparing plots along longitude for temperature and temperature-polyfit2d with trendlines
if False:
    print('')
    print('- Comparing plots along longitude for one cluster CT minus lat-lon-CT polyfit2d') 
    # Make the Plot Parameters
    pp_p_v_lat = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['CT'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR})
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['CT-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lon_BGR})
    # Make the subplot groups
    group_p_v_lat = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_p_v_lat, plot_title='Uncorrected')
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit, plot_title='Corrected by lat-lon-CT polyfit2d')
    # # Make the figure
    # ahf.make_figure([group_p_v_lat])
    ahf.make_figure([group_p_v_lat, group_minus_fit], row_col_list=[2,1, 0.45, 1.4])
# Comparing plots along latitude for temperature and temperature-polyfit2d with trendlines
if False:
    print('')
    print('- Comparing plots along latitude for one cluster CT minus lat-lon-CT polyfit2d') 
    # Make the Plot Parameters
    pp_p_v_lat = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['CT'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lat_BGR})
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['CT-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lat_BGR})
    # Make the subplot groups
    group_p_v_lat = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_p_v_lat, plot_title='Uncorrected')
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit, plot_title='Corrected by lat-lon-CT polyfit2d')
    # # Make the figure
    # ahf.make_figure([group_p_v_lat])
    ahf.make_figure([group_p_v_lat, group_minus_fit], row_col_list=[2,1, 0.45, 1.4])
################################################################################
## Pre-clustered correcting single clusters with polyfit2d for pressure
################################################################################
# Plotting across lat-lon a cluster's pressure, polyfit2d, and residual
if False:
    print('')
    print('- Creating lat-lon plots for one cluster`s pressure, polyfit2d, and residual') 
    press_lims = [300,170]
    res_lims = [65,-65]
    # Make the Plot Parameters
    pp_2d = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='press', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':press_lims})
    pp_2d_hist = ahf.Plot_Parameters(x_vars=['hist'], y_vars=['press'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'y_lims':press_lims})

    pp_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='press', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':press_lims})
    pp_og_vs_res = ahf.Plot_Parameters(x_vars=['fit_press'], y_vars=['press'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'fit_vars':['lon','lat'], 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':press_lims, 'y_lims':press_lims})

    pp_res = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='press-fit', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'fit_vars':['lon','lat'], 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':res_lims})
    pp_res_hist = ahf.Plot_Parameters(x_vars=['hist'], y_vars=['press-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'fit_vars':['lon','lat'], 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'y_lims':res_lims})
    # Make the subplot groups
    group_2d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_2d, plot_title='Cluster 6')
    group_2d_hist = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_2d_hist, plot_title='Cluster 6')
    group_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_fit, plot_title='Polynomial Fit')
    group_og_vs_res = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_og_vs_res, plot_title='Original vs. Fit')
    group_res = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_res, plot_title='Residuals')
    group_res_hist = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_res_hist, plot_title='Residuals')
    # # Make the figure
    ahf.make_figure([group_2d, group_fit, group_res, group_2d_hist, group_og_vs_res, group_res_hist])
    # ahf.make_figure([group_2d])
# Plotting a cluster across lat-lon with a polyfit2d in pressure in 2D / 3D
if False:
    print('')
    print('- Creating plot for one cluster with a lat-lon-press polyfit2d') 
    # Make the Plot Parameters
    pp_2d = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='press', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':[350,150]})
    pp_3d_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], z_vars=['press'], clr_map='press', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'z_lims':[350,150]})
    # Make the subplot groups
    group_2d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_2d)
    group_3d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_3d_fit)
    # # Make the figure
    ahf.make_figure([group_2d, group_3d])
# Plotting a cluster's pressure-polyfit2d across lat-lon in 2D / 3D
if False:
    print('')
    print('- Creating plot for one cluster press minus lat-lon-press polyfit2d') 
    # Make the Plot Parameters
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='press-fit', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR})
    pp_minus_fit3d = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], z_vars=['press-fit'], clr_map='press-fit', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'z_lims':[-70,70]})
    # Make the subplot groups
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit)
    group_minus_fit3d = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit3d)
    # # Make the figure
    ahf.make_figure([group_minus_fit, group_minus_fit3d])
# Comparing plots along time for pressure and pressure-polyfit2d with trendlines
if False:
    print('')
    print('- Comparing plots along time for one cluster press minus lat-lon-press polyfit2d') 
    # Make the Plot Parameters
    pp_p_v_lat = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['press'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']})
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['press-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']})
    # Make the subplot groups
    group_p_v_lat = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_p_v_lat, plot_title='Uncorrected')
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit, plot_title='Corrected by lat-lon-press polyfit2d')
    # # Make the figure
    # ahf.make_figure([group_p_v_lat])
    ahf.make_figure([group_p_v_lat, group_minus_fit], row_col_list=[2,1, 0.45, 1.4])
# Comparing plots along longitude for pressure and pressure-polyfit2d with trendlines
if False:
    print('')
    print('- Comparing plots along longitude for one cluster press minus lat-lon-press polyfit2d') 
    # Make the Plot Parameters
    pp_p_v_lat = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['press'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR})
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['press-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lon_BGR})
    # Make the subplot groups
    group_p_v_lat = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_p_v_lat, plot_title='Uncorrected')
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit, plot_title='Corrected by lat-lon-press polyfit2d')
    # # Make the figure
    # ahf.make_figure([group_p_v_lat])
    ahf.make_figure([group_p_v_lat, group_minus_fit], row_col_list=[2,1, 0.45, 1.4])
# Comparing plots along latitude for pressure and pressure-polyfit2d with trendlines
if False:
    print('')
    print('- Comparing plots along latitude for one cluster press minus lat-lon-press polyfit2d') 
    # Make the Plot Parameters
    pp_p_v_lat = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['press'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lat_BGR})
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['press-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']}, ax_lims={'x_lims':lat_BGR})
    # Make the subplot groups
    group_p_v_lat = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_p_v_lat, plot_title='Uncorrected')
    group_minus_fit = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_minus_fit, plot_title='Corrected by lat-lon-press polyfit2d')
    # # Make the figure
    # ahf.make_figure([group_p_v_lat])
    ahf.make_figure([group_p_v_lat, group_minus_fit], row_col_list=[2,1, 0.45, 1.4])

################################################################################
## Pre-clustered correcting many clusters with polyfit2d for pressure
################################################################################
pfs_clstr_4 = ahf.Profile_Filters(clstrs_to_plot=[4])
pfs_clstr_5 = ahf.Profile_Filters(clstrs_to_plot=[5])
pfs_clstr_6 = ahf.Profile_Filters(clstrs_to_plot=[6])
pfs_clstr_7 = ahf.Profile_Filters(clstrs_to_plot=[7])
pfs_clstr_8 = ahf.Profile_Filters(clstrs_to_plot=[8])
pfs_clstr_9 = ahf.Profile_Filters(clstrs_to_plot=[9])
# Plotting across lat-lon many clusters' pressure and polyfit2d
if False:
    print('')
    print('- Creating lat-lon plots for many clusters` pressure and polyfit2d') 
    press_lims = [300,170]
    # Make the Plot Parameters
    pp_fit = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['lat'], clr_map='press', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':True, 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR, 'y_lims':lat_BGR, 'c_lims':press_lims})
    # Make the subplot groups
    group_clstr_4 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_4, pp_fit, plot_title='Cluster 4')
    group_clstr_5 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_5, pp_fit, plot_title='Cluster 5')
    group_clstr_6 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_6, pp_fit, plot_title='Cluster 6')
    group_clstr_7 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_7, pp_fit, plot_title='Cluster 7')
    group_clstr_8 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_8, pp_fit, plot_title='Cluster 8')
    group_clstr_9 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_9, pp_fit, plot_title='Cluster 9')
    # # Make the figure
    ahf.make_figure([group_clstr_4, group_clstr_5, group_clstr_6, group_clstr_7, group_clstr_8, group_clstr_9])
# Plotting histograms of many clusters' pressure and polyfit2d
if False:
    print('')
    print('- Creating histograms for many clusters` pressure and polyfit2d') 
    press_lims = [300,170]
    # Make the Plot Parameters
    pp_hist = ahf.Plot_Parameters(x_vars=['hist'], y_vars=['press'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':False, 'extra_vars_to_keep':['SA','cluster']})#, ax_lims={'y_lims':press_lims})
    # Make the subplot groups
    group_clstr_4 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_4, pp_hist, plot_title='Cluster 4')
    group_clstr_5 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_5, pp_hist, plot_title='Cluster 5')
    group_clstr_6 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_6, pp_hist, plot_title='Cluster 6')
    group_clstr_7 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_7, pp_hist, plot_title='Cluster 7')
    group_clstr_8 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_8, pp_hist, plot_title='Cluster 8')
    group_clstr_9 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_9, pp_hist, plot_title='Cluster 9')
    # # Make the figure
    ahf.make_figure([group_clstr_4, group_clstr_5, group_clstr_6, group_clstr_7, group_clstr_8, group_clstr_9])
# Comparing plots along time for pressure and pressure-polyfit2d with trendlines
if False:
    print('')
    print('- Comparing plots along time for many clusters` press minus lat-lon-press polyfit2d') 
    # Make the Plot Parameters
    pp_p_v_lat = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['press'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']})
    pp_minus_fit = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['press-fit'], legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster'], 'fit_vars':['lon','lat']})
    pp_fit = pp_minus_fit
    # Make the subplot groups
    group_clstr_4 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_4, pp_fit, plot_title='Cluster 4')
    group_clstr_5 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_5, pp_fit, plot_title='Cluster 5')
    group_clstr_6 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_6, pp_fit, plot_title='Cluster 6')
    group_clstr_7 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_7, pp_fit, plot_title='Cluster 7')
    group_clstr_8 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_8, pp_fit, plot_title='Cluster 8')
    group_clstr_9 = ahf.Analysis_Group(ds_this_BGR, pfs_clstr_9, pp_fit, plot_title='Cluster 9')
    # # Make the figure
    ahf.make_figure([group_clstr_4, group_clstr_5, group_clstr_6, group_clstr_7, group_clstr_8, group_clstr_9])

################################################################################
## Pre-clustered comparing multiple clusters across time periods
################################################################################
# Define the profile filters
pfs_these_clstrs = ahf.Profile_Filters(clstrs_to_plot=[4,5,6,7,8,9])
# Multiple clusters in SA vs. la_CT space
if False:
    print('')
    print('- Creating plot of pre-clustered BGR ITP data for multiple cluster')
    pp_pre_clstrd = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['la_CT'], clr_map='cluster', extra_args={'sort_clstrs':False, 'b_a_w_plt':True}, ax_lims={'x_lims':test_S_range})
    # Make the subplot groups
    group_pre_clstrd = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_pre_clstrd)
    # Plot the figure
    ahf.make_figure([group_pre_clstrd], use_same_y_axis=False)
# Multiple clusters plotting SA, CT, and press vs. time with trend lines
if False:
    print('')
    print('- Creating plots across time to look at multiple clusters across different periods')
    # Make the Plot Parameters
    pp_SA = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['SA'], clr_map='cluster', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']})#, 'clstrs_to_plot':[4,5,6]}) 
    pp_CT = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['CT'], clr_map='cluster', legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']})
    pp_press = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['press'], clr_map='cluster', legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']})
    # Make the subplot groups
    group_SA = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_SA)
    group_CT = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_CT)
    group_press = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_press)
    # Make the figure
    ahf.make_figure([group_SA, group_CT, group_press], row_col_list=[3,1, 0.45, 1.4])
# Multiple clusters plotting SA, CT, and press vs. longitude with trend lines
if False:
    print('')
    print('- Creating plots across longitude to look at multiple clusters across different periods')
    # Make the Plot Parameters
    pp_SA = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['SA'], clr_map='cluster', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR})#, 'clstrs_to_plot':[4,5,6]}) 
    pp_CT = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['CT'], clr_map='cluster', legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR})
    pp_press = ahf.Plot_Parameters(x_vars=['lon'], y_vars=['press'], clr_map='cluster', legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lon_BGR})
    # Make the subplot groups
    group_SA = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_SA)
    group_CT = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_CT)
    group_press = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_press)
    # Make the figure
    ahf.make_figure([group_SA, group_CT, group_press], row_col_list=[3,1, 0.45, 1.4])
# Multiple clusters plotting SA, CT, and press vs. latitude with trend lines
if False:
    print('')
    print('- Creating plots across latitude to look at multiple clusters across different periods')
    # Make the Plot Parameters
    pp_SA = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['SA'], clr_map='cluster', legend=True, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lat_BGR})#, 'clstrs_to_plot':[4,5,6]}) 
    pp_CT = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['CT'], clr_map='cluster', legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lat_BGR})
    pp_press = ahf.Plot_Parameters(x_vars=['lat'], y_vars=['press'], clr_map='cluster', legend=False, extra_args={'sort_clstrs':False, 'plot_slopes':'OLS', 'extra_vars_to_keep':['SA','cluster']}, ax_lims={'x_lims':lat_BGR})
    # Make the subplot groups
    group_SA = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_SA)
    group_CT = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_CT)
    group_press = ahf.Analysis_Group(ds_this_BGR, pfs_these_clstrs, pp_press)
    # Make the figure
    ahf.make_figure([group_SA, group_CT, group_press], row_col_list=[3,1, 0.45, 1.4])

################################################################################


## la_CT-SA vs. la_CT-SA-dt_start plots
if False:
    print('')
    print('- Creating TS and TS-time plots')
    # Make the Plot Parameters
    pp_CT_SA = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['SA'], clr_map='instrmt', legend=True)
    # pp_CT_SA = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['SA'], clr_map='density_hist', extra_args={'clr_min':0, 'clr_max':10, 'clr_ext':'max', 'xy_bins':1000, 'log_axes':[False,False,True]})
    # pp_CT_SA_3d = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['dt_start'], z_vars=['la_CT'], clr_map='cluster', extra_args={'cl_x_var':'SA', 'cl_y_var':'dt_start', 'cl_z_var':'la_CT', 'm_pts':280, 'b_a_w_plt':False})
    # Make the Analysis Group pfs_fltrd pfs_BGR1
    group_CT_SA_plot = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_CT_SA)
    # group_CT_SA_plot = ahf.Analysis_Group(ds_ITP_test, pfs_BGR1, pp_CT_SA)
    # group_CT_SA_3d_plot = ahf.Analysis_Group(ds_BGOS, pfs_fltrd, pp_CT_SA_3d)
    # Make the figure
    ahf.make_figure([group_CT_SA_plot], filename='Figure_2.pickle')
## lon-dt_start plots
if False:
    print('')
    print('- Creating lon-time plots')
    # Make the Plot Parameters
    pp_lon_dt = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['lon'], clr_map='instrmt')
    # Make the Analysis Group pfs_fltrd pfs_BGR1
    group_lon_dt_plot = ahf.Analysis_Group(ds_this_BGR, pfs_this_BGR, pp_lon_dt)
    # Make the figure
    ahf.make_figure([group_lon_dt_plot])

## Comparing multiple BGR ITP time period clusterings
# BGR ITP clustering
if False:
    print('')
    print('- Creating plots to compare pre-clustered BGR ITP data')
    # this_ds = ds_BGRa_m110
    # this_ds = ds_BGRm_m410
    # this_ds = ds_BGRn_m240
    this_ds = ds_BGRmn
    # this_ds = ds_BGRno
    # this_ds = ds_BGRmno
    # Make the Plot Parameters
    # pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['hist'], clr_map='clr_by_dataset', extra_args={'extra_vars_to_keep':['cluster']}) 
    pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['ca_SA'], y_vars=['ca_CT'], clr_map='clr_by_dataset', extra_args={'extra_vars_to_keep':['cluster'], 'errorbars':True}) 
    # Make the subplot groups
    group_comp_clstrs = ahf.Analysis_Group(this_ds, pfs_0, pp_comp_clstrs)
    # print('done making analysis group')
    # # Make the figure
    ahf.make_figure([group_comp_clstrs])
if False:
    print('')
    print('- Creating plots to compare pre-clustered BGR ITP data')
    # this_ds = ds_BGRa_m110
    # this_ds = ds_BGRm_m410
    # this_ds = ds_BGRn_m240
    # this_ds = ds_BGRmn
    this_ds = ds_BGRno
    # this_ds = ds_BGRmno
    # Make the Plot Parameters
    # pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['hist'], clr_map='clr_by_dataset', extra_args={'extra_vars_to_keep':['cluster']}) 
    pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['ca_SA'], y_vars=['ca_CT'], clr_map='clr_by_dataset', extra_args={'extra_vars_to_keep':['cluster'], 'errorbars':True}) 
    # Make the subplot groups
    group_comp_clstrs = ahf.Analysis_Group(this_ds, pfs_0, pp_comp_clstrs)
    # print('done making analysis group')
    # # Make the figure
    ahf.make_figure([group_comp_clstrs])
if False:
    print('')
    print('- Creating plots to compare pre-clustered BGR ITP periods')
    this_ds = ds_BGR05060708
    # Make the Plot Parameters
    # pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['hist'], clr_map='clr_by_dataset', extra_args={'extra_vars_to_keep':['cluster']}) 
    pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['ca_SA'], y_vars=['ca_CT'], clr_map='clr_by_dataset', extra_args={'extra_vars_to_keep':['cluster'], 'errorbars':False}) 
    # Make the subplot groups
    group_comp_clstrs = ahf.Analysis_Group(this_ds, pfs_0, pp_comp_clstrs)
    # # Make the figure
    ahf.make_figure([group_comp_clstrs])
    #
    pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['ca_SA'], y_vars=['ca_CT'], clr_map='clr_by_dataset', extra_args={'extra_vars_to_keep':['cluster'], 'errorbars':True}) 
    # Make the subplot groups
    group_comp_clstrs = ahf.Analysis_Group(this_ds, pfs_0, pp_comp_clstrs)
    # # Make the figure
    ahf.make_figure([group_comp_clstrs])

# BGR ITP clustering, histograms
if False:
    print('')
    print('- Creating histograms of BGR ITP data')
    # Make the Plot Parameters
    pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['hist'], clr_map='cluster', extra_args={'plt_noise':True}, legend=False, ax_lims={'x_lims':test_S_range})
    # Make the subplot groups
    group_clstr_hist = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_comp_clstrs)
    # # Make the figure
    ahf.make_figure([group_clstr_hist])
# BGR ITP clustering, comparing with histograms
if False:
    print('')
    print('- Creating plots to compare pre-clustered BGR ITP data')
    # Make the Plot Parameters
    pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['hist'], clr_map='cluster', extra_args={'plt_noise':False}, legend=False)#, ax_lims=test_S_range) 
    # Make the subplot groups
    group_comp_clstrs0 = ahf.Analysis_Group(ds_BGR0506, pfs_0, pp_comp_clstrs)
    group_comp_clstrs1 = ahf.Analysis_Group(ds_BGR0607, pfs_0, pp_comp_clstrs)
    group_comp_clstrs2 = ahf.Analysis_Group(ds_BGR0708, pfs_0, pp_comp_clstrs)
    # # Make the figure
    # ahf.make_figure([group_comp_clstrs0, group_comp_clstrs1], row_col_list=[2,1, 0.8, 1.25])
    ahf.make_figure([group_comp_clstrs0, group_comp_clstrs1, group_comp_clstrs2], row_col_list=[3,1, 0.4, 2.0])
# BGR ITP clustering, comparing with histograms, looking for valleys
if False:
    print('')
    print('- Creating plots to compare pre-clustered BGR ITP data')
    # Make the Plot Parameters
    h_bins = 1000
    pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['hist'], clr_map='clr_by_dataset', extra_args={'plt_noise':False, 'log_axes':[False,True,False], 'n_h_bins':h_bins}, legend=False, ax_lims=test_S_range) 
    pp_comp_clstrs1 = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['hist'], clr_map='clr_all_same', extra_args={'plt_noise':False, 'log_axes':[False,True,False], 'n_h_bins':h_bins}, legend=False, ax_lims=test_S_range) 
    # Make the subplot groups
    group_comp_clstrs0 = ahf.Analysis_Group(ds_BGR05060708, pfs_0, pp_comp_clstrs1, plot_title='BGR05060708 with noise')
    group_comp_clstrs1 = ahf.Analysis_Group(ds_BGR05060708_no_noise, pfs_0, pp_comp_clstrs1, plot_title='BGR05060708 without noise')
    # # Make the figure
    ahf.make_figure([group_comp_clstrs0, group_comp_clstrs1], row_col_list=[2,1, 0.8, 1.25])
# BGR ITP clustering, comparing with 2D histograms
if False:
    print('')
    print('- Creating plots to compare pre-clustered BGR ITP data')
    # Make the Plot Parameters
    pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['dt_start'], clr_map='density_hist', extra_args={'clr_min':0, 'clr_max':15, 'clr_ext':'max', 'xy_bins':1000, 'log_axes':[False,False,True]}, legend=False, ax_lims=test_S_range) 
    # Make the subplot groups
    group_comp_clstrs0 = ahf.Analysis_Group(ds_BGR05060708, pfs_0, pp_comp_clstrs, plot_title='BGR05060708 with noise')
    group_comp_clstrs1 = ahf.Analysis_Group(ds_BGR05060708_no_noise, pfs_0, pp_comp_clstrs, plot_title='BGR05060708 without noise')
    # # Make the figure
    ahf.make_figure([group_comp_clstrs0, group_comp_clstrs1], row_col_list=[2,1, 0.8, 1.25])
# BGR ITP clustering, comparing on salinity vs time
if False:
    print('')
    print('- Creating plots to compare pre-clustered BGR ITP data')
    # Make the Plot Parameters
    pp_comp_clstrs = ahf.Plot_Parameters(x_vars=['SA'], y_vars=['dt_start'], clr_map='cluster', legend=False, ax_lims=test_S_range, extra_args={'extra_vars_to_keep':['CT']}) 
    # Make the subplot groups
    group_comp_clstrs0 = ahf.Analysis_Group(ds_BGR05060708, pfs_0, pp_comp_clstrs, plot_title='BGR05060708 with noise')
    group_comp_clstrs1 = ahf.Analysis_Group(ds_BGR05060708_no_noise, pfs_0, pp_comp_clstrs, plot_title='BGR05060708 without noise')
    # # Make the figure
    ahf.make_figure([group_comp_clstrs0, group_comp_clstrs1], row_col_list=[2,1, 0.8, 1.25], filename='test_SA_vs_time.pickle')
    # ahf.make_figure([group_comp_clstrs1])

# BGR ITP clustering, comparing across time
if False:
    print('')
    print('- Creating plots of pre-clustered BGR ITP data')
    pp_pre_clstrd = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['CT'], clr_map='cluster', extra_args={'b_a_w_plt':False}, legend=False)
    # Make the subplot groups
    group_pre_clstrd = ahf.Analysis_Group(ds_BGR0506, pfs_0, pp_pre_clstrd)
    group_pre_clstrd1 = ahf.Analysis_Group(ds_BGR0607, pfs_0, pp_pre_clstrd)
    group_pre_clstrd2 = ahf.Analysis_Group(ds_BGR0708, pfs_0, pp_pre_clstrd)
    # # Make the figure
    ahf.make_figure([group_pre_clstrd, group_pre_clstrd1, group_pre_clstrd2], use_same_x_axis=False)

    pp_pre_clstrd = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['press'], clr_map='cluster', extra_args={'b_a_w_plt':False}, legend=False)
    # Make the subplot groups
    group_pre_clstrd = ahf.Analysis_Group(ds_BGR0506, pfs_0, pp_pre_clstrd)
    group_pre_clstrd1 = ahf.Analysis_Group(ds_BGR0607, pfs_0, pp_pre_clstrd)
    group_pre_clstrd2 = ahf.Analysis_Group(ds_BGR0708, pfs_0, pp_pre_clstrd)
    # # Make the figure
    ahf.make_figure([group_pre_clstrd, group_pre_clstrd1, group_pre_clstrd2], use_same_x_axis=False)
# BGR ITP clustering, SA vs la_CT and SA vs time
exit(0)
for ds_this_BGR in [ds_BGR04, ds_BGR0506, ds_BGR0607, ds_BGR0708]:
    if True:
        print('')
        print('- Creating plots of pre-clustered BGR ITP data')
        pp_pre_clstrd_sali = ahf.Plot_Parameters(x_vars=['la_CT'], y_vars=['SA'], clr_map='cluster', extra_args={'b_a_w_plt':True}, ax_lims={'y_lims':test_S_range})
        pp_pre_clstrd_time = ahf.Plot_Parameters(x_vars=['dt_start'], y_vars=['SA'], clr_map='cluster', extra_args={'b_a_w_plt':False}, legend=False)
        # Make the subplot groups
        group_pre_clstrd_time = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_pre_clstrd_sali)
        group_pre_clstrd_sali = ahf.Analysis_Group(ds_this_BGR, pfs_0, pp_pre_clstrd_time)
        # # Make the figure
        ahf.make_figure([group_pre_clstrd_time, group_pre_clstrd_sali], use_same_x_axis=False)
