.. _module-distributed-training:

Distributed training
====================

Mammoth supports distributed training via `DataParallel <https://pytorch.org/docs/stable/nn.html#dataparallel-layers-multi-gpu-distributed>`_. To use it, simply pass the `--distributed=dp` argument to ``utils/main.py``.

DataParallel training **splits the batch** across GPUs and performs the forward and backward passes on each GPU. The gradients are then **averaged** across GPUs and the model parameters are updated. This is the simplest form of distributed training supported by PyTorch and is the only one supported by Mammoth as of now.

.. important::
    As of now, Mammoth only supports DataParallel training. This is due to the difficulty of synchronizing the memory buffer across multiple GPUs after each batch.