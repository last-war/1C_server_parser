from pathlib import Path
import shutil

if __name__ == '__main__':
    path1c = Path('//s-1c8/C$/Program Files/1cv8/srvinfo/reg_1541')  #
    name_f = '1CV8Clsto.lst'
    without = ("S-1C8", "Локальный кластер", "Центральный сервер", "Главный менеджер кластера", ",")
    dict_rez = {}
    with open(path1c.joinpath(name_f), 'r', encoding='utf-8') as f_1c:
        for file_line in f_1c:
            if file_line[9:10] == file_line[14:15] == file_line[19:20] == file_line[24:25] == '-':
                ind_ = file_line[39:60].find('"')
                if ind_ == -1:
                    ind_ = file_line[39:].find('"')
                bas = file_line[39:39+ind_]
                if not bas in without:
                    dict_rez[file_line[1:37]] = bas

    for dir in path1c.iterdir():
        if dir.is_dir():
            if not dir.stem in dict_rez.keys():
                print("del dir "+dir.stem)
                shutil.rmtree(dir)






#    for cur_dir in path1c.iterdir():
#        print(cur_dir)
#    print(type(path1c))
