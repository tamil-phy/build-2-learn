from unittest import TestCase
from dotenv import load_dotenv
from detector import DementiaDetector
from langchain_core.messages import HumanMessage, AIMessage
from detector import DementiaDetector

class TestConversation(TestCase):

    def setUp(self):
        load_dotenv()
        self._detector = DementiaDetector()

    def test_conversation(self):
        conversations = [
            HumanMessage("Hi, there")
        ]
        res = self._detector.detect(user_id=1, story_id=1, conversation=conversations)
        print(res)



