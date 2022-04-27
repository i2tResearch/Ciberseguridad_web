# PDG-Analysis-Of-Time-Windows-to-detect-Botnet-Behaviour-APP-


## prerequisites

1. Use Linux Distribution
2. VUE JS
3. NFDUMP

## To run The Front

Please, do the following steps:

1. Open in visual studio code the front-end folder
2. Open a terminal
3. Use the following command:

```bash
npm run serve
```


## To run The Back

1. Enable NFPCAPD

```bash

move to nfdump installation folder
. /configure - -enable-nfpcapd
Make
Sudo make install

```
2. Open CMD

3. Configure the app.main of Flask

```bash

cd backend/Controllers/
export FLASK_APP=ServiceControllers.py
```
3. Execute App

```bash

flask run
```



## Possible Errors

### Permission denied: ‘/usr/bin/dumpcap’

![Image description](https://github.com/JulioCe98/PDG-Analysis-Of-Time-Windows-to-detect-Botnet-Behaviour-APP-/blob/master/Resources/permissionDenied.png)

### Possible solution

![Image description](https://github.com/JulioCe98/PDG-Analysis-Of-Time-Windows-to-detect-Botnet-Behaviour-APP-/blob/master/Resources/permissionDeniedSolution.png)

Use only the first line.


### Permission not permite /sniff of scapy

![Image description](https://github.com/JulioCe98/PDG-Analysis-Of-Time-Windows-to-detect-Botnet-Behaviour-APP-/blob/master/Resources/errorScapy.png)

### Possible solution

![Image description](https://github.com/JulioCe98/PDG-Analysis-Of-Time-Windows-to-detect-Botnet-Behaviour-APP-/blob/master/Resources/permissionDeniedSolution.png)

where PythonX.X. is the version 3.6

