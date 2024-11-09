# Overview

This module defines a `Dataset` object which stores some analytical data in an [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html). One may then standardize these data in various ways to convert “raw” measurements of the relative abundances of CO2 isotopologue into δ values corresponding to canonical metrological scales (VPDB, VSMOW) or Δ values corresponding to different isotopic anomalies (Δ17O, Δ638, Δ828).

After performing one or more standardization procedures, the `Dataset` object stores the following additional information:

* `samples`: a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) of all samples in the dataset, along with their mean raw measurements and their standardized values (along with the corresponding standard error, 95 % confidence limits, and standard deviation).
* `sessions`: a dictionary where each value is a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) of all analytical sessions in the dataset for a given quantity (e.g., `d13C_VPDB`), along with some statistics (number of anchors/unknowns in each session, instrumental correction parameters and their uncertainties).

The `Dataset` object also provides some plotting methods, such as:

* `Dataset.plot_residuals()`: display analytical residuals over time
* `Dataset.plot_D17O_residuals()`: plot the covariation of (δ18O, Δ17O) residuals