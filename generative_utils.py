import google.generativeai as genai
from dotenv import load_dotenv
import os
from config import GENERATION_CONFIG, SAFETY_SETTINGS, PROMPT_PARTS


load_dotenv()  # Call it once, ideally at the start of your app


def setup_generative_model():
    api_key = os.getenv("GENAI_API_KEY")
    if not api_key:
        raise ValueError("GENAI_API_KEY is not set in the environment variables.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config=GENERATION_CONFIG,
        safety_settings=SAFETY_SETTINGS,
    )


model = setup_generative_model()


def generate_content(model, prompt_parts):
    response = model.generate_content(prompt_parts)
    return response


def process_response(response_text):
    lines = response_text.splitlines()
    data_dict = {}
    flag = bool(lines)  # Directly assign based on the truthiness of lines

    for item in lines:
        key, value = item.split(": ", 1)
        data_dict[key] = value

    # Simplify conversions with direct assignments
    need_action = data_dict["need_action"].lower() == "yes"
    actions = None if data_dict["actions"].lower() == "null" else data_dict["actions"]
    action_time = (
        None if data_dict["action_time"].lower() == "null" else data_dict["action_time"]
    )
    advice = None if data_dict["advice"].lower() == "null" else data_dict["advice"]

    # Streamline actions handling
    if actions:
        actions = [action.strip() for action in actions.split("|")]

    return need_action, actions, action_time, advice, flag


def util(prompt):
    model = setup_generative_model()

    prompt_parts_extended = PROMPT_PARTS.copy()
    prompt_parts_extended.extend(
        [f"input: {prompt}", "need_action ", "actions ", "action_time ", "advice "]
    )

    response = generate_content(model, prompt_parts_extended)

    need_action, actions, action_time, advice, flag = process_response(response.text)

    prompt_parts_extended = prompt_parts_extended[: len(prompt_parts_extended) - 4]

    return need_action, actions, action_time, advice, flag
