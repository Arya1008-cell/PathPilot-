from langgraph.graph import StateGraph
from llm_utils import get_llm

llm = get_llm()


def career_agent(state):
    profile = state["profile"]

    prompt = f"""
Based on this student profile:

{profile}

Give a SHORT response only.

Format:
Careers:
- 3 career suggestions (one line each)

Skills Needed:
- 4–5 important skills only

Roadmap:
- 3 simple steps only

Keep answer concise and clear.
No long explanations.
"""

    
    response = llm.invoke(prompt)

    return {"result": response.content}


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("career", career_agent)
    graph.set_entry_point("career")

    return graph.compile()
