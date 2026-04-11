# trigger
---
title: OpenEnv Mini Grid RL Environment
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 🚀 OpenEnv Mini Grid RL Environment

This project implements a simple reinforcement learning (RL) mini-game environment using the OpenEnv framework.

---

## 🧠 Project Overview

- A grid-based environment where an agent moves toward a goal.
- Designed for automated evaluation using OpenEnv.
- Includes multiple tasks with increasing difficulty.
- Supports structured logging and LLM-based inference.

---

## 🎯 Features

- ✅ Custom RL environment (Grid World)
- ✅ 5 tasks with increasing difficulty:
  - task_easy
  - task_medium
  - task_hard
  - task_expert
  - task_insane
- ✅ Automated graders with valid score range (0,1)
- ✅ OpenEnv-compatible API (`reset`, `step`, `state`)
- ✅ Hugging Face Space deployment
- ✅ Dockerized setup

---

## ⚙️ Environment Design

- Agent starts at position `[0,0]`
- Goal position varies by task difficulty
- Actions:
  - `left`
  - `right`
  - `up`
  - `down`
- Episode ends when agent reaches goal

---

## 📊 Reward Logic

- Small negative reward per step → encourages efficiency
- Positive reward when goal is reached
- Rewards normalized for evaluation

---

## 🧪 Tasks & Graders

Each task has:
- Increasing grid size
- Dedicated grader function
- Score strictly between (0,1)

---

## 🤖 Inference

- Uses OpenAI-compatible client via environment variables:
  - `API_BASE_URL`
  - `MODEL_NAME`
  - `HF_TOKEN`
- Emits structured logs:
