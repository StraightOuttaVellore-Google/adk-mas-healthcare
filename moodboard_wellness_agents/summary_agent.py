from .prompts import SUMMARY_AGENT_PROMPT
from google.adk.agents import LlmAgent
from .tools import Mem0Tool
import os

mem0_tool = Mem0Tool()

summary_agent = LlmAgent(
    model=os.getenv("MODEL_NAME"),
    name="summary_agent",
    instruction=SUMMARY_AGENT_PROMPT,
    output_key="generated_summary",
    tools=[mem0_tool.save_memory, mem0_tool.search_memory]
)