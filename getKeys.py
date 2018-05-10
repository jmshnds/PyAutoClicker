import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
	keyList.append(char)

def key_check():
	keys = set()
	for key in keyList:
		if wapi.GetAsyncKeyState(ord(key)):
			keys.add(key)
	return keys
