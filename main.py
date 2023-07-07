from src.gl_api_requester.GLAPIRequester import *

def main():
	requester = GLAPIRequester()

	print(requester.get_user_from_name('vadeledav'))

if __name__ == "__main__":
	main()
