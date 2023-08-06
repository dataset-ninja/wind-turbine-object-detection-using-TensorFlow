Dataset **Wind Turbine Detection (by Luke Borkowski)** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/F/x/H3/gh3LhNG7E4kFgBDGeDXWnkR0lao32XDBSwE8gx77W6E5qBeTAL7kD8IQz3gIa7MEzCJsSMUKnY9PR2O47itqesoaeWTaiIL2giBlbVMe7wF7sOn81EFjlcXiGljo.tar)

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

The data in original format can be [downloaded here](https://github.com/lbborkowski/wind-turbine-detector/archive/refs/heads/master.zip)