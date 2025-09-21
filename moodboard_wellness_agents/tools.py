from mem0 import MemoryClient
from google.adk.tools import ToolContext

class Mem0Tool():
    def __init__(self):
        self.mem0 = MemoryClient()

    def search_memory(self, query: str, user_id: str) -> dict:
        """Search through past conversations and memories"""
        memories = self.mem0.search(query, user_id=user_id, output_format='v1.1')
        if memories.get('results', []):
            memory_list = memories['results']
            memory_context = "\n".join([f"- {mem['memory']}" for mem in memory_list])
            return {"status": "success", "memories": memory_context}
        return {"status": "no_memories", "message": "No relevant memories found"}

    def save_memory(self, content: str, user_id: str) -> dict:
        """Save important information to memory"""
        try:
            result = self.mem0.add([{"role": "user", "content": content}], user_id=user_id, output_format='v1.1')
            return {"status": "success", "message": "Information saved to memory", "result": result}
        except Exception as e:
            return {"status": "error", "message": f"Failed to save memory: {str(e)}"}


def exit_safety_loop(tool_context: ToolContext):
    """
    Call this function when safety review is complete and satisfactory.
    This tool allows the safety refinement loop to exit cleanly when
    all safety conditions are met for general wellness management.
    
    Args:
        tool_context: The tool context containing agent information
        
    Returns:
        dict: Status indicating safety review completion
    """
    print(f"[Wellness Safety Loop] Exiting - conditions satisfied by {tool_context.agent_name}")
    tool_context.actions.escalate = True
    return {"status": "safety_review_complete", "message": "Wellness safety review passed all criteria"}


def escalate_safety_concern(tool_context: ToolContext, concern: str = ""):
    """
    Call this function when a serious safety concern is detected that requires
    immediate escalation rather than refinement for general wellness management.
    
    Args:
        tool_context: The tool context containing agent information
        concern: Description of the safety concern
        
    Returns:
        dict: Status indicating escalation
    """
    print(f"[Wellness Safety Loop] ESCALATING - {concern} detected by {tool_context.agent_name}")
    tool_context.actions.escalate = True
    return {
        "status": "safety_escalation", 
        "message": f"Serious wellness safety concern detected: {concern}",
        "requires_human_review": True
    }