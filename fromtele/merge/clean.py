with open('fromtele/merged.txt', 'r') as file:
    lines = file.readlines()

filtered_lines = [line for line in lines if not line.startswith('<div class="tgme_widget_message_text js-message_reply_text')]

with open('fromtele/mergedclean.txt', 'w') as file:
    file.writelines(filtered_lines)
