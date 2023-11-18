Dataset **Wind Turbine Detection (by Luke Borkowski)** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/e/9/8P/YJblquxzo7pO8K7fSt26dZlXdtJcXNrLJLL7vKYpN5GMuMkOUlAbPfKQpvi5akOVHjQtjHmXmSxm7yXnLEpBAbBFC9Rcnkgf2VZ6vM4DTfYzxiI8EIe4y9zgIA7I.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Wind Turbine Detection (by Luke Borkowski)', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://github.com/lbborkowski/wind-turbine-detector/archive/refs/heads/master.zip).