import os,sys
from random import choice

extensionList = ['.doc','.docx','.log','.msg','.odt','.pages','.rtf','.tex','.wpd','.wps','.csv','.dat','.gbr','.ged','.ibooks','.key','.keychain','.pps','.ppt','.pptx','.sdf','.tar','.tar','.tax2012','.vcf','.xml','.3g2','.3gp','.asf','.asx','.avi','.flv','.m4v','.mov','.mp4','.mpg','.rm','.srt','.swf','.vob','.wmv','.3dm','.3ds','.max','.obj','.bmp','.dds','.gif','.jpg','.png','.psd','.pspimage','.tga','.thm','.tif','.tiff','.yuv','.ai','.eps','.ps','.svg','.indd','.pct','.pdf','.xlr','.xls','.xlsx','.accdb','.db','.dbf','.mdb','.pdb','.sql','.apk','.app','.bat','.cgi','.com','.exe','.gadget','.jar','.pif','.vb','.wsf','.dem','.gam','.nes','.rom','.sav','.dwg','.dxf','.gpx','.kml','.kmz','.asp','.aspx','.cer','.cfm','.csr','.css','.htm','.html','.js','.jsp','.php','.rss','.xhtml','.crx','.plugin','.fnt','.fon','.otf','.ttf','.cab','.cpl','.cur','.deskthemepack','.dll','.dmp','.drv','.icns','.ico','.lnk','.sys','.cfg','.ini','.prf','.hqx','.mim','.uue','.7z','.cbr','.deb','.gz','.pkg','.rar','.rpm','.sitx','.tar.gz','.zip','.zipx','.bin','.cue','.dmg','.iso','.mdf','.toast','.vcd','.c','.class','.cpp','.cs','.dtd','.fla','.h','.java','.lua','.m','.pl','.sh','.sln','.vcxproj','.xcodeproj','.bak','.tmp','.crdownload','.ics','.msi','.part','.torrent']


folderName = raw_input('Please enter the directory name: ')

folder = folderName
for filename in os.listdir(folder):
       randomExtension = choice(extensionList)
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       fileExtensionName = os.path.splitext(filename)[1]
       newname = infilename.replace(fileExtensionName, randomExtension)
       output = os.rename(infilename, newname)
