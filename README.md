# Staircase Clustering Detection Algorithm version 2

Written by Mikhail Schee for the PhD thesis: Thermohaline staircases in the Arctic Ocean: Detection, evolution, and interaction

Based upon the code written for:
Mikhail Schee, Erica Rosenblum, Jonathan M. Lilly, and Nicolas Grisouard (2023) "Unsupervised Clustering Identifies Thermohaline Staircases in the Canada Basin of the Arctic Ocean"
which can be found at https://zenodo.org/doi/10.5281/zenodo.8029947

## License

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    1. Redistributions in source code must retain the accompanying copyright notice, this list of conditions, and the following disclaimer.
    2. Redistributions in binary form must reproduce the accompanying copyright notice, this list of conditions, and the following disclaimer in the documentation and/or other materials provided with the distribution.
    3. Names of the copyright holders must not be used to endorse or promote products derived from this software without prior written permission from the copyright holders.
    4. If any files are modified, you must cause the modified files to carry prominent notices stating that you changed the files and the date of any change.

Disclaimer

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS "AS IS" AND ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Contact

* Corresponding Author: Mikhail Schee (he/him)
* Email: [mikhail.schee@mail.utoronto.ca](mailto:mikhail.schee@mail.utoronto.ca)
* GitHub: https://github.com/scheemik/Staircase_Clustering_Detection_Algorithm_v2

## Summary

This repository contains the code used by the above study to apply the Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN) clustering algorithm to data from Ice Tethered Profilers.

A detailed explanation of how the code was used to make each plot in the study can be found in the accompanying Jupyter notebook `Create_Figures.ipynb`.

## Steps to get final clustered netcdfs

1. Run `make_netcdf.py`, `take_moving_average.py`, and `subsample_netcdf.py`, in that order
2. Make minimal netcdfs to send to Niagara, using `cluster_data.py` and setting `m_pts=None`
3. Send those netcdfs to Niagara, can use `HPC_scp_to_Niagara.sh`
4. Edit `HPC_param_sweep.py` for each run, specifying `ds_this_BGR` and `this_plot_title`, then push to git repo
5. Run parameter sweeps on Niagara, using `HPC_job_submit.sh` (auto runs git pull) without `-c` option 
6. Find the `mpts` with the highest `DBCV` for each netcdf, plot those clusters with `figures.py`
7. Edit the `relab_these` variables for each netcdf so the cluster IDs line up across periods
8. Run `cluster_data.py` with those values of `mpts` and `relab_these` to make clustered netcdfs

## Acknowledgements

The Ice-Tethered Profiler data were collected and made available by the Ice-Tethered Profiler Program (Toole et al., 2011; Krishfield et al., 2008) based at the Woods Hole Oceanographic Institution https://www2.whoi.edu/site/itp/

This repository includes the [orthoregress code](https://gist.github.com/robintw/d94eb527c44966fbc8b9) from [Robin Wilson](https://blog.rtwilson.com/orthogonal-distance-regression-in-python/).

This research was supported in part by the National Science Foundation under Grant No. NSF PHY-1748958. 

We acknowledge fruitful discussions with Maike Sonnewald and Carine van der Boog.

M.S. and N.G. were supported by the Natural Sciences and Engineering Research Council of Canada (NSERC) [funding reference numbers RGPIN-2015-03684 and RGPIN-2022-04560]. J.M.L. was supported by grant number 2049521 from the Physical Oceanography program of the United States National Science Foundation.

