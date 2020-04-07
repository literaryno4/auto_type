import sys
import os

## prepare work
head = "\\documentclass[11pt]{article}\n\\usepackage{CJKutf8}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amsthm,amsfonts,amssymb,amscd}\n\\usepackage{multirow,booktabs}\n\\usepackage[table]{xcolor}\n\\usepackage{fullpage}\n\\usepackage{lastpage}\n\\usepackage{enumitem}\n\\usepackage{fancyhdr}\n\\usepackage{mathrsfs}\n\\usepackage{wrapfig}\n\\usepackage{setspace}\n\\usepackage{calc}\n\\usepackage{multicol}\n\\usepackage{cancel}\n\\usepackage[retainorgcmds]{IEEEtrantools}\n\\usepackage[margin=3cm]{geometry}\n\\usepackage{amsmath}\n\\newlength{\\tabcont}\n\\setlength{\\parindent}{0.0in}\n\\setlength{\\parskip}{0.05in}\n\\usepackage{empheq}\n\\usepackage{framed}\n\\usepackage[most]{tcolorbox}\n\\usepackage{xcolor}\n\\colorlet{shadecolor}{orange!15}\n\\parindent 0in\n\\parskip 12pt\n\\geometry{margin=1in, headsep=0.25in}\n\\theoremstyle{definition}\n\\newtheorem{defn}{Definition}\n\\newtheorem{reg}{Rule}\n\\newtheorem{exer}{Exercise}\n\\newtheorem{note}{Note}\n\\newtheorem*{sol}{Solution}\n\\usepackage{hyperref}\n\\hypersetup{\ncolorlinks=true,\nlinkcolor=blue,\nfilecolor=magenta,\nurlcolor=cyan,\n}\n\\usepackage{float}\n\\begin{document}\n\\begin{CJK*}{UTF8}{gbsn}\n"
tail = "\\end{CJK*}\n\\end{document}"

file_name = input("请输入文件名：")
num_question = int(input("请输入题目个数："))
num_have_subques = int(input("请输入有小问的题目个数"))
ques_style = input("请输入问题页码和标号风格（例如：P533,Q17-i）：")
ans_style = input("请输入答案页码和标号风格（例如：P533,A17-i）：")
next_line = "\\\\\n"

## a dict to store the info of subquestion
subques_dict = {}
for i in range(num_have_subques):
    ind_subques, num_subques = map(int, input("请输入有小问的题目序号以及相应的小问个数（空格隔开）：").split())
    subques_dict[ind_subques] = num_subques


## open file
f = open(file_name, "a")

## write head
f.write(head)

## write content
#f.write("content here...\n")
## begin write content
for i in range(num_question):
    f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    f.write("题号：" + str(i+1) + next_line)
    f.write("题型：解答" + next_line)
    f.write("题目页码：" + ques_style + str(i+1) + next_line)
    f.write("题干：" + next_line)
    if i+1 in subques_dict:
        for j in range(subques_dict[i+1]):
            f.write("题目内容" + str(j+1) + "：" + next_line)
    else:
        f.write("题目内容：" + next_line)
    f.write("解答页码：" + ans_style + str(i+1) + next_line)
    f.write("答案：" + next_line)
    if i+1 in subques_dict:
        for j in range(subques_dict[i+1] - 1):
            f.write(next_line)
    f.write("\n")

## write tail
f.write(tail)

## close file
f.close()
