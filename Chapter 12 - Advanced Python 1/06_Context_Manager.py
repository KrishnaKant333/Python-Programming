with(
	open("file1.txt") as f1,
	open("file2.txt") as f2
):
	pass

# we can use multiple context managers in a single With statement using parenthesis.
