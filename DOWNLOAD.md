Dataset **Wind Turbines 9** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/T/x/VX/c3e76sozsdvOl6yInn8bGGDptJmQleZIH4hSIOCDcpYba9zXxEN8HfmUi7nd2K4VO183Y9UCmRKGlBrBjfWfSNeuobXnxZRZRXMleEtjSs2Olozam58LW4rmdZHr.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Wind Turbines 9', dst_path='~/dtools/datasets/Wind Turbines 9.tar')
```
The data in original format can be 🔗[downloaded here](https://github.com/lbborkowski/wind-turbine-detector/archive/refs/heads/master.zip)