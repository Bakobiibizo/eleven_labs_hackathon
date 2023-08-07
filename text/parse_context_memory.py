def parse_messages(json_data):
    with open (json_data, "r") as f:
        json_data = f.read()
    parsed_list = []

    for entry in json_data:
        # For entries with a single 'message'
        if "message" in entry:
            parsed_list.append({
                "role": entry["message"]["role"],
                "content": entry["message"]["content"]
            })
        # For entries with a list of 'messages'
        elif "messages" in entry:
            for message in entry["messages"]:
                parsed_list.append({
                    "role": message["role"],
                    "content": message["content"]
                })
                print(parsed_list)

    return parsed_list


