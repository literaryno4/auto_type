import sys
import os

class auto_type(object):
    """
    This class is used to do some automative work for my part-time job, which is mainly to form a firm format.
    """

    head = "\\documentclass[11pt]{article}\n\\usepackage{CJKutf8}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amsthm,amsfonts,amssymb,amscd}\n\\usepackage{multirow,booktabs}\n\\usepackage[table]{xcolor}\n\\usepackage{fullpage}\n\\usepackage{lastpage}\n\\usepackage{enumitem}\n\\usepackage{fancyhdr}\n\\usepackage{mathrsfs}\n\\usepackage{wrapfig}\n\\usepackage{setspace}\n\\usepackage{calc}\n\\usepackage{multicol}\n\\usepackage{cancel}\n\\usepackage[retainorgcmds]{IEEEtrantools}\n\\usepackage[margin=3cm]{geometry}\n\\usepackage{amsmath}\n\\newlength{\\tabcont}\n\\setlength{\\parindent}{0.0in}\n\\setlength{\\parskip}{0.05in}\n\\usepackage{empheq}\n\\usepackage{framed}\n\\usepackage[most]{tcolorbox}\n\\usepackage{xcolor}\n\\colorlet{shadecolor}{orange!15}\n\\parindent 0in\n\\parskip 12pt\n\\geometry{margin=1in, headsep=0.25in}\n\\theoremstyle{definition}\n\\newtheorem{defn}{Definition}\n\\newtheorem{reg}{Rule}\n\\newtheorem{exer}{Exercise}\n\\newtheorem{note}{Note}\n\\newtheorem*{sol}{Solution}\n\\usepackage{hyperref}\n\\hypersetup{\ncolorlinks=true,\nlinkcolor=blue,\nfilecolor=magenta,\nurlcolor=cyan,\n}\n\\usepackage{float}\n\\begin{document}\n\\begin{CJK*}{UTF8}{gbsn}\n"
    tail = "\\end{CJK*}\n\\end{document}"
    next_line = "\\\\\n"
    pic_path = "/Users/chao/Desktop/pic/"

    def __init__(self):
        pic_name = list(filter(lambda x:'.png' in x, os.listdir(auto_type.pic_path)))
        self.pic_name_Q = list(filter(lambda x: 'Q' in x, pic_name))
        self.pic_name_A = list(filter(lambda x: 'A' in x, pic_name))
        try:
            self.file_name = input("请输入文件名：")
        except:
            self.file_name = input("发生错误，请重新输入文件名：")
        self.ques_style = input("请输入问题页码和标号风格（例如：P533,Q17-i）：")
        try:
            self.num_question = int(input("请输入题目个数："))
        except:
            print(sys.exc_info())
            self.num_question = int(input("发生错误!!!！请输入题目个数："))
        try:
            self.num_have_subques = int(input("请输入有小问的题目个数："))
        except:
            print(sys.exc_info())
            self.num_have_subques = int(input("发生错误！！！！请重新输入有小问的题目个数："))

        ## a dict to store the info of subquestion
        self.subques_dict = {}
        for i in range(self.num_have_subques):
            try:
                ind_subques, num_subques = map(int, input("请输入有小问的题目序号以及相应的小问个数（空格隔开）：").split())
            except:
                print(sys.exc_info())
                ind_subques, num_subques = map(int, input("发生错误！！！！！！请输入有小问的题目序号以及相应的小问个数（空格隔开）：").split())
            self.subques_dict[ind_subques] = num_subques

        self.ans_page = int(input("请输入答案起始页码："))
        ans_end_page = int(input("请输入答案结束页码："))
        #self.ans_style = input("请输入答案标号风格（例如：Q）：")
        self.ans_style = 'Q'
        self.ans_per_page = (self.num_question // (ans_end_page - self.ans_page))

    def write(self):
        """
        write the format to a .tex file
        """
        ## process pic name
        pic_number_Q = list(map(lambda x: x[(x.index('Q')+1):x.index('.')], self.pic_name_Q))
        pic_number_Q = list(map(int, [x.strip('abcdefghijklmnopqrstuvwxyz') for x in pic_number_Q]))
        pic_number_A = list(map(lambda x: x[(x.index('A')+1):x.index('.')], self.pic_name_A))
        pic_number_A = list(map(int, [x.strip('abcdefghijklmnopqrstuvwxyz') for x in pic_number_A]))
        pic_dict_Q = dict(zip(pic_number_Q, pic_name_Q))
        pic_dict_A = dict(zip(pic_number_A, pic_name_A))

        
        ## open file
        with open(self.file_name, "w") as f:

            ## write head
            f.write(auto_type.head)

            ## write content
            #f.write("content here...\n")
            ## begin write content
            for i in range(self.num_question):
                f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
                f.write("题号：" + str(i+1) + auto_type.next_line)
                f.write("题型：解答" + auto_type.next_line)
                f.write("题目页码：" + self.ques_style + str(i+1) + auto_type.next_line)
                f.write("题干：" + auto_type.next_line)
                if i+1 in pic_dict_Q:
                    f.write('\%' + pic_dict_Q[i+1])
                if i+1 in self.subques_dict:
                    for j in range(self.subques_dict[i+1]):
                        f.write("题目内容" + str(j+1) + "：" + auto_type.next_line)
                else:
                    f.write("题目内容：" + auto_type.next_line)
                f.write("解答页码：" + "P" +str(self.ans_page + i // self.ans_per_page) + "," + self.ans_style + str(i+1) + auto_type.next_line)
                f.write("答案：\n") #+ auto_type.next_line)
            #    if i+1 in subques_dict:
            #        for j in range(subques_dict[i+1] - 1):
            #            f.write(auto_type.next_line)
                if i+1 in pic_dict_A:
                    f.write('%' + pic_dict_A[i+1])
                f.write("\n")

            ## write tail
            f.write(auto_type.tail)
        print("Writing work finished ! <_>")
        print("Next, move the .tex file...")

    def move(self):
        os.system("mkdir ~/Desktop/第五周/" + self.file_name.replace(".tex", ""))
        os.system("mkdir ~/Desktop/第五周/" + self.file_name.replace(".tex", "") + "/pic")
        os.system("mv *.tex ~/Desktop/第五周/" + self.file_name.replace(".tex", ""))

auto_typer = auto_type()
auto_typer.write()
auto_typer.move()
