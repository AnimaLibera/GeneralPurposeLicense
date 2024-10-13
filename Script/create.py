import yaml
import os

def main():
	content = load_yaml_file("../", "license.yaml")
	print(recursive_print(content))

def load_yaml_file(path, name):
	with open(path + name, "r") as file:
		return yaml.safe_load(file)

def recursive_print(content, text = "", indention = 0, stepsize = 2, paragraph = None):
	headings = " " * indention
	trailing = "" if paragraph is None else f" §{paragraph}"
	term = content["Term"]
	
	text = text + headings + content["Title"] + trailing + os.linesep
	
	#Base Case	
	if isinstance(term, str):
		text = text + headings + term + os.linesep
		if "ListTerm" in content.keys():
			for element in content["ListTerm"]:
				text = text + headings + element + os.linesep
		text = text + os.linesep
	#Recurison Case
	elif isinstance(term, list):
		text = text + os.linesep #Newline after Title before List of Elements
		for index, element in enumerate(term):
			alterd_paragraph = str(index + 1) if paragraph is None else paragraph + "." + str(index + 1)
			text = recursive_print(element, text, indention + stepsize, stepsize, alterd_paragraph)
	#Error Case
	else:
		raise TypeError(f"The Type of {term} is not String or List")
	
	return text

if __name__ == "__main__":
	main()