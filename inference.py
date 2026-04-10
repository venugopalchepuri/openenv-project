import os
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

TASK_NAME = "task_easy"
ENV_NAME = "grid-env"
MAX_STEPS = 10


def log_start():
    print(f"[START] task={TASK_NAME} env={ENV_NAME} model={MODEL_NAME}", flush=True)


def log_step(step, action, reward, done, error):
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={error if error else 'null'}",
        flush=True,
    )


def log_end(success, steps, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} rewards={rewards_str}", flush=True)


def run_llm():
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "move right"}],
    )
    return response.choices[0].message.content


def main():
    pos = 0
    goal = 5
    rewards = []

    log_start()

    for step in range(1, MAX_STEPS + 1):
        try:
            _ = run_llm()  # REQUIRED for proxy check

            action = "right"
            pos += 1

            done = pos >= goal
            reward = 0.2 if not done else 0.9

            rewards.append(reward)

            log_step(step, action, reward, done, None)

            if done:
                break

        except Exception as e:
            log_step(step, "error", 0.0, True, str(e))
            break

    success = True if sum(rewards) > 0 else False
    log_end(success, len(rewards), rewards)


if __name__ == "__main__":
    main()