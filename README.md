# GDRXYZ

Player's data will be stored in a list of dictionaries, the key is the player id which is just the len() of list_of_players in the moment the player is created,
the values will be a list which contain:

- Name
- Race

- Stats:
    is a dictionary:
    "attribute":int_value
    attribute can be:
      - "int"
      - "str"
      - "phy"
      - "agl"
      - "teq"
      
- Skills:
      will be a dictionary:
        "skill_name":int_skill_level
