# Reward Sampler

Pretty simple code. Generates n candidates for completions every k tokens. Uses a reward model to pick the best completion. I got pretty coherent results with Qwen0.5b as a generator and a GPT2 reward model as the discriminator.

### Sources

This isn't my idea, here's some stuff that inspired it:
 - https://redwoodresearch.substack.com/p/getting-50-sota-on-arc-agi-with-gpt
