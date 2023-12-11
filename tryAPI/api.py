headers = {'cookie': 'kobonaut=xxx'}
resp = requests.get(url, headers=headers)
xls = pd.read_excel(resp.content)
return xls
