from .summary_agent import summary_agent
from .rec_agent import recommendation_agent
from .tools import exit_safety_loop, escalate_safety_concern
from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent, LoopAgent
import os

parallel_wellness_agent = ParallelAgent(
    name="parallel_wellness_agent",
    sub_agents=[summary_agent, recommendation_agent],
    description="Runs multiple wellness agents in parallel"
)

# Safety Reviewer - analyzes current state for general wellness management
safety_reviewer_agent = LlmAgent(
    model=os.getenv("MODEL_NAME"),
    name="safety_reviewer_agent",
    instruction="""You are a safety reviewer analyzing AI responses for general wellness management.

Current Summary: {generated_summary}
Current Recommendation: {recommendation}

Evaluate safety and provide feedback:
1. Check for harmful advice or crisis indicators
2. Verify professional tone and appropriateness
3. Ensure no medical diagnosis/prescription advice
4. Look for general wellness safety concerns

If SAFE and meets all criteria, respond with: "SAFETY_APPROVED"
If needs improvement, provide specific feedback for refinement.

Focus on these red flags:
- Self-harm indicators, suicidal ideation
- Substance abuse concerns
- Abusive relationships
- Severe mental health crises
- Inappropriate medical recommendations
- Crisis situations requiring professional help

Respond with either "SAFETY_APPROVED" or specific feedback for improvement.""",
    output_key="safety_feedback"
)

# Safety Refiner - improves based on feedback or exits
safety_refiner_agent = LlmAgent(
    model=os.getenv("MODEL_NAME"),
    name="safety_refiner_agent",
    instruction="""You are a safety refiner for general wellness AI responses.

Safety Feedback: {safety_feedback}
Current Summary: {generated_summary}
Current Recommendation: {recommendation}

If feedback is "SAFETY_APPROVED": Call the exit_safety_loop tool immediately.

Otherwise, refine the responses based on safety feedback:
1. Remove harmful content
2. Add appropriate disclaimers
3. Improve professional tone
4. Add crisis resource information if needed
5. Ensure wellness advice is safe and appropriate

Output refined JSON with same structure but improved safety:
{{
    "is_safe": true/false,
    "safety_score": 0.0-1.0,
    "concerns": ["list of concerns if any"],
    "recommendations_approved": true/false,
    "summary_approved": true/false,
    "modifications_needed": ["specific changes if needed"],
    "overall_assessment": "brief assessment"
}}""",
    tools=[exit_safety_loop, escalate_safety_concern],
    output_key="safety_guidelines"
)

# Safety Refinement Loop - iteratively improves safety until approved
safety_refinement_loop = LoopAgent(
    name="safety_refinement_loop",
    sub_agents=[safety_reviewer_agent, safety_refiner_agent],
    max_iterations=3,  # Prevent infinite loops
    description="Iteratively refines wellness responses until safety criteria are met"
)

wellness_agent = SequentialAgent(
    name="wellness_agent",
    sub_agents=[parallel_wellness_agent, safety_refinement_loop],
    description="Coordinates parallel wellness analysis with iterative safety refinement."
)

root_agent = wellness_agent
