.. _paper-aerabs:

May the Forgetting Be with You: Alternate Replay for Learning with Noisy Labels
===============================================================================

    - :fa:`circle-check` `Proceedings of the 35th British Machine Vision Conference <https://bmvc2024.org/proceedings/680/>`_
    - :fa:`calendar` November 2024
    - :fa:`scroll` `BMVC <https://bmvc2024.org/>`_
    - :fa:`tags` :bdg-primary:`Continual Learning` :bdg-primary:`Noisy Label Learning` :bdg-primary:`Rehearsal` :bdg-primary:`Sample Selection`

This study investigates the impact of annotation errors on the performance of rehearsal-based methods, showing that current approaches are limited to the single-epoch scenario. Indeed, as the model is allowed to fit the data from each task, the buffer becomes poisoned by the mislabelled data. We thus propose **AER** and **ABS**, two methods that leverage *forgetting* to mitigate the impact of annotation errors.