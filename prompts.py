from pprint import pprint

from langchain_core.prompts import ChatPromptTemplate


def get_prompt(history):
    return ChatPromptTemplate.from_messages([
        ("system", "Paraphrase the text and then write a friendly blog."),
        ("placeholder", "{history}")
    ]).invoke({"history": history})


if __name__ == '__main__':
    message = [
        ("human", "Write a blog on Tech"),
    ]
    prompt = get_prompt(message)
    pprint(f"{prompt}=")
