.. _paper-ccic:

Continual semi-supervised learning through contrastive interpolation consistency
================================================================================

    - :fa:`circle-check` `10.1016/j.patrec.2022.08.006 <https://doi.org/10.1016/j.patrec.2022.08.006>`_
    - :fa:`calendar` October 2022
    - :fa:`scroll` `PRL <https://www.sciencedirect.com/journal/pattern-recognition-letters>`_
    - :fa:`tags` :bdg-primary:`Continual Learning` :bdg-primary:`Semi-Supervised Learning` :bdg-primary:`Consistency Regularization` :bdg-primary:`Contrastive Learning`

This work is the result of my :ref:`MSc thesis <msc-thesis>`.

Existing Continual Learning methods often require labeled data for each task, which is impractical in real-world scenarios. This study explores **Continual Semi-Supervised Learning** (**CSSL**), where only a small portion of labeled data is available. Evaluating current CL methods in this setting reveals challenges of overfitting. We propose a novel CSSL method: **Contrastive Continual Interpolation Consistency** (**CCIC**), which imposes consistency among augmented and interpolated examples while exploiting secondhand information peculiar to the Class-Incremental setting. Results demonstrate its robustness to limited supervision, outperforming state-of-the-art methods when these are trained with full supervision.