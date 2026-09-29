from smolagents import CodeAgent, InferenceClientModel
from app.tools.tools import sql_engine
from app.core.config import Settings


def main():
    if not Settings.HF_TOKEN:
        raise RuntimeError("HF_TOKEN is not set. Add it to the environment or a .env file.")

    agent = CodeAgent(
        tools=[sql_engine],
        model=InferenceClientModel(
            model_id="Qwen/Qwen3-8B",
            api_key=Settings.HF_TOKEN,
        ),
    )
    print(agent.run("Can you give me the name of the client who got the most expensive receipt?"))


if __name__ == "__main__":
    main()
