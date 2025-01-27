.. _paper-secondorder:

A Second-Order Perspective on Model Compositionality and Incremental Learning
=============================================================================

    - :fa:`circle-check` `Proceedings of the 13th International Conference on Learning Representations <https://openreview.net/forum?id=OZVTqoli2N>`_
    - :fa:`calendar` Apr 2025
    - :fa:`scroll` `ICLR <https://openreview.net/group?id=ICLR.cc/2025>`_
    - :fa:`tags` :bdg-primary:`Task Arithmetic` :bdg-primary:`Unlearning` :bdg-primary:`Specialization` :bdg-primary:`Model Compositionality` :bdg-primary:`Incremental Learning`

We examine how fine-tuning deep pre-trained models yields compositional modules in non-linear networks, using a *second-order* Taylor approximation of the loss. Our findings show that staying within the pre-training basin is key for preserving composability. Building on this, we propose two incremental training strategies: **ITA**, where each task is handled by an individually trained module; and **IEL**, a complementary approach that jointly optimizes the composed model. Both methods foster an accurate multi-task model with flexible editing capabilities, enabling specialization or unlearning for specific tasks.