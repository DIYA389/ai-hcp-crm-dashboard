from pydantic import BaseModel

class InteractionCreate(BaseModel):
    hcp_name:str
    interaction_type:str
    date:str
    topics_discussed:str
    sentiment:str
    materials_shared:str
    follow_up:str