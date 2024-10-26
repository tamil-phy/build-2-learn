from fastapi import FastAPI
from pydantic import BaseModel
from detector import DementiaDetector
from langchain_core.messages import AIMessage, HumanMessage
from data import STORIES
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
_detector = DementiaDetector()

class Payload(BaseModel):
    story_id: int
    user_id: int
    conversations: list[str]

@app.post("/inference/")
def get_inference(messages: Payload):
    conv = [

    ]
    for ind, message in enumerate(messages.conversations):
        if ind % 2 == 0:
            conv.append(AIMessage(message))
        else:
            conv.append(HumanMessage(message))

    res = _detector.detect(
                     user_id=messages.user_id,
                     story_id=messages.story_id,
                     conversation=conv
                     )

    return {"result": res}

@app.get("/story/{story_id}")
def get_story(story_id):
    return STORIES.get(story_id)
