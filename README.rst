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
* Documentation: https://pyircor.readthedocs.io.


.. Features
.. --------

.. * TODO


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


Reference
--------
::

  @inproceedings{urbano2017ties,
    author = {Urbano, Juli{\'{a}}n and Marrero, M{\'{o}}nica},
    booktitle = {ACM SIGIR International Conference on the Theory of Information Retrieval},
    pages = {321--324},
    title = {{The Treatment of Ties in AP Correlation}},
    year = {2017}
  }
