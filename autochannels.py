DEFAULT_HOUR = 6

AUTOCHANNELS = {}
with open("autochannels.txt") as f:
	for line in f:
		c = line.strip().split(' : ')
		if len(c) >= 2:
			AUTOCHANNELS[c[0]] = c[1]

def export_autochannels() -> None:
	with open("autochannels.txt", "w") as f:
		w = ""
		for channel in AUTOCHANNELS:
			w += f"{channel} : {AUTOCHANNELS[channel]}\n"
		f.write(w)

def add_autochannel(channel: str, hour: int) -> None:
	
	channel = str(channel)
	
	if hour < 0 or hour > 23:
		hour = DEFAULT_HOUR
	
	AUTOCHANNELS[channel] = hour
	export_autochannels()

def remove_autochannel(channel: str) -> None:
	
	channel = str(channel)
	
	AUTOCHANNELS.pop(channel, None)
	export_autochannels()

print("> Existing autochannel data established")
