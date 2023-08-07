from text.openai_text import OpenAITextGeneration, Messages


text = OpenAITextGeneration()
msgs = Messages()


def run_text_generation(messages, model=None):
    response = text.send_chat_complete(messages=messages, model=model)
    parsed_response = text.parse_openai_response(response)
    print(parsed_response)
    return parsed_response
        
if __name__ == "__main__":
    run_text_generation(text=None, role="user", model="gpt-3.5-turbo")