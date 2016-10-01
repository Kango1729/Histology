#coding:utf-8

'''txtファイルを読む'''
txtName = input('txtFile Name?: ') + ".txt"
txtFile = open(txtName, 'r',encoding = 'utf-8')
txtLines = txtFile.readlines()
txtFile.close()

'''各行にエスケープシークエンス'''
for i in range(len(txtLines)):
    txtLines[i] = txtLines[i].replace("\"","&quot;")
    txtLines[i] = txtLines[i].replace("<","&lt;")
    txtLines[i] = txtLines[i].replace(">","&gt;")



'''マークアップ内の各属性値を属性に挿入される部位'''
TextContents = []
TextContents.append("<span class = \'form\' data-jp = \'")
TextContents.append("\' data-eng =\'")
TextContents.append("\' data-hide = \'")
TextContents.append("\' data-link = \'Dict/")
TextContents.append(".html\'>  </span>")
TextContent = "".join(TextContents)


'''各行にマークアップを適応'''
OutputTexts = []
for txtLine in txtLines:
    tags = txtLine.split("#")
    for i in range(1, len(tags), 2):
        datasets = tags[i].split(",")
        tags[i] = TextContents[0] + datasets[0] + TextContents[1] + datasets[1] + TextContents[2] + datasets[2] + TextContents[3] + datasets[1].replace(" ", "_")+ TextContents[4]

    OutputTexts.append("".join(tags).replace("\n", "<br>\n").replace("</span>","</span>\n"))

'''tempファイルを読む'''
tempName = "Template.html" #input('templateName?: ' )
tempFile = open(tempName, 'r',encoding = 'utf-8')
tempLines = "".join(tempFile.readlines())
tempFile.close()

'''meta descriptionを挿入される部位'''
Summarys = []
Summarys.append("<meta class = \'description\' content = \"")
Summarys.append("\" onload = \'ReadMode(&quot;description&quot;)'>")
Summary = "".join(Summarys)

'''本文以外の部分の作成'''
tempSegs = []
tempSegs.append(tempLines[:tempLines.find(Summary)])
tempSegs.append (tempLines[tempLines.find(Summary) + len(Summary) : tempLines.find(TextContent)])
tempSegs.append(tempLines[tempLines.find(TextContent) + len(TextContent):])

'''
print("tempSegs[0]\n\n" +tempSegs[0] +"\n-----")
print("Summarys[0]\n\n"+Summarys[0]+"\n-----")
print("OutputTexts[0]\n\n"+OutputTexts[0]+"\n-----")
print("Summarys[1]\n\n"+Summarys[1]+"\n-----")
print("tempSegs[1]\n\n"+tempSegs[1]+"\n-----")
print("OutputTexts\n\n"+"".join(OutputTexts)+"\n-----")
print("tempSegs[2]\n\n"+tempSegs[2]+"\n-----")
'''


'''出力を作成'''
OutputText = "".join([tempSegs[0], Summarys[0], OutputTexts[0], Summarys[1], tempSegs[1], "".join(OutputTexts),  tempSegs[2]])

'''cmdとhtmlファイルに出力'''
print(OutputText)
htmlName = input('htmlFile Name?: ') + ".html"
htmlFile = open(htmlName, 'w', encoding = 'utf-8')
htmlFile.write(OutputText)
htmlFile.flush()
htmlFile.close()
