from smolagents import InferenceClientModel, CodeAgent
from app.tools.retreiver_tool import retreiver_tool
from app.core.config import Settings

agent = CodeAgent(
    tools = [retreiver_tool],
    model = InferenceClientModel(
        model_id="Qwen/Qwen3-8B",
        api_key=Settings.HF_TOKEN,
    ),
    max_steps = 5,
    verbosity_level = 2
)

# Ask a question that requires retrieving information
question = "For a transformers model training, which is slower, the forward or the backward pass?"

# Run the agent to get an answer
agent_output = agent.run(question)

# Display the final answer
print("\nFinal answer:")
print(agent_output)