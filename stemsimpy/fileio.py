import numpy as np
import yaml


def array_from_multislice(fname):
    """
    Load numpy array from multislice output text file.

    Expected format:

    
    Parameters
    ----------
    fname:     str, file or pathlib.Path
                
    """
    tmparray = np.loadtxt(fname=fname,
                          dtype={'names': ('ix',
                                           'iy',
                                           'real_amplitude',
                                           'imag_amplitude'),
                                 'formats': ('u4',
                                             'u4',
                                             'f8',
                                             'f8')})
    nx = np.max(tmparray['ix'])
    ny = np.max(tmparray['iy'])
#    print(tmparray[0:2])
#    print(tmparray[672:675])
    result = np.empty(shape=nx*ny, dtype=np.complex128)
    result = tmparray['real_amplitude'] + 1j * tmparray['imag_amplitude']
    result = result.reshape((nx, ny))
#    print(result.shape)
#    print(result[0,0], result[0,1], result[1,0])
    return result


def open_yaml(yamlfile):
    """
    
    Parameters
    ----------
    yamlfile:   str
                YAML file to be opened
    """
    with open(yamlfile, 'r') as stream:
        try:
            yamldata = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return yamldata



