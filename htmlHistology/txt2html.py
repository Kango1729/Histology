#coding:utf-8

txtName = input('txtFile Name?: ') + ".txt"
txtFile = open(txtName, 'r',encoding = 'utf-8')
txtLines = txtFile.readlines()
txtFile.close()
OutputText = []
for txtLine in txtLines:
    tags = txtLine.split("#")
    for i in range(1, len(tags), 2):
        datasets = tags[i].split(",")
        tags[i] = "<span class = 'form' data-answer = '" + datasets[0] + "' data-eng ='" + datasets[1] + "' data-hide = '" + datasets[2] + "' data-link = 'Text/Dict/" + datasets[1] + "'>  </span>"
    OutputText.append("".join(tags))

templateName = "Template.html" #input('templateName?: ' )
templateFile = open(templateName, 'r',encoding = 'utf-8')
templateLines = "".join(templateFile.readlines())
templateFile.close()


templateFront = templateLines[:templateLines.find("<span")]
templateBack = templateLines[templateLines.find("</span>") + 7:]

OutputLine = templateFront + "".join(OutputText).replace("\n", "<br>\n") + templateBack
print(OutputLine)

htmlName = input('htmlFile Name?: ') + ".html"
htmlFile = open(htmlName, 'w', encoding = 'utf-8')
htmlFile.write(OutputLine)
htmlFile.flush()
htmlFile.close()
