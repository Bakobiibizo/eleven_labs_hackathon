from text.openai_text import OpenAITextGeneration, Messages


text = OpenAITextGeneration()
msgs = Messages()


def run_text_generation(message, role="user", model=None):
    response = text.send_chat_complete(content=message, role=role, model=model)
    print(response)
    return response
        
if __name__ == "__main__":
    run_text_generation(text=None, role="user", model="gpt-3.5-turbo")