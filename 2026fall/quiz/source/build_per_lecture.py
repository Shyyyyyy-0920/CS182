"""Build per-lecture question papers, editable answer copies, and solutions.

Quiz.tex is a personal answer file: it is created once and NEVER overwritten.
All question/solution content comes from L01.json ... L07.json in this folder.
"""
from pathlib import Path
import argparse
import json
import random
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--lesson', help='Build just one lecture, e.g. 07')
args = parser.parse_args()

PREAMBLE = r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern,array,amsmath,amssymb,booktabs,enumitem,fancyhdr,lastpage,needspace,microtype}
\usepackage[margin=19mm,headheight=14pt,footskip=11mm]{geometry}
\usepackage[hidelinks]{hyperref}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\setlength{\emergencystretch}{2em}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small CS182 --- Lecture LECTUREID}
\fancyhead[R]{\small DOCUMENTLABEL}
\fancyfoot[L]{\small Independent practice quiz}
\fancyfoot[R]{\small Page \thepage\ of \pageref{LastPage}}
\newcommand{\SetAnswer}[2]{\expandafter\gdef\csname QuizAnswer#1\endcsname{#2}}
\newcommand{\GetAnswer}[1]{\csname QuizAnswer#1\endcsname}
\newlength{\BlankAnswerHeight}\setlength{\BlankAnswerHeight}{16mm}
\newcommand{\AnswerBlank}{\leavevmode\par\vspace{\BlankAnswerHeight}}
'''

def md(s):
    return s.replace(r'\(', '$').replace(r'\)', '$').replace(r'\[','\n$$\n').replace(r'\]','\n$$\n')

def block(s):
    return r'\par\noindent\begin{minipage}{\linewidth}'+'\n'+s+'\n'+r'\end{minipage}\par\vspace{3mm}'+'\n'

def source_tex(s):
    return r'{\footnotesize\textit{Source: '+s.replace('_',r'\_')+'.}}'

def grid(start, count, kind, values=None):
    out=[]
    for a in range(start,start+count,6):
        ns=list(range(a,min(a+6,start+count)))
        out += [r'\begin{center}\renewcommand{\arraystretch}{1.15}\begin{tabular}{|'+'c|'*len(ns)+'}',r'\hline', ' & '.join(map(str,ns))+r'\\\hline']
        cells=[]
        for n in ns:
            value=values[n-start] if values is not None else r'\GetAnswer{'+kind+f'{n:02}'+'}'
            cells.append(r'\makebox[20mm]{\rule{0pt}{5mm}'+value+'}')
        out += [' & '.join(cells)+r'\\\hline',r'\end{tabular}\end{center}']
    return '\n'.join(out)+'\n'

def config_tex(data):
    out=[r'''% 本文件为独立可填写答题卷；用 pdfLaTeX 编译两次。
% 在 BEGIN TF ANSWERS 和 BEGIN MC ANSWERS 中填写短答案。
% 大题请搜索 BEGIN ANSWER Q25(a) 等注释；每个小问都有独立区域。
% 写完小问后删除该处的 \AnswerBlank，或将 BlankAnswerHeight 改为 0mm。
% 所有打印内容及你填写的回答请使用英文。中文只出现在源文件注释中。
% build_per_lecture.py 不会覆盖已经存在的 Quiz.tex，以保留你的作答。
% BEGIN STUDENT INFO / 个人信息
\newcommand{\StudentName}{}
\newcommand{\StudentID}{}
% END STUDENT INFO
% BEGIN TF ANSWERS / 判断题答题区（第二组花括号填 T 或 F）''']
    out += [f'\\SetAnswer{{TF{n:02}}}{{}} % Question {n}' for n in range(1,13)]
    out += ['% END TF ANSWERS','% BEGIN MC ANSWERS / 不定项选择答题区（填选项字母，如 BD；仅格式示例）']
    out += [f'\\SetAnswer{{MC{n:02}}}{{}} % Question {n}' for n in range(13,25)]
    out += ['% END MC ANSWERS','']
    return '\n'.join(out)

def cover_tex(d,solution,keys):
    title='Worked Solutions and Marking Guide' if solution else 'Lecture Quiz and Answer Copy'
    s=r'\begin{center}{\Large\bfseries CS182: Introduction to Machine Learning}\par{\Large\bfseries Lecture '+d['id']+': '+d['title']+r'}\par{\large '+title+r'}\end{center}'+'\n'
    s+=r'\textbf{Scope:} '+d['pdf'].replace('_',r'\_')+r'. Independent practice material based on the official 2026 Fall lecture.\par\textbf{Total:} 100 marks. \quad \textbf{Suggested time:} 120 minutes.'+'\n'
    if not solution:
        s+=r'\par\textbf{Name:} \underline{\makebox[60mm][l]{\StudentName}}\hfill\textbf{Student ID:} \underline{\makebox[45mm][l]{\StudentID}}'+'\n'
    s+=r'''\begin{center}\begin{tabular}{lrrr}\toprule
Section & Questions & Each & Marks\\\midrule
A. Misconceptions: True/False & 12 & 1 & 12\\
B. Multiple response & 12 & 2 & 24\\
C. Proofs and formula derivations & 4 & 10 & 40\\
D. Applications & 2 & 12 & 24\\\midrule
Total & 30 & & 100\\\bottomrule\end{tabular}\end{center}
\textbf{Scoring.} In Section B each item has exactly four options, of which one,
two, or three are correct. The complete correct set earns 2 marks; a nonempty
proper subset earns 1 mark; any incorrect option or no selection earns 0.
T/F answers earn 1 mark only when correct. Show reasoning in Sections C and D;
part marks are available for valid intermediate work. Equivalent correct methods receive credit.
\par\medskip\textbf{Instructions.} Answer in English. Use natural logarithms.
Exact values and justified approximations are accepted. All vectors are columns
unless stated otherwise. Use local assumptions, label conventions, and tie rules.
'''
    s+=r'\par\medskip\textbf{'+('Quick key' if solution else 'Answer sheet')+' --- Section A}\n'
    s+=grid(1,12,'TF',['T' if q['answer'] else 'F' for q in d['tf']] if solution else None)
    s+=r'\par\medskip\textbf{'+('Quick key' if solution else 'Answer sheet')+' --- Section B}\n'
    s+=grid(13,12,'MC',keys if solution else None)
    return s

def validate(d):
    assert len(d['tf'])==12 and len(d['mc'])==12 and len(d['long'])==6,d['id']
    assert [q['kind'] for q in d['long']]==['proof']*4+['application']*2
    assert [q['marks'] for q in d['long']]==[10]*4+[12]*2
    for q in d['mc']:
        assert len(q['options'])==4 and 1<=sum(o['correct'] for o in q['options'])<=3
        assert all(o['why'].strip() for o in q['options'])
    for q in d['long']:
        assert sum(p['marks'] for p in q['parts'])==q['marks']
        assert all(p['question'].strip() and p['solution'].strip() for p in q['parts'])
    assert 12+24+sum(q['marks'] for q in d['long'])==100
    def strings(v):
        if isinstance(v,str):yield v
        elif isinstance(v,dict):
            for x in v.values():yield from strings(x)
        elif isinstance(v,list):
            for x in v:yield from strings(x)
    for s in strings(d):
        assert s.count(r'\(')==s.count(r'\)'),(d['id'],s)
        assert s.count(r'\[')==s.count(r'\]'),(d['id'],s)

def arrange(d):
    rng=random.Random(182000+int(d['id']))
    rng.shuffle(d['tf']);rng.shuffle(d['mc'])
    # Keep options unpredictable but reasonably distributed across letters.
    for attempt in range(10000):
        opts=[]
        for q in d['mc']:
            a=q['options'].copy();rng.shuffle(a);opts.append(a)
        keys=[''.join(chr(65+j) for j,o in enumerate(a) if o['correct']) for a in opts]
        count=Counter(''.join(keys))
        if len(count)==4 and max(count.values())-min(count.values())<=3 and all(keys[j]!=keys[j+1] for j in range(11)):
            for q,a in zip(d['mc'],opts):q['options']=a
            return keys,dict(sorted(count.items()))
    raise ValueError('Could not shuffle option sets: '+d['id'])

def render_tex(d,keys,solution=False):
    out=PREAMBLE.replace('LECTUREID',d['id']).replace('DOCUMENTLABEL','Solutions' if solution else 'Personal answer copy')
    if not solution:out+=config_tex(d)
    out+='\n'+r'\begin{document}'+'\n'+cover_tex(d,solution,keys)
    out+=r'\newpage\section*{Section A. True/False'+(' --- Explanations' if solution else r' \hfill 12 marks')+'}\n'
    for n,q in enumerate(d['tf'],1):
        body=r'\textbf{'+str(n)+'.} '+(r'\textbf{'+('True.' if q['answer'] else 'False.')+'} '+q['explanation'] if solution else q['statement'])
        if solution:body+='\n\n'+source_tex(q['source'])
        out+=block(body)
    for start in range(0,12,4):
        out+=r'\newpage\section*{Section B. Multiple Response'+(' --- Explanations' if solution else r' \hfill 24 marks')+'}\n'
        if not solution:out+=r'\textit{Select all correct options. Each question has 1--3 correct options.}\par'+'\n'
        for idx,q in enumerate(d['mc'][start:start+4],start):
            n=idx+13
            body=f'% BEGIN QUESTION Q{n} / 题目与选项区\n'+r'\textbf{'+str(n)+'.} '+(r'\textbf{Correct set: '+', '.join(keys[idx])+'.}' if solution else q['stem'])+'\n'
            body+=r'\begin{enumerate}[label=(\Alph*),leftmargin=8mm,itemsep=2pt,topsep=2pt]'+'\n'
            for o in q['options']:
                body+=r'\item '+((r'\textbf{'+('Correct.' if o['correct'] else 'Incorrect.')+'} '+o['why']) if solution else o['text'])+'\n'
            body+=r'\end{enumerate}'+'\n'
            if solution:body+=source_tex(q['source'])+'\n'
            body+=f'% END QUESTION Q{n}\n'
            out+=block(body)
    for n,q in enumerate(d['long'],25):
        section='C. Proofs and Formula Derivations' if q['kind']=='proof' else 'D. Applications'
        out+=r'\newpage\section*{Section '+section+'}\n'+r'\textbf{'+str(n)+'. '+q['title']+r'}\hfill\textbf{['+str(q['marks'])+' marks]}'+r'\par\medskip'+'\n'
        # The problem setup may be stored either as a stem or in the first part.
        if q.get('stem'):out+=q['stem']+'\n\n'
        if solution:
            for j,p in enumerate(q['parts']):
                out+=r'\textbf{('+chr(97+j)+') ['+str(p['marks'])+' marks]} '+p['solution']+'\n\n'
            out+=r'\textit{Marking: use the displayed subpart allocations; award credit for the logical or numerical intermediate steps.}\par'+'\n'+source_tex(q['source'])+'\n'
        else:
            out+=r'\begin{enumerate}[label=(\alph*),leftmargin=8mm,itemsep=3pt]'+'\n'
            for p in q['parts']:out+=r'\item '+p['question']+r'\hfill\textbf{['+str(p['marks'])+(' mark' if p['marks']==1 else ' marks')+']}\n'
            out+=r'\end{enumerate}\par\medskip\hrule\medskip\textbf{Student response}\par'+'\n'
            out+=f'% BEGIN ANSWER Q{n} / 第{n}题答题区\n'+r'\begin{enumerate}[label=(\alph*),leftmargin=8mm,itemsep=3pt]'+'\n'
            for j,p in enumerate(q['parts']):
                tag=f'Q{n}({chr(97+j)})'
                out+=r'\item'+'\n'+f'% >>> BEGIN ANSWER {tag}\n% 在这里写英文推导或证明；完成后可删除下方空白占位命令。\n'+r'\AnswerBlank'+'\n'+f'% <<< END ANSWER {tag}\n'
            out+=r'\end{enumerate}'+'\n'+f'% END ANSWER Q{n}\n'
    if solution:
        out+=r'\newpage\section*{Lecture Alignment and Coverage}'+'\n'
        out+=r'Primary source: \texttt{'+d['pdf'].replace('_',r'\_')+r'} in \texttt{E:\textbackslash CS182\textbackslash 2026fall\textbackslash lecture}. All PDF pages count the cover as page 1. Additional arguments are marked as supplementary derivations when appropriate. These are original practice questions, not copied homework questions.'+'\n\n'
        for name,items,start in [('T/F',d['tf'],1),('Multiple response',d['mc'],13),('Proofs and applications',d['long'],25)]:
            out+=r'\textbf{'+name+'}\n'+r'\begin{description}[leftmargin=12mm,itemsep=1pt]'+'\n'
            for n,q in enumerate(items,start):out+=r'\item['+str(n)+'] '+q['source'].replace('_',r'\_')+'.\n'
            out+=r'\end{description}'+'\n'
    return out+r'\end{document}'+'\n'

def render_md(d,keys,solution=False):
    s=f'# Lecture {d["id"]}: {d["title"]}\n\n## '+('Worked Solutions' if solution else 'Practice Quiz')+'\n\n'
    s+='**100 marks: 12 True/False × 1; 12 multiple response × 2; 4 proofs/derivations × 10; 2 applications × 12.**\n\n'
    s+='Answer in English. Every multiple-response question has four options and 1–3 correct answers. Exact set: 2 marks; nonempty proper correct subset: 1; any wrong option or no answer: 0. Use `Quiz.tex` to type your responses in its marked regions.\n\n'
    s+=f'Primary source: [{d["pdf"]}](../../lecture/{d["pdf"]}). Page numbers start at the cover.\n\n'
    s+='## A. True/False\n\n'
    for n,q in enumerate(d['tf'],1):
        s+=f'**{n}.** '+md(q['statement'])+'\n\n'
        if solution:s+=f'**{"True" if q["answer"] else "False"}.** '+md(q['explanation'])+f'\n\n*{q["source"]}.*\n\n'
    s+='## B. Multiple Response\n\n'
    for idx,q in enumerate(d['mc']):
        s+=f'**{idx+13}.** '+md(q['stem'])+'\n\n'
        for j,o in enumerate(q['options']):
            s+=f'- **{chr(65+j)}.** '+md(o['text'])
            if solution:s+=f' **{"Correct" if o["correct"] else "Incorrect"}:** '+md(o['why'])
            s+='\n'
        if solution:s+=f'\n**Correct set: {", ".join(keys[idx])}.** *{q["source"]}.*\n'
        s+='\n'
    for n,q in enumerate(d['long'],25):
        s+=f'## {n}. {q["title"]} [{q["marks"]} marks]\n\n'
        if q.get('stem'):s+=md(q['stem'])+'\n\n'
        for j,p in enumerate(q['parts']):
            s+=f'**({chr(97+j)}) [{p["marks"]} marks]** '+md(p['question'])+'\n\n'
            if solution:s+='**Worked solution:** '+md(p['solution'])+'\n\n'
        if solution:s+=f'*Source: {q["source"]}.*\n\n'
    return s

summary=[]
for f in sorted((ROOT/'source').glob('L[0-9][0-9].json')):
    if args.lesson and f.stem!='L'+args.lesson.zfill(2):continue
    d=json.loads(f.read_text(encoding='utf-8'));validate(d);keys,freq=arrange(d)
    folder=ROOT/('L'+d['id']+'_'+d['slug']);folder.mkdir(exist_ok=True)
    quiz=folder/'Quiz.tex'
    if not quiz.exists():quiz.write_text(render_tex(d,keys),encoding='utf-8')
    else:print('Preserved personal answer file:',quiz)
    (folder/'Solutions.tex').write_text(render_tex(d,keys,True),encoding='utf-8')
    (folder/'Quiz.md').write_text(render_md(d,keys),encoding='utf-8')
    (folder/'Solutions.md').write_text(render_md(d,keys,True),encoding='utf-8')
    audit={'lecture':d['id'],'total_marks':100,'question_count':30,'tf_key':['T' if q['answer'] else 'F' for q in d['tf']],'mc_key':keys,'letter_frequency':freq,'correct_option_counts':dict(Counter(map(len,keys)))}
    (folder/'author_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
    summary.append((d['id'],d['title'],folder.name))
    print(d['id'],d['title'],'validated and generated')

if not args.lesson:
    text='# CS182 — Quizzes by Lecture\n\n'
    text+='Each lecture has a separate English 100-mark quiz: 12 misconception T/F questions, 12 multiple-response questions, 4 proof/formula-derivation problems, and 2 application problems. This design allows a complete check immediately after studying that lecture.\n\n'
    text+='The multiple-response rule is unchanged: exactly four options, 1–3 correct; complete correct set = 2, nonempty proper correct subset = 1, any wrong selection or blank = 0. Proofs require intermediate steps, assumptions, and dimensions.\n\n'
    text+='| Lecture | Editable TeX | Questions | Worked solutions |\n|---|---|---|---|\n'
    for ident,title,folder in summary:
        text+=f'| {ident} · {title} | [Quiz.tex]({folder}/Quiz.tex) | [PDF]({folder}/Quiz.pdf) · [MD]({folder}/Quiz.md) | [PDF]({folder}/Solutions.pdf) · [TeX]({folder}/Solutions.tex) · [MD]({folder}/Solutions.md) |\n'
    text+='\n## Type your answers\n\nOpen the corresponding `Quiz.tex`. Fill the second brace pair in `\\SetAnswer{TF01}{}` ... `\\SetAnswer{TF12}{}` and `\\SetAnswer{MC13}{}` ... `\\SetAnswer{MC24}{}`. Search `BEGIN ANSWER Q25(a)` and the analogous markers to type each proof/application subpart. Delete its `\\AnswerBlank` after writing, or change `\\BlankAnswerHeight` to `0mm`. Printed answers and reasoning should be in English; Chinese source comments identify the editing regions. Compile twice with pdfLaTeX. Each TeX file is standalone.\n\n'
    text+='Solutions are separate and include a quick key, an explanation for each option, full mathematical steps, subpart point allocations, and lecture page references. `author_audit.json` also contains answer keys and is intended for checking after attempting the quiz.\n\n'
    text+='The original integrated L1–L6 PDFs remain available as later review papers. The current series uses 30 focused questions per lecture rather than copying that integrated paper into seven files. The source JSONs are read from `source/`; rebuilding preserves an existing `Quiz.tex` so that typed answers are not erased.\n'
    (ROOT/'README.md').write_text(text,encoding='utf-8')
