post = "Hey harry bhai is good, harry bhai is very good and harry is great"

if("Harry".lower() in post.lower()):
	# convert both harry string and post string so there will be fair comparison
	print("This post is probably talking about \"harry\"")
else:
	print("This post doesn't even have a mention of \"harry\"")
