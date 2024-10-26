from langchain_core.messages import SystemMessage, BaseMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from data import STORIES


class DementiaDetector:

    _detector_prompt = """
    You are provided with a list of conversations from a user, Your task is to detect the potential signs of dementia he/she might have.
    You'll be provided with a story to ask the user questions from. You need to ask questions from them.
    If you feel the user is not answering correctly, help them slightly. If the user doesn't answer correctly in the following conversation, You can declare that they have dementia.
    
    Story --> 
    {story}
    """

    _prompt_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=_detector_prompt),
            MessagesPlaceholder(variable_name="messages")
        ]
    )

    def __init__(self):
        self._llm = self._prompt_template | ChatOpenAI()

    def _retrieve_story(self, story_id):
        return STORIES.get(story_id)

    def detect(self, user_id: int, story_id: int, conversation: list[BaseMessage]):
        _story = self._retrieve_story(story_id)
        res = self._llm.invoke({"story": _story, "messages": conversation})
        return res.content


