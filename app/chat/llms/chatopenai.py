from langchain_openai import ChatOpenAI

def build_llm(chat_args):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A chain

    Example Usage:

        chain = build_llm(chat_args)
    """
    return ChatOpenAI()