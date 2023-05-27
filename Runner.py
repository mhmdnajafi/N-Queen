from NQueen import Gentic
queen=Gentic(7,500,0.8,0.2)
run_l,answer_l,time_l,answer=queen.run(30000)
path_save=queen.folder('7 Queen')
queen.chart(run_l,answer_l,'Run','True Answer',show=False,path=path_save,save=True)
queen.chart(time_l[2:],answer_l,'Time','True Answer',show=False,path=path_save,save=True)
queen.chart(time_l[2:],run_l,'Time','Run',show=False,path=path_save,save=True)
queen.txt(path_save,answer)