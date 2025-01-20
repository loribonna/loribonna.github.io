.. _paper-starprompt:

Semantic Residual Prompts for Continual Learning
================================================

    - :fa:`circle-check` `10.1007/978-3-031-73030-6_1 <https://doi.org/10.1007/978-3-031-73030-6_1>`_
    - :fa:`calendar` October 2024
    - :fa:`scroll` `ECCV <https://eccv2024.ecva.net/>`_
    - :fa:`tags` :bdg-primary:`Continual Learning` :bdg-primary:`Prompt Selection` :bdg-primary:`Rehearsal-free` :bdg-primary:`Pretrain-based`

 
We study the impact of forgetting on the prompt-selection mechanism adopted in most pretrain-based models (*e.g.*, L2P, CODA-Prompt, DualPrompt) and we introduce **STAR-Prompt** a *two-level prompt selection* strategy where an initial Vision-Language model (*CLIP*) is used to select the most relevant second-level prompts. The second-level prompts are then used to guide the learning of the target task using a *semantic residual* approach.