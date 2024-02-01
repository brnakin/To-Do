# Configuration settings for content generation
GENERATION_CONFIG = {
    "temperature": 0.05,
    "top_p": 0.1,
    "top_k": 1,
    "max_output_tokens": 1024,
}

# Safety settings to filter harmful content
SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

# Prompt for model
PROMPT_PARTS = [
    'Task: Design a to-do list app that interprets user-provided text inputs, determining whether action is required and, if so, identifying action/s, their respective timelines, and offering succinct advice. When analyzing the input, evaluate whether there is a verb in the sentence.  For example, "buy" is a verb, but "buying" is not. Automatically detect the language that used in input and give response with that language for just action, action_time and advice parameters. For example, if the input is English the response should be English, if the input is Turkish the response should be Turkish. Do not code! Do not create more than one actions. Do not create sub action. Do not fragmentate of the action. Do not give more than one advice. Input Format: Each input will contain a task or activity. Information will include whether the task requires actions (needs_actions: Yes), the specific actions needed (actions), the time frame or deadline for these actions (actions_time), and a concise advice (advice). Input/Output Format: Input: [Task description] need_action: [Yes/No] actions: [Action or actions] action_time: [Time frame or deadline] advice: [One or two pieces of advice related to the task]',
    "input: Yarın köpek için mama siparişi ver",
    "need_action No",
    "actions null",
    "action_time Yarın",
    "advice Mamayı seçerken köpeğinin diyetini gözden geçirmeyi unutma",
    "input: Send a birthday gift to my friend in Japan",
    "need_action Yes",
    "actions Purchase gift that you choose | Ship the gift",
    "action_time null",
    "advice Consider their interests and preferences when selecting a gift",
    "input: Tomorrow I'll do the weekly shop.",
    "need_action Yes",
    "actions Make shopping list | Purchase groceries",
    "action_time Tomorrow",
    "advice Plan your meals for the week and create a detailed shopping list to ensure you get everything you need",
    "input: Pizza night with friends this saturday",
    "need_action No",
    "actions null",
    "action_time Saturday",
    "advice null",
    "input: Send CV to companies",
    "need_action Yes",
    "actions Prepare the CV | Send the CV",
    "action_time null",
    "advice Tailor your CV to each specific job application, highlighting relevant skills and experience.",
    "input: Fix the broken light switch",
    "need_action Yes",
    "actions Fix the switch",
    "action_time null",
    "advice If attempting DIY repairs, ensure you turn off the power first",
    "input: Drinking water with friends",
    "need_action No",
    "actions Gather friends | Get water",
    "action_time null",
    "advice null",
    "input: Study exam this night",
    "need_action Yes",
    "actions Study exam",
    "action_time Tonight",
    "advice Break down the material into smaller chunks and study in intervals to improve retention",
    "input: Help to Karen",
    "need_action Yes",
    "actions Help Karen",
    "action_time null",
    "advice Be patient and understanding, and offer your support in any way you can",
    "input: Meeting with Kim",
    "need_action No",
    "actions Prepare for the meeting | Attend the meeting",
    "action_time null",
    "advice null",
    "input: Meeting with friends",
    "need_action No",
    "actions null",
    "action_time null",
    "advice null",
    "input: Recharge Netflix subscription",
    "need_action Yes",
    "actions Renew Netflix subscription",
    "action_time null",
    "advice Recharge your subscription before it expires to avoid any interruption in service",
    "input: Upload the edited engagement photos",
    "need_action Yes",
    "actions Edit engagement photos | Upload enagagement photos",
    "action_time null",
    "advice When you upload your photos, give them descriptive filenames",
    "input: Dog grooming appointment on Friday",
    "need_action No",
    "actions null",
    "action_time Friday",
    "advice null",
    "input: Pizza night with friends this Saturday",
    "need_action No",
    "actions null",
    "action_time Saturday",
    "advice null",
    "input: Mother's day gift pickup",
    "need_action Yes",
    "actions Pick up Mother's day gift",
    "action_time null",
    "advice Add a handwritten card or note to the gift for a personal touch",
    "input: Bu haftasonu sınavlarına çalışmayı unutma",
    "need_action Yes",
    "actions Sınavlara çalış",
    "action_time Bu haftasonu",
    "advice Sınavlara çalışırken düzenli aralıklarla mola verin ve çalıştığınız konuları tekrar gözden geçirin",
    "input: I have some money for Friday night",
    "need_action No",
    "actions null",
    "action_time Friday night",
    "advice null",
    "input: Buying flowers for Valentine's Day",
    "need_action No",
    "actions null",
    "action_time Valentine's Day",
    "advice null",
    "input: Buy flowers for Valentine's Day",
    "need_action Yes",
    "actions Buy flowers",
    "action_time Valentine's Day",
    "advice Choose flowers that are in season and that your loved one will appreciate",
    "input: Paying the payments",
    "need_action No",
    "actions null",
    "action_time null",
    "advice null",
    "input: Pay the payments",
    "need_action Yes",
    "actions Pay the payments",
    "action_time null",
    "advice Set up automatic payments to avoid late fees",
]
