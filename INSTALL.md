## Installation	

⚠️ **ART 6.1** is the last version to support **Python 3.5** officially	

⚠️ **ART 4.4** is the last version to support **Python 2.7** & **Python 3.4** officially		

⚠️ **PyPI** support of these versions will be removed in a **future release**


### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install art==6.1` (Need root access)

### Source code
- Download [Version 6.1](https://github.com/sepandhaghighi/art/archive/v6.1.zip) or [Latest Source](https://github.com/sepandhaghighi/art/archive/dev.zip)
- `pip install .`

### Conda

#### Conda-Forge
- Check [Conda-Forge](https://conda-forge.org)
- `conda install -c conda-forge ascii-art ` (Need root access)

#### Private channel
- Check [Conda Managing Package](https://conda.io)
- `conda install -c sepandhaghighi art ` (Need root access)

### MATLAB

- Download and install [MATLAB](https://www.mathworks.com/products/matlab.html) (>=8.5, 64/32 bit)
- Download and install [Python3.x](https://www.python.org/downloads/) (>=3.5, 64/32 bit) 
	- [x] Select `Add to PATH` option
	- [x] Select `Install pip` option
- Run `pip install art` (Need root access)
- Configure Python interpreter
```matlab
>> pyversion PYTHON_EXECUTABLE_FULL_PATH
```
- Visit [MATLAB Examples](https://github.com/sepandhaghighi/art/tree/master/MATLAB)	
