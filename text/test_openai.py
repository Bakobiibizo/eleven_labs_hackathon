from text.openai_text import OpenAITextGeneration, Messages


text = OpenAITextGeneration()
msgs = Messages()


def run_text_generation(messages, model, role="user"):
    response = text.send_chat_complete(messages, model, role)
    print(response)
    return response
        
if __name__ == "__main__":
    run_text_generation(
        messages="this is a test of the openai api endpoint",  
        model="gpt-3-5-turbo", 
        role="user",
        )