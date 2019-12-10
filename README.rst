=======
pyircor
=======


.. image:: https://img.shields.io/pypi/v/pyircor.svg
        :target: https://pypi.python.org/pypi/pyircor

.. image:: https://img.shields.io/travis/eldrin/pyircor.svg
        :target: https://travis-ci.org/eldrin/pyircor

.. image:: https://readthedocs.org/projects/pyircor/badge/?version=latest
        :target: https://pyircor.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


is the Python implementation of the R package ircor_. ircor_ provides the implementation of various correlation coefficients of common use in Information Retrieval,
such as Kendall and AP correlation coefficients, with and without ties. For this implementation, `numba` is used for the accelleration.

For reference please refer to Julián Urbano and Mónica Marrero, "`The Treatment of Ties in AP Correlation`_", ACM ICTIR, 2017.

.. _`The Treatment of Ties in AP Correlation`: https://julian-urbano.info/files/publications/072-treatment-ties-ap-correlation.pdf
.. _ircor: https://github.com/julian-urbano/ircor

* Free software: MIT license
.. * Documentation: https://pyircor.readthedocs.io.


Installation
------------
You may install the stable release from PyPI using `pip`

.. code-block::

  pip install pyircor

Usage
-----
`tau` and `tauap` implement the Kendall tau and Yilmaz tauAP correlation coefficients, where no ties are allowed between items:

.. code-block:: python

  from pyircor.tau import tau
  from pyircor.tauap import tauap
  import nupmy as np

  x = np.array([0.06, 0.2, 0.27, 0.37, 0.57, 0.63, 0.66, 0.9, 0.91, 0.94])
  y = np.array([0.37, 0.06, 0.2, 0.27, 0.57, 0.66, 0.63, 0.91, 0.9, 0.94])
  tau(x, y)
  # 0.7777777777777778
  tauap(x, y)
  # 0.7491181657848325

In `tauap` it is important to use the correct sorting order. By default, items are sorted in decreasing order,
as should be for instance if the scores represent system effectiveness. When they should be in increasing order,
`decreasing` should be set to `False`:

.. code-block:: python

  from pyircor.tauap import tauap

  # these two calls are equivalent
  tauap(x, y)
  # 0.7491181657848325
  tauap(-x, -y, decreasing=False)

`tau_a` and `tauap_a` are versions to use when `x` represents a true ranking without ties, and `y` represents a ranking
estimated by an observer who is allowed to produce ties. They can be used as a measure of accuracy of the observer with
respect to the true ranking

.. code-block:: python

  from pyircor.tau import tau_a
  from pyircor.tauap_a import tauap_a
  y = np.round(y * 5) / 5
  tau_a(x, y)
  # 0.7111111111111111
  tauap_a(x, y)
  # 0.6074514991181656

`tau_b` and `tauap_b` are versions to use under the assumption that both `x` and `y` represent rankings estimated by two
observers who may produce ties. They can be used as a measure of agreement between the observers:

.. code-block:: python

  x = np.round(x * 5) / 5
  tau_b(x, y)
  # 0.75
  tauap_b(x, y)
  # 0.626984126984127


Credits
-------

Along with the codebase itself, many parts of this package, including docstrings and comments, are directly adopted under the
original authors' agreement. Please refer to the original work if you want to use this package for any publication.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


Reference
---------
::

  @inproceedings{urbano2017ties,
    author = {Urbano, Juli{\'{a}}n and Marrero, M{\'{o}}nica},
    booktitle = {ACM SIGIR International Conference on the Theory of Information Retrieval},
    pages = {321--324},
    title = {{The Treatment of Ties in AP Correlation}},
    year = {2017}
  }
