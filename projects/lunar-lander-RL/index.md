---
layout: single
title: "Lunar Lander: Reinforcement Learning"
author_profile: true
---

## About This Project
This project, built for CSPB 3202: Intro to AI, implements and trains a baseline Deep Q-Network (DQN) and a Double DQN agent to solve Gymnasium's LunarLander-v3 environment. Core components include a replay buffer for stable, sample-efficient learning, an epsilon-greedy policy for balancing exploration and exploitation, and a target network to stabilize training targets.

The baseline DQN plateaued around a 197 average score and never sustained a "solved" 100-episode average, revealing a stability failure consistent with DQN's known overestimation bias. Switching to Double DQN, which decouples action selection from evaluation, solved the environment at episode 962 with a 201.57 average, confirming that the architectural change measurably improved training stability. A follow-up six-configuration hyperparameter sweep over learning rate and epsilon decay then showed that tuning the exploration schedule mattered just as much as the algorithmic choice: the best-tuned configuration (epsilon decay=0.99) solved the environment faster and reached a higher final score (265.32) than Double DQN's own default hyperparameters, while a poorly chosen learning rate or epsilon decay could erase Double DQN's advantage entirely.

The notebook walks through the full workflow, from a random-agent baseline (-176.37 average) through both DQN implementations, the hyperparameter sweep, and a discussion of results, and closes with recorded video demonstrations comparing the random agent against the trained Double DQN agent landing consistently.

## Project Documentation
- [Lunar Lander Notebook](/projects/lunar-lander-RL/LunarLander_SGillihan.html)

## Technologies Used
- Python
- PyTorch
- OpenAI Gymnasium (Box2D)
- NumPy
- Matplotlib
- MoviePy

## Repository
Repository link: [Lunar Lander RL](https://github.com/sgillihan/LunarLander.git)

