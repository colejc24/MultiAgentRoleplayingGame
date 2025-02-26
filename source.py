from autogen import ConversableAgent, GroupChat, GroupChatManager
from secret import SECRET_KEY

#Unused right now
human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,
    human_input_mode="ALWAYS",
)

dungeonMaster = ConversableAgent(
    "DM",
    system_message="You are a dungeon master for a tabletop role-playing game.",
    llm_config={"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": SECRET_KEY}]},
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
)

goblinPlayer = ConversableAgent(
    "goblinPlayer",
    system_message="You are a player in a tabletop role-playing game. You are playing as a Goblin Bard who grew up as a theif.",
    llm_config={"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": SECRET_KEY}]},
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
)

elfPlayer = ConversableAgent(
    "elfPlayer",
    system_message="You are a player in a tabletop role-playing game. You are playing as an Elven Archer who grew up as a high prince.",
    llm_config={"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": SECRET_KEY}]},
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
)

dwarfPlayer = ConversableAgent(
    "dwarfPlayer",
    system_message="You are a player in a tabletop role-playing game. You are playing as an Dwarf Warrior who grew up in the mines.",
    llm_config={"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": SECRET_KEY}]},
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
)

group_chat = GroupChat(
    agents=[dungeonMaster, goblinPlayer, elfPlayer, dwarfPlayer, human_proxy],
    messages=[],
    max_round=10,
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config={"config_list": [{"model": "gpt-3.5-turbo", "api_key": SECRET_KEY}]},
)

chat_result = dungeonMaster.initiate_chat(
    group_chat_manager,
    message="Start a new game of Dungeons and Dragons.",
    summary_methods="reflection_with_llm"
)