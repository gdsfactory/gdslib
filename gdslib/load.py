import numpy as np
import pp
from scipy.constants import speed_of_light
from simphony.elements import Model
from simphony.tools import interpolate

from gdslib.config import CONFIG


def load(component=None, filepath=None, numports=None, **kwargs):
    """ load Sparameters for a component

    Args:
        component: component factory or instance
        filepath:
        numport number of ports
        **kwargs
    """
    if filepath is None:
        component = pp.call_if_func(component, **kwargs)
    pins, f, s = pp.sp.load(
        component, filepath=filepath, dirpath=CONFIG.sp, numports=numports
    )

    def interpolate_sp(freq):
        return interpolate(freq, f, s)

    m = Model()
    m.pins = pins
    m.s_params = (f, s)
    m.s_parameters = interpolate_sp
    m.freq_range = (
        m.s_params[0][0],
        m.s_params[0][-1],
    )  #: The valid frequency range for this model.
    m.wavelengths = speed_of_light / np.array(f)
    m.s = s
    return m


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    c = load(pp.c.mmi1x2())
    # wav = np.linspace(1520, 1570, 1024) * 1e-9
    # f = speed_of_light / wav
    # s = c.s_parameters(freq=f)

    wav = c.wavelengths
    s = c.s
    plt.plot(wav * 1e9, np.abs(s[:, 1] ** 2))

    plt.show()
