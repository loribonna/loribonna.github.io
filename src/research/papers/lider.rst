.. _paper-lider:

On the Effectiveness of Lipschitz-Driven Rehearsal in Continual Learning
========================================================================

    - :fa:`circle-check` `Advances in Neural Information Processing Systems 35 <https://proceedings.neurips.cc/paper_files/paper/2022/hash/cf10920ac985275845247f865b452529-Abstract-Conference.html>`_
    - :fa:`calendar` November 2022
    - :fa:`scroll` `NeurIPS <https://neurips.cc/>`_
    - :fa:`tags` :bdg-primary:`Continual Learning` :bdg-primary:`Rehearsal` :bdg-primary:`Lipschitz Regularization`

The paper highlights a common issue in Continual Learning: *using rehearsal methods to prevent forgetting can lead to unstable decision boundaries*. To address this, we propose **Lipschitz-DrivEn Rehearsal** (**LiDER**), which smooths the network's outputs by constraining its Lipschitz constant for respect to replay examples. We show that LiDER improves performance across datasets for rehearsal CL methods, with or without pre-training, and shed light on buffer overfitting in CL.