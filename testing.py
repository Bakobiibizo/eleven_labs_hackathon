from handlers import data_handler


handler = data_handler.DataHandler()


def test_text(message = None):
    response = handler.handle_chat(content=message, role="user")
    with open("output/text_output.txt", "w") as f:
        f.write(response)
        print(response)
    return response


if __name__=="__main__":
    test_text()