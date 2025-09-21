from .prompts import RECOMMENDATION_AGENT_PROMPT
from google.adk.agents import LlmAgent
from .tools import Mem0Tool
import os

mem0_tool = Mem0Tool()

recommendation_agent = LlmAgent(
    model=os.getenv("MODEL_NAME"),
    name="recommendation_agent",
    instruction=RECOMMENDATION_AGENT_PROMPT,
    output_key="recommendation",
    tools=[mem0_tool.save_memory, mem0_tool.search_memory]
)