# coding : utf-8

#
import os
import psutil
import sys
import shutil


print ("Privet")
name = input ("ваше имя ")
print (name, ", привет")

otvet="W"

while otvet !="q":
	otvet= input ("Хочешь поработать? Y/N/q ")
	if otvet == "Y":
		print("Ok")
		print("___________________________")
		print("1 - Вывести список файлов")
		print("2- Вывести информацию файлов")
		print("3- Вывести информацию о PID")
		print("4- Дублицировать все файлы")
		print("5- Удалить дубликаты файлов")
		print("6- Дублицирование указанного файла")
		print("7- удаление конкретного файла")
		do = int(input ("Укажите действие"))

		if do==1:
			print(os.listdir())
		elif do==2:
			print(os.cpu_count())
		elif do==3:
			print(psutil.pids())
		elif do==4:
			print ("Дублируем")
			file_list = os.listdir()
			i=0
			while i<len(file_list):
				newfile=file_list[i]+'.dupl'
				shutil.copy(file_list[i], newfile)
				i+=1
		elif do==5:
			print ("Удаляем все дубликаты файлов")
			file_list = os.listdir()
			totaldel=0
			i=0
			while i<len(file_list):
				name_file=file_list[i]
				dlina=len(name_file)
				print (dlina)
				print(name_file+ " " + " --------  "+ name_file[dlina-5:dlina])
				if name_file[dlina-5:dlina]==".dupl":
					os.remove (name_file)
					totaldel+=1
				i+=1
			print("Удалено "+ str(totaldel)+ " файлов")
			
		elif do==6:
			print("Дублицирование указанного файла")
			file_list=os.listdir()
			print (file_list)
			vybor = int(input (" Введите номер файла, который хотите дублировать? "))
			newfile=file_list[vybor-1]+'.dupl'
			shutil.copy(file_list[vybor-1], newfile)
		elif do==7:
			print("Удаление конкретного файла")
			file_list=os.listdir()
			print (file_list)
			vybor = int(input (" Введите номер файла, который хотите удалить? "))
			name_file=file_list[vybor-1]
			os.remove(name_file)
			print (name_file+" deleted")
			
	elif otvet == "N":
		print("всего хорошего!")	
	else:
		print("Ошибка ввода. Попробуйте еще раз...")		