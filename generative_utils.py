import google.generativeai as genai
from dotenv import load_dotenv
import os
from config import GENERATION_CONFIG, SAFETY_SETTINGS, PROMPT_PARTS


def setup_generative_model():
    load_dotenv()
    genai.configure(api_key=os.getenv("GENAI_API_KEY"))

    model = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config=GENERATION_CONFIG,
        safety_settings=SAFETY_SETTINGS,
    )
    return model


def generate_content(model, prompt_parts):
    response = model.generate_content(prompt_parts)
    return response


def process_response(response_text):
    lines = response_text.splitlines()
    data_dict = {}

    for item in lines:
        key, value = item.split(": ", 1)
        data_dict[key] = value

    need_action = data_dict["need_action"]
    actions = data_dict["actions"]
    action_time = data_dict["action_time"]
    advice = data_dict["advice"]

    advice = None if advice.lower() == "null" else advice
    action_time = None if action_time.lower() == "null" else action_time
    actions = None if actions.lower() == "null" else actions
    need_action = True if need_action.lower() == "yes" else False

    if actions is not None:
        if "|" in actions:
            actions = [action.strip() for action in actions.split("|")]
        else:
            actions = [actions.strip()]
    else:
        pass

    return need_action, actions, action_time, advice


def util(prompt):
    model = setup_generative_model()

    prompt_parts_extended = PROMPT_PARTS.copy()
    prompt_parts_extended.extend(
        [f"input: {prompt}", "need_action ", "actions ", "action_time ", "advice "]
    )

    response = generate_content(model, prompt_parts_extended)

    need_action, actions, action_time, advice = process_response(response.text)

    prompt_parts_extended = prompt_parts_extended[: len(prompt_parts_extended) - 4]

    return need_action, actions, action_time, advice
