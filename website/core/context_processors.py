from datetime import datetime

def current_date(request):
	today = datetime.today()
	return {'datetime': today}
