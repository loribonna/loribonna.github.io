First steps
===============

1. Install the requirements with ``pip install -r requirements.txt``.

2. From the root directory, run ``python utils/main.py --help`` to see the available options.

Results and logs - WandB
------------------------ 

- The logs are organized in the following way: `<setting>/<dataset>/<model>/logs.pyd`.

- Each line in the log file is a dictionary containing the arguments and results for a single run.

WandB
~~~~~

For advanced logging, including loss values, metrics, and hyperparameters, you can use `WandB <https://wandb.ai/>`_ by providing both ``--wandb_project`` and ``--wandb_entity`` arguments. If you don't want to use WandB, you can simply omit these arguments.

.. tip::
    By default, all arguments, loss values, and metrics are logged.

Metrics are logged on WandB both in a raw form, separated for each task and class. This allows further analysis.

Testing
-------

Mammoth includes a few tests to ensure that the code is working as expected for all available models and datasets. The tests are run using `pytest` and can be run using the following command:

.. code-block:: bash

    pytest --verbose tests

