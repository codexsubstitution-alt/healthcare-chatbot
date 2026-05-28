DOMAIN_FEATURES = ["Conversational question input", "Context-aware answer panel", "Suggested follow-up prompts", "Session summary and notes"]
DOMAIN_ENTITIES = ["conversation", "message", "topic", "advice"]
SAMPLE_INPUTS = ["What questions can I ask this assistant?", "Give me a quick summary for a first-time user.", "What should I do next based on this issue?"]


def _pick_relevant_terms(message: str) -> list[str]:
    lowered = message.lower()
    matches = [
        item for item in DOMAIN_FEATURES + DOMAIN_ENTITIES
        if any(part.lower() in lowered for part in item.split()[:2])
    ]
    return matches[:4] or DOMAIN_FEATURES[:3]


def generate_reply(blueprint: dict, message: str) -> dict:
    terms = _pick_relevant_terms(message)
    focus = ", ".join(terms)
    answer = (
        f"Thanks for sharing that. For {blueprint['project_name']}, "
        f"the best response is to focus on {focus}. "
        f"Based on your input, start with the user's immediate need, "
        f"keep the workflow simple, and turn the result into clear next actions."
    )
    suggestions = [
        f"Ask about {DOMAIN_ENTITIES[0]} details",
        f"Use {DOMAIN_FEATURES[0].lower()}",
        SAMPLE_INPUTS[0],
    ]
    next_steps = [
        "Confirm the user's goal",
        "Collect the minimum required details",
        "Return a concise recommendation",
        "Offer one practical follow-up action",
    ]
    return {
        "project": blueprint["project_name"],
        "message": message,
        "answer": answer,
        "suggestions": suggestions,
        "next_steps": next_steps,
    }
