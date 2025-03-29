def check_force_sub(client, user_id):
    user = client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
    return user.status in ["member", "administrator", "creator"]
