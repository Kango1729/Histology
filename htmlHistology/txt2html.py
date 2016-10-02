#coding:utf-8

'''txtファイルを読む'''
txtName = input('txtFile Name?: ') + ".txt"
txtFile = open(txtName, 'r',encoding = 'utf-8')
txtLines = txtFile.readlines()
txtFile.close()

'''tempファイルを読む'''
tempName = "Template.html" #input('templateName?: ' )
tempFile = open(tempName, 'r',encoding = 'utf-8')
tempLines = tempFile.readlines()
tempFile.close()

'''ベーステンプレート作成'''
TxtDirDis = len(list(txtName.split("/")))
for i in range(len(tempLines)):
    line = tempLines[i]
    if ("<base" == line[:5]):
        TempDirDis = line[i].count("../")
        AddDirNum = TxtDirDis - TempDirDis
        tempLines[i] = line[:line.find("../")] + "../"*AddDirNum + line[line.rfind("../") + 3:]
        break
tempLine = "".join(tempLines)

'''サマリーテンプレート作成'''
for line in tempLines:
    if "<meta class" == line[:11]:
        SummaryTemp = line.split('""')
        break

'''meta descriptionを挿入される部位'''
Summarys = []
Summarys.append(SummaryTemp[0] + "\"")
Summarys.append("\"" + SummaryTemp[1])
Summary = SummaryTemp[0] + '""' + SummaryTemp[1]

'''各行にエスケープシークエンス'''
for i in range(len(txtLines)):
    txtLines[i] = txtLines[i].replace("\"","&quot;")
    txtLines[i] = txtLines[i].replace("<","&lt;")
    txtLines[i] = txtLines[i].replace(">","&gt;")

'''マークアップテンプレート作成'''

for line in tempLines:
    if "<span" == line[:5]:
        markupTemp = line.split("''")
        break

'''マークアップ内の各属性値を属性に挿入される部位'''
TextContents = []
TextContents.append(markupTemp[0] + "\'")
TextContents.append("\'" + markupTemp[1] + "\'")
TextContents.append("\'" + markupTemp[2] + "\'")
TextContents.append("\'" + markupTemp[3])
TextContents.append(markupTemp[4])
TextContent = TextContents[0] + TextContents[1] + TextContents[2] + TextContents[3] + "''" + TextContents[4]

'''各行にマークアップを適応'''
OutputTexts = []
for txtLine in txtLines:
    tags = txtLine.split("#")
    for i in range(1, len(tags), 2):
        datasets = tags[i].split(",")
        tags[i] = TextContents[0] + datasets[0] + TextContents[1] + datasets[1] + TextContents[2] + datasets[2] + TextContents[3] + datasets[1].replace(" ", "_")+ TextContents[4].replace("\n",'')

    OutputTexts.append("".join(tags).replace("\n", "<br>\n").replace("</span>","</span><!--\n-->"))


'''本文以外の部分の作成'''
tempSegs = []
tempSegs.append(tempLine[:tempLine.find(Summary)])
tempSegs.append (tempLine[tempLine.find(Summary) + len(Summary) : tempLine.find(TextContent)])
tempSegs.append(tempLine[tempLine.find(TextContent) + len(TextContent):])


'''
print(tempLine.find(Summary))
print(Summary)
print(tempLine.find(TextContent))
print(TextContent)
'''
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
#print(OutputText)
htmlName = input('htmlFile Name?: ') + ".html"
htmlFile = open(htmlName, 'w', encoding = 'utf-8')
htmlFile.write(OutputText)
htmlFile.flush()
htmlFile.close()
