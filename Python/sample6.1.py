try:
	f = open('sample6.1.txt', 'w')
	f.write('Name:Sweater\nAddless:Takizawa_Village')
except:
	print('ファイルを開けません')
finally:
	f.close()

try:
	f = open('sample6.1.txt', 'r')
	lines = f.readlines()
except:
	print('ファイルを読み込めません')
else:
	for l in lines:
		print(l)
finally:
	f.close()
