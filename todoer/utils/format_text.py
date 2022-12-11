def msg_formatter(message_text, head, foot):
	head = f"**╒═⟦ {head} ⟧**\n"
	foot = f"\n**╘═⟦ {foot} ⟧**"
	text = f"{head}{message_text}{foot}"
	return text