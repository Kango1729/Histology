#coding:utf-8

txtName = input('txtFile Name?: ') + ".txt"
txtFile = open(txtName, 'r',encoding = 'utf-8')
txtLines = txtFile.readlines()
txtFile.close()
OutputTexts = []

tempName = "Template.html" #input('templateName?: ' )
tempFile = open(tempName, 'r',encoding = 'utf-8')
tempLines = "".join(tempFile.readlines())
tempFile.close()

Summarys = []
Summarys.append("<meta class = \'description\' content = \"")
Summarys.append("\" onload = \'ReadMode(&quot;description&quot;)'>")
Summary = "".join(Summarys)

TextContents = []
TextContents.append("<span class = \'form\' data-answer = \'")
TextContents.append("\' data-eng =\'")
TextContents.append("\' data-hide = \'")
TextContents.append("\' data-link = \'Dict/")
TextContents.append("\'>  </span>")
TextContent = "".join(TextContents)

tempSegs = []
tempSegs.append(tempLines[:tempLines.find(Summary)])
tempSegs.append (tempLines[tempLines.find(Summary) + len(Summary) : tempLines.find(TextContent)])
tempSegs.append(tempLines[tempLines.find(TextContent) + len(TextContent):])

for txtLine in txtLines:
    tags = txtLine.split("#")
    for i in range(1, len(tags), 2):
        datasets = tags[i].split(",")
        tags[i] = TextContents[0] + datasets[0] + TextContents[1] + datasets[1] + TextContents[2] + datasets[2] + TextContents[3] + datasets[1].replace(" ", "_")+ TextContents[4]

    OutputTexts.append("".join(tags).replace("\n", "<br>\n").replace("</span>","</span>\n"))


    OutputText = "".join([tempSegs[0], Summarys[0], OutputTexts[0], Summarys[1], tempSegs[1], "".join(OutputTexts),  tempSegs[2]])

print(OutputText)
htmlName = input('htmlFile Name?: ') + ".html"
htmlFile = open(htmlName, 'w', encoding = 'utf-8')
htmlFile.write(OutputText)
htmlFile.flush()
htmlFile.close()
