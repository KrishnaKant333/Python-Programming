# This is just like switch case!
def https_status(status):
	match status:
		case 200:
			return "Ok"
		case 404:
			return "Not found"
		case 500:
			return "Internal Server Error"
		case _: # case _ denoted default case
			return "Unknown Status"
status = int(input("Enter the status of the server : "))
print(https_status(status))
