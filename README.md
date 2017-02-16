## recognize_valid_code
前置工作
-安装**homebrew**
 	终端：ruby -e "$(curl --insecure -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	如果失败
	终端：ruby -e "$(curl --insecure -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
-安装**PIL**
	下载：http://www.pythonware.com/products/pil/index.htm
	解压：tar -xzf Imaging-1.1.7.tar.gz
	cd到：Imaging-1.1.7
	终端：**sudo python setup.py install**
-安装图片支持库
	终端：**brew install libpng**
	终端：**brew install jpeg**
	终端：**brew install libtiff**
-安装**leptonica**
	终端：**brew install leptonica**
-安装**tesseract-ocr**
	终端：**brew install tesseract**
-安装**pip**
	终端：**sudo easy_install pip**
-安装**pytesseract**
	终端：**sudo pip install pytesseract**