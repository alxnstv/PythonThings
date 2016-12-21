import os, sys, hashlib, unicodedata
from unidecode import unidecode

reload(sys)  
sys.setdefaultencoding('utf8')

block_size = 65536
path = "C:\\Users\\anastev\\Downloads"

def calculate_hash(path):
	file = open(path, 'rb') #rb = read+write mode/binary
	md5_hasher = hashlib.md5()
	binary_data = file.read(block_size)
	
	while len(binary_data)>0:
		md5_hasher.update(binary_data)
		binary_data = file.read(block_size)
	file.close()
	return md5_hasher.hexdigest()

def spot_duplicates(folder):
	hashlist = {}
	duplicates = []
	for file in os.listdir(folder):
		hashcontent = []
		path = os.path.join(folder, file)
		path = path.decode('latin1')
   
		file_hash = calculate_hash(path)
		print(file_hash)

		if file_hash not in hashlist.iterkeys():
		   hashlist[file_hash] = 1
		else :
		   hashlist[file_hash]+= 1
		   
		if hashlist[file_hash] > 1 :
			duplicates.append(path)
	
	#DEBUG	
	for e in duplicates:
		print("DEBUG duplicates: %r"%e)
	return duplicates
		
if __name__ == '__main__':
	duplicates_list = spot_duplicates(path)
	proceed = raw_input("Would you like to delete duplicate files?")
	print(proceed)
	if proceed == 'yes':
		for d in duplicates_list:
			os.remove(d)
	else:
		sys.exit(0)

