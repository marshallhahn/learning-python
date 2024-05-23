def emoji_converter(message):
    EMOJI_MAPPING = {":)": "🙂", ":(": "😞", ":D": "😁"}

    words = message.split(" ")

    output = ""
    for word in words:
        output += EMOJI_MAPPING.get(word, word) + " "
    return output


user_input = input("How are you feeling? ")
converted = emoji_converter(message=user_input)
print(converted)
