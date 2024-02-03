# generative_utils.py
# This module is designed to interface with the Google Generative AI API to generate content based on provided prompts.
# It utilizes environment variables for configuration and relies on custom settings defined in a separate config module.
# The core functionality includes setting up a generative model, generating content, and processing the AI-generated responses.

import google.generativeai as genai  # Import Google's generative AI module
from dotenv import (
    load_dotenv,
)  # Import dotenv for loading environment variables from .env files
import os  # Import os for accessing environment variables
from config import (
    GENERATION_CONFIG,
    SAFETY_SETTINGS,
    PROMPT_PARTS,
)  # Import configuration constants

load_dotenv()  # Load environment variables from a .env file, should be called once at the start of the application


def setup_generative_model():
    """
    Sets up and returns a generative model instance configured with API key and specified settings.

    Raises:
        ValueError: If the GENAI_API_KEY environment variable is not set, indicating configuration issue.

    Returns:
        genai.GenerativeModel: An instance of the GenerativeModel configured with the necessary settings.
    """
    api_key = os.getenv("GENAI_API_KEY")  # Retrieve API key from environment variables
    if not api_key:
        raise ValueError(
            "GENAI_API_KEY is not set in the environment variables."
        )  # Error if API key is missing
    genai.configure(api_key=api_key)  # Configure the genai module with the API key
    return genai.GenerativeModel(
        model_name="gemini-pro",  # Specify the model name
        generation_config=GENERATION_CONFIG,  # Apply generation configuration settings
        safety_settings=SAFETY_SETTINGS,  # Apply safety settings
    )


model = setup_generative_model()  # Initialize the generative model on module load


def generate_content(model, prompt_parts):
    """
    Generates content by invoking the model's generate_content method with given prompt parts.

    Parameters:
        model (genai.GenerativeModel): The generative model instance to use for content generation.
        prompt_parts (list): A list of strings that make up the parts of the prompt to be sent to the generative model.

    Returns:
        The response from the generative model.
    """
    response = model.generate_content(
        prompt_parts
    )  # Generate content using the model and prompt parts
    return response


def process_response(response_text):
    """
    Processes the text response from the generative model, extracting structured information.

    Parameters:
        response_text (str): The raw text response from the generative model.

    Returns:
        tuple: A tuple containing structured information extracted from the response, including:
               - need_action (bool): Indicates whether an action is needed based on the response.
               - actions (list or None): A list of actions to take, if any.
               - action_time (str or None): The suggested time for action, if any.
               - advice (str or None): Additional advice provided in the response.
               - flag (bool): A flag indicating whether the response contained any data.
    """
    lines = response_text.splitlines()  # Split the response text into lines
    data_dict = {}  # Initialize an empty dictionary to hold processed data
    flag = bool(lines)  # Set flag based on whether there are any lines in the response

    for item in lines:
        key, value = item.split(": ", 1)  # Split each line into key-value pairs
        data_dict[key] = value  # Store the key-value pairs in the dictionary

    # Extract and process specific fields from the response
    need_action = (
        data_dict["need_action"].lower() == "yes"
    )  # Determine if action is needed
    actions = (
        None if data_dict["actions"].lower() == "null" else data_dict["actions"]
    )  # Extract actions, handling null
    action_time = (
        None if data_dict["action_time"].lower() == "null" else data_dict["action_time"]
    )  # Extract action time, handling null
    advice = (
        None if data_dict["advice"].lower() == "null" else data_dict["advice"]
    )  # Extract advice, handling null

    if actions:
        actions = [
            action.strip() for action in actions.split("|")
        ]  # Split and strip actions if not None

    return need_action, actions, action_time, advice, flag  # Return the structured data


def util(prompt):
    """
    Utility function to generate content based on a given prompt, process the response, and return structured information.

    Parameters:
        prompt (str): The input prompt based on which content is to be generated.

    Returns:
        tuple: A tuple containing structured information extracted from the generated content, similar to process_response.
    """
    model = setup_generative_model()  # Set up a new generative model instance

    # Extend the default prompt parts with additional details based on the input prompt
    prompt_parts_extended = PROMPT_PARTS.copy()
    prompt_parts_extended.extend(
        [f"input: {prompt}", "need_action ", "actions ", "action_time ", "advice "]
    )

    response = generate_content(
        model, prompt_parts_extended
    )  # Generate content using the extended prompt parts

    # Process the text response to extract structured information
    need_action, actions, action_time, advice, flag = process_response(response.text)

    # Remove the last 4 elements from prompt_parts_extended, reverting to original prompt parts
    prompt_parts_extended = prompt_parts_extended[: len(prompt_parts_extended) - 4]

    return (
        need_action,
        actions,
        action_time,
        advice,
        flag,
    )  # Return the structured information
