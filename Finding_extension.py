dictionary={"py":"python","txt":"text","docx":"Microsoft Word Document","java":"java","pdf":"Acrobat-Portable document format","jpg":"image","jpeg":"image","ppt":"Microsoft Powerpoint Presentation","mp3":"audio file","mp4":"video file"}

name_of_file=input("Enter the name of your file:")
extension=name_of_file.split(".")
x=extension[-1]
print("The extension of your file is:",dictionary.get(x))
