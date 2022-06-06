def msg_formatter(message_text, head, foot):
	head = f"**╒═⟦ {head} ⟧**\n\n"
	foot = f"\n\n**╘═⟦ {foot} ⟧**"
	text = f"{head}{message_text}{foot}"
	return text