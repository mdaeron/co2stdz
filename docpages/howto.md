# How-to

## Create a dataset

Start with a csv with each line corresponding to a single analysis, and the following (case-sensitive) column names:
* `Sample` (mandatory; case sensitive): this is the (unique) name of a homogeneous amount of analyte (water, carbonate powder, tank of CO2...) that was analyzed one or more times. Sample names should preferably start with a ASCII letter (A-Z or a-z) and only contain ASCII letters, numbers, and underscores ('_') or dashes ('-').
* `UID` (optional but strongly recommended; case sensitive): a unique identifier for a each analysis.
* `Session` (optional; case sensitive): this is the (unique) name of an analytical session during which a given analysis was performed. All measurements performed in a given session will be standardized by applying a session-specific set of instrumental corrections. If no `Session` is specified, all analyses will be treated as belonging to the same session, arbitrarily named `this_session`.
* `d636`, `d628`, `d13C_raw`... (optional): any number of aritrarily named raw measurements expressed in permil relative to a session-specific working reference gas.
* `P`, `carb_mass`, `timetag`... (optional): any number of aritrarily named raw measurements expressed in permil relative to a session-specific working reference gas.

The CSV might look like this:

```
.. include:: ../examples/example_dataset.csv
```

To import this data into a `Dataset()` object, use `read_csv()`:

```py
from co2spectroscopy import Dataset
ds = Dataset()
ds.read_csv('some_data.csv')
# append some more data from a different csv:
ds.read_csv('some_new_data.csv')
```

## Standardize carbon-13 measurements

You'll need to provide at least two δ13C anchors (in-lab standards and/or international reference materials such as [IAEA603](https://analytical-reference-materials.iaea.org/iaea-603)), specifying their nominal δ13CVPDB values.

Example code:
```py
.. include:: ../examples/example_d13C.py
```
The above code will first randomly generate the following dataset:

```
.. include:: ../examples/example_d13C_data.txt
```
 
Then `standardize()` will convert raw δ636 measurements (`d636`) into δ13C values referenced to the VPDB scale (`d13C_VPDB`). The results are stored in `ds.samples`:
 
```
.. include:: ../examples/example_d13C_samples.txt
```

The correction parameters for each analytical session are stored in `ds.sessions['d13C_VPDB']`:
 
```
.. include:: ../examples/example_d13C_sessions.txt
```

<h1>API Documentation</h1>