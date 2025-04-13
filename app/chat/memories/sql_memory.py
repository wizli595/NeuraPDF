from pydantic.v1 import BaseModel
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseChatMessageHistory
from app.web.api import (get_messages_by_conversation_id,add_message_to_conversation)

class SQLMemory(BaseChatMessageHistory,BaseModel):
    """
    SQLMemory stores messages in a SQL database and retrieves them for a conversation.
    It uses the ConversationBufferMemory from Langchain to manage the message history.
    """

    conversation_id: str
    @property
    def messages(self):
        """
        Retrieves messages from the database for the given conversation_id.
        """
        return get_messages_by_conversation_id(self.conversation_id)
    
    def add_message(self, message):
        """
        Adds a message to the database for the given conversation_id.
        """
        return add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message.content
        )
    def clear(self):
        pass

def build_memory(chat_args):
    """
    Builds a SQLMemory instance for the given conversation_id.
    """
    return ConversationBufferMemory(
        chat_memory=SQLMemory(conversation_id=chat_args.conversation_id),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer",
    )