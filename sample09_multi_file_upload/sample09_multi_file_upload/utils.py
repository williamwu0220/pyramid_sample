class FileIO:
	'''
    objFIO = utils.FileIO()
    objFIO.output_file('save_sql.txt', sql % sql_params)
    objFIO.output_file('save_test.txt', 'test_message')
    '''
	def __init__(self):
		pass

	def output_file(self, str_file_name, str_file_content):
		'產出檔案以儲存輸出內容'
		outf = open(str_file_name, 'w', encoding = 'UTF-8')
		outf.write(str_file_content)
		outf.close()

class ImageFileUpload:

	def __init__(self):
		pass

	def upload_files(self, file_files, int_one_file=1, str_new_name='', int_max_wsize=0, str_thumb='_std', str_up_dir='posimage'):
		import os
		# 影像處理函式庫
		from PIL import Image
		# 解析專案目錄絕對路徑
		from pyramid.path import AssetResolver

		static_path = AssetResolver().resolve('sample09_multi_file_upload:static/{0}'.format(str_up_dir)).abspath()

		# 若 int_one_file 等於 0，表示為多檔上傳，變更檔名參數強制取消，一律以原檔名儲存
		if int_one_file == 0:
			str_new_name = ''
				
		list_saved_files = []

		for temp_file in file_files:
			# 若無任何上傳檔案，傳回空的 list_saved_files
			if hasattr(temp_file, 'filename') is False:
				return list_saved_files

			if(int_one_file == 1 and str_new_name != ''):
				each_file = os.path.join(static_path, str_new_name + temp_file.filename[-4:])
			else:
				each_file = os.path.join(static_path, temp_file.filename)

			temp_file.file.seek(0)
			with open(each_file, 'wb') as save_file:
				# 限制每次讀寫檔案區段大小(5MB)，以免檔案太大，一次全部讀取造成記憶體不足
				while True:
					content = temp_file.file.read(5120000)
					if not content:
						break
					save_file.write(content)
		   
			# 產生縮圖
			if str_thumb != '':
				thumb_file = each_file[:-4] + str_thumb + each_file[-4:]
			else:
				thumb_file = each_file[:-4] + '_thumb' + each_file[-4:]

			with open(thumb_file, 'wb') as out_file:
				im = Image.open(each_file)
				# 設定縮圖大小並回值長寬值
				int_src_wsize, int_src_hsize = im.size 
				tuple_new_size = self.resize_file(int_src_wsize, int_src_hsize, int_max_wsize) 

				# 使用優良畫質
				im.thumbnail(tuple_new_size, Image.ANTIALIAS) 

				# 依副檔名指定縮圖存檔格式參數
				if thumb_file[-3:].upper() == "PNG":
					im.save(out_file, "PNG")
				elif thumb_file[-3:].upper() == "JPG":
					im.save(out_file, "JPEG")

			# 儲存檔名，前面加上指定資料夾 str_up_dir (如：posimage)
			list_saved_files.append((str_up_dir + '\\' + each_file.split('\\')[-1], str_up_dir + '\\' + thumb_file.split('\\')[-1]))

		#若無上傳儲存任何檔案，則傳回空字串；一個檔案則傳回單一檔名；多個檔案則傳回 list
		if(len(list_saved_files) == 0):
			return ''
		elif(int_one_file==1 and len(list_saved_files) == 1):
			return list_saved_files[0][1]
		else:	
			return list_saved_files

	def resize_file(self, int_std_wsize, int_std_hsize, int_max_wsize):
		'''
		若 int_max_wsize 等於 0，或 int_std_wsize 已經小於 int_max_wsize，則縮圖大小為原尺寸
		否則依限制最大寬度 int_max_wsize 為基準，計算縮圖應有尺寸
		'''
		if int_max_wsize > 0 and int_std_wsize > int_max_wsize:
			int_std_hsize = int_std_hsize / (int_std_wsize / int_max_wsize)
			int_std_wsize = int_max_wsize

		return (int_std_wsize, int_std_wsize)



