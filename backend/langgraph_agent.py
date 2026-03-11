from langchain_groq import ChatGroq
from langgraph.graph import StateGraph
from typing import TypedDict
import json
import re

llm = ChatGroq(
    api_key="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",
    model="llama-3.3-70b-versatile"
)


class AgentState(TypedDict):
    prompt: str
    extracted_data: dict


def extract_interaction(state: AgentState):

    user_text = state["prompt"]

    prompt = f"""
Extract the following fields from the interaction text.

Return ONLY valid JSON.

Fields:
hcp_name
interaction_type
topics_discussed
sentiment
materials_shared
follow_up

TEXT:
{user_text}
"""

    response = llm.invoke(prompt)

    text = response.content

    print("LLM RAW RESPONSE:", text)

    match = re.search(r"\{[\s\S]*\}", text)

    if match:
        json_text = match.group()

        try:
            data = json.loads(json_text)
        except Exception as e:
            print("JSON ERROR:", e)
            data = {}

    else:
        data = {}

    return {"extracted_data": data}


builder = StateGraph(AgentState)

builder.add_node("extract", extract_interaction)

builder.set_entry_point("extract")

graph = builder.compile()


def run_agent(prompt):

    result = graph.invoke({"prompt": prompt})

    print("FINAL DATA:", result["extracted_data"])

    return result["extracted_data"]