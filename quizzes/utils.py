def validate_nonempty_quiz_elements(quiz_name, questions_list, choices_dict):
    error_messages = []
    if quiz_name == '':
        error_messages.append('Quiz name cannot be empty.')
    for question in questions_list:
        if question == '':
            error_messages.append('Questions cannot be empty.')
            break
    for key in choices_dict:
        for choice in choices_dict[key]:
            if choice == '':
                error_messages.append('Choices cannot be empty.')
    return error_messages
