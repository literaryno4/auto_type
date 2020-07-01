import sys
import os
import re

class auto_type(object):
    """
    This class is used to do some automative work for my part-time job, which is mainly to form a firm format.
    """

    head = "\\documentclass[11pt]{article}\n\\usepackage{CJKutf8}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amsthm,amsfonts,amssymb,amscd}\n\\usepackage{multirow,booktabs}\n\\usepackage[table]{xcolor}\n\\usepackage{fullpage}\n\\usepackage{lastpage}\n\\usepackage{enumitem}\n\\usepackage{fancyhdr}\n\\usepackage{mathrsfs}\n\\usepackage{wrapfig}\n\\usepackage{setspace}\n\\usepackage{calc}\n\\usepackage{multicol}\n\\usepackage{cancel}\n\\usepackage[retainorgcmds]{IEEEtrantools}\n\\usepackage[margin=3cm]{geometry}\n\\usepackage{amsmath}\n\\newlength{\\tabcont}\n\\setlength{\\parindent}{0.0in}\n\\setlength{\\parskip}{0.05in}\n\\usepackage{empheq}\n\\usepackage{framed}\n\\usepackage[most]{tcolorbox}\n\\usepackage{xcolor}\n\\colorlet{shadecolor}{orange!15}\n\\parindent 0in\n\\parskip 12pt\n\\geometry{margin=1in, headsep=0.25in}\n\\theoremstyle{definition}\n\\newtheorem{defn}{Definition}\n\\newtheorem{reg}{Rule}\n\\newtheorem{exer}{Exercise}\n\\newtheorem{note}{Note}\n\\newtheorem*{sol}{Solution}\n\\usepackage{hyperref}\n\\hypersetup{\ncolorlinks=true,\nlinkcolor=blue,\nfilecolor=magenta,\nurlcolor=cyan,\n}\n\\usepackage{float}\n\\begin{document}\n\\begin{CJK*}{UTF8}{gbsn}\n"
    tail = "\\end{CJK*}\n\\end{document}"
    next_line = "\\\\\n"
    pic_path = "/Users/chao/Desktop/pic"

    def __init__(self):
        pic_name = list(filter(lambda x:'.png' in x, os.listdir(auto_type.pic_path)))
        self.pic_name_Q = list(filter(lambda x: 'Q' in x, pic_name))
        self.pic_name_A = list(filter(lambda x: 'A' in x, pic_name))

        try:
            self.file_name = input("请输入文件名：")
        except:
            self.file_name = input("发生错误，请重新输入文件名：")
        
    def write(self):
        """
        write the format to a .tex file
        """

        bango = 1

        ## process pic name
        pic_number_Q = list(map(lambda x: x[(x.index('Q')+1):x.index('.')], self.pic_name_Q))
        pic_number_Q = [x.strip('abcdefghijklmnopqrstuvwxyz\'') for x in pic_number_Q]
        pic_number_A = list(map(lambda x: x[(x.index('A')+1):x.index('.')], self.pic_name_A))
        pic_number_A = [x.strip('abcdefghijklmnopqrstuvwxyz\'') for x in pic_number_A]
        pic_dict_Q = dict(zip(pic_number_Q, self.pic_name_Q))
        pic_dict_A = dict(zip(pic_number_A, self.pic_name_A))

        content_list = []
        with open('testread.txt', 'r') as cf:
            a_string = cf.read()
            content_list = re.split(r"\n\n\n\d*\.\s", a_string)
        print(len(content_list))

        ## open file
        with open(self.file_name, "w") as f:

            ## write head
            f.write(auto_type.head)

            ## write content
            #f.write("content here...\n")
            try:
                num_type = 1
                ## num_type = int(input("enter how many types(4):"))
            except:
                print(sys.exc_info())
                num_type = int(input("发生错误！！！enter how many types(4):"))
            for types in range(num_type):
                #ques_style = input("请输入问题页码和标号风格（例如：P533,Q17-i）：")
                try:
                    #num_question = int(input("请输入题目个数："))
                    num_question = len(content_list)
                except:
                    print(sys.exc_info())
                    num_question = int(input("发生错误!!!！请输入题目个数："))
                try:
                    #num_have_subques = int(input("请输入有小问的题目个数："))
                    num_have_subques = 0
                except:
                    print(sys.exc_info())
                    num_have_subques = int(input("发生错误！！！！请重新输入有小问的题目个数："))

                ## a dict to store the info of subquestion
                subques_dict = {}
                for i in range(num_have_subques):
                    try:
                        ind_subques, num_subques = map(int, input("请输入有小问的题目序号以及相应的小问个数（空格隔开）：").split())
                    except:
                        print(sys.exc_info())
                        ind_subques, num_subques = map(int, input("发生错误！！！！！！请输入有小问的题目序号以及相应的小问个数（空格隔开）：").split())
                    subques_dict[ind_subques] = num_subques

                try:
                    ans_page = int(input("请输入答案起始页码："))
                except:
                    print(sys.exc_info())
                    ans_page = int(input("发生错误！！！！！请输入答案起始页码："))
                try:
                    ans_end_page = int(input("请输入答案结束页码："))
                except:
                    print(sys.exc_info())
                    ans_end_page = int(input("发生错误！！！！！请输入答案结束页码："))
                #ans_style = input("请输入答案标号风格（例如：Q）：")
                #ans_style = 'Q'
                ans_style = 'P'#input("请输入答案页码和标号风格（例如：TP or P）：")

                ans_per_page = (num_question / (ans_end_page - ans_page + 1))
            
                ## begin write content
                for i in range(num_question):
                    content = re.split(r'\ta\.|ANSWER:', content_list[i])
                    ques_type, ques_content = ("选择", ("a." + content[1])) if len(content) == 3 else ("解答", "")
                    num_style = str(i+1) if num_type == 1 else str(i+1) + "(" + str(types) + ")" 
                    f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
                    f.write("题号：" + str(bango) + auto_type.next_line)
                    f.write("题型：" + ques_type + auto_type.next_line)
                    #f.write("题目页码：" + ques_style + num_style + auto_type.next_line)
                    f.write("题目页码：" + ans_style  +str(int(ans_page + i / ans_per_page)) + "," + "Q" + num_style + auto_type.next_line)
                    f.write("题干：" + content[0] + auto_type.next_line)
                    if num_style in pic_dict_Q:
                        f.write('%pic\"' + pic_dict_Q[num_style] + '\"\n')
                    if i+1 in subques_dict:
                        for j in range(subques_dict[i+1]):
                            f.write("题目内容" + str(j+1) + "：" + auto_type.next_line)
                            if num_style + chr(97 + j) in pic_dict_Q:
                                f.write('%pic\"' + pic_dict_Q[num_style + chr(97 + j)] + '\"\n')
                    else:
                        f.write("题目内容：" + ques_content +  auto_type.next_line)
                    f.write("解答页码：" + ans_style  +str(int(ans_page + i / ans_per_page)) + "," + "Q" + num_style + auto_type.next_line)
                    f.write("答案：" + content[-1].replace("\n", "\\\\") + '\n')
                #    if i+1 in subques_dict:
                #        for j in range(subques_dict[i+1] - 1):
                #            f.write(auto_type.next_line)
                    if num_style in pic_dict_A:
                        f.write('%pic\"' + pic_dict_A[num_style] + "\"\n")
                    for asc in range(97, 123):
                        if num_style + chr(asc) in pic_dict_A:
                            f.write('%pic\"' + pic_dict_A[num_style + chr(asc)] + '\"\n')
                    f.write("\n")
                    bango += 1
                print("总共有小题：%d 个" % (bango - num_have_subques + sum(subques_dict.values()) - 1))
                with open('numbers.txt', 'a') as number_f:
                    number_f.write(str(bango - num_have_subques + sum(subques_dict.values()) - 1) + "\n")
                self.subques_dict = {}
                print("This round has done!\n\n\n\n\n")
            f.write(auto_type.tail)
        print("Writing work finished ! <_>")

    def move(self):
        path = "~/Desktop/domywork/" + self.file_name.replace(".tex", "")
        os.system("mkdir " + path)
        if os.listdir(auto_type.pic_path) == ['.DS_Store']:
            pass
        else:
            os.system("mkdir " + path + "/pic")
            os.system("mv " + auto_type.pic_path + "/*.png " + path + "/pic")
        os.system("vim -S auto_replace.vim " + self.file_name)
        os.system("mv *.tex " + path)
        os.system("open " + path + "/" + self.file_name)
        print("Moving work done! .tex 文件被移动到 " + path)

auto_typer = auto_type()
auto_typer.write()
auto_typer.move()
