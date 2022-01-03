from django.shortcuts import redirect

class LoginRequired:
	def __init__(self, get_response):
		self.get_response = get_response
		self.login_except_urls = ['/', '/blogs/', '/accounts/login/', '/accounts/signup/']

	def __call__(self, request):
		if not request.user.is_authenticated and request.path not in self.login_except_urls:
			return redirect('login')

		response = self.get_response(request)

		return response