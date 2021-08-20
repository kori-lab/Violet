def run (text: str, optionReturn=False) -> str:
  colorList = {
    
    ("preto", "black") : "\033[1;30m",
    ("vermelho", "red") : "\033[1;31m",
    ("verde", "green") : "\033[1;32m",
		("amarelo", "yellow"): "\033[1;33m",
		("magenta", "magenta"): "\033[1;35m",
		("azul", "blue"): "\033[1;34m",
		("::"): "\033[0;0m",
  
  }
  
  formatString = text
  for cores in colorList.keys():
      if cores == "::": 
        formatString = formatString.replace(f"{cores}", colorList[cores]) + colorList["::"];
      else:
        for cor in cores:
        	formatString = formatString.replace(f":{cor}:", colorList[cores]) + colorList["::"];
  
  if optionReturn:
    print(formatString);
  
  return formatString;

  