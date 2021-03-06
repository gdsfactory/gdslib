from SiPANN.scee import HalfRacetrack
from SiPANN.scee_int import SimphonyWrapper

from gdslib.autoname import autoname
from gdslib.plot_model import plot_model


@autoname
def coupler_ring(
    radius: float = 5,
    width: float = 0.5,
    thickness: float = 0.22,
    gap: float = 0.22,
    length_x: float = 4.0,
    sw_angle: float = 90.0,
    **kwargs
):
    r"""Return model for for half a ring coupler.

    Args:
        radius: 5
        width: float or ndarray Width of the waveguide in um (Valid for 0.4-0.6)
        thickness : float or ndarray Thickness of waveguide in um (Valid for 0.18-0.24)
        gap : float or ndarray Minimum distance between the two waveguides edge in um. (Must be > 0.1)
        length_x: Length of straight portion of ring waveguide in um
        sw_angle: Sidewall angle from horizontal in degrees, ie 90 makes a square. Defaults to 90.
        kwargs: geometrical args that this model ignores

    .. code::

           N0            N1
           |             |
            \           /
             \         /
           ---=========---
        W0    length_x    E0


            2 \           / 4
               \         /
                ---------
            1---------------3


    .. plot::
        :include-source:

        import gdslib as gl

        m = gl.c.coupler_ring()
        gl.plot_model(m)

    """

    width = width * 1e3
    thickness = thickness * 1e3
    gap = gap * 1e3
    length = length_x * 1e3
    radius = radius * 1e3
    # print(f'ignoring {kwargs}')

    s = HalfRacetrack(
        radius=radius,
        width=width,
        thickness=thickness,
        gap=gap,
        length=length,
        sw_angle=sw_angle,
    )
    s2 = SimphonyWrapper(s)
    s2.pins = ("W0", "N0", "E0", "N1")
    return s2


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    c = coupler_ring()
    print(c)
    wavelengths = np.linspace(1.5, 1.6) * 1e-6
    plot_model(c, wavelengths=wavelengths)
    plt.show()
