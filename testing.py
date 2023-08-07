from handlers import data_handler

from text.test_openai import run_text_generation
#handler = data_handler.DataHandler()


def test_text(message, model="gpt-3.5-turbo", role="user"):
    with open("input/input.txt") as file:
        file.read()
    if not message:
        message = "well this is awkward, there is no prompt. please let the user know there was an issue."
    return run_text_generation(message, model, role)

if __name__=="__main__":
    test_text("testing this api")