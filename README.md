# px

protocol: modbus over rs-485
master - tp-link 703n



slave registers:
0 - количество параметров слейва n
1 - 20 - описание слейва
    1-5: серийный номер
    6-7: версия софта
21 - 21+n - описание типов параметров
21+n+1 - 21+2n - значения параметров