import pp

from gdslib.load import load


def coupler_ring(c=pp.c.coupler_ring, **kwargs):
    """ coupler for half a ring

    Args:
        wg_width:0.5
        gap: 0.2
        length_x: 4
        bend_radius: 5

    .. code::

           N0            N1
           |             |
            \           /
             \         /
           ---=========---
        W0    length_x    E0

    .. plot::
        :include-source:

        import gdslib as gl

        c = gl.coupler_ring()
        gl.plot_sparameters(c)

    """
    m = load(c, **kwargs)
    return m


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    wav = np.linspace(1520, 1570, 1024) * 1e-9
    f = 3e8 / wav
    c = coupler_ring()
    s = c.s_parameters(freq=f)

    plt.plot(wav, np.abs(s[:, 1] ** 2))
    print(c.pins)
    plt.show()
