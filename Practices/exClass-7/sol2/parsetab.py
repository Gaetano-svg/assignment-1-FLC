
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'C CM DATA DATE HOUR IP KBS NUMBER S SERVER SONG START TIME\n        prog : prog_ok\n        \n        prog_ok : START C mp3_list SERVER C data_time user_list\n        \n        mp3_list : mp3 \n                    | mp3_list mp3\n        \n        mp3 : NUMBER KBS NT1 C NT0 song_list S\n        \n        NT1 : \n        \n        NT0 : \n        \n        song_list : song_list CM song \n                    | song\n        \n        song : SONG NUMBER\n        \n        data_time : TIME C HOUR DATA C DATE\n                    | DATA C DATE TIME C HOUR \n        \n        user_list : \n                    | user_list user\n        \n        user : ip C songs_list S\n        \n        ip : IP\n        \n        songs_list : SONG\n                        | songs_list CM SONG\n        '
    
_lr_action_items = {'START':([0,],[3,]),'$end':([1,2,13,17,21,40,42,43,],[0,-1,-13,-2,-14,-15,-11,-12,]),'C':([3,8,10,12,14,15,22,23,30,31,],[4,11,-6,16,18,19,29,-16,37,38,]),'NUMBER':([4,5,6,9,28,32,],[7,7,-3,-4,34,-5,]),'SERVER':([5,6,9,32,],[8,-3,-4,-5,]),'KBS':([7,],[10,]),'TIME':([11,25,],[14,31,]),'DATA':([11,24,],[15,30,]),'IP':([13,17,21,40,42,43,],[-13,23,-14,-15,-11,-12,]),'SONG':([16,20,29,33,41,],[-7,28,36,28,44,]),'HOUR':([18,38,],[24,43,]),'DATE':([19,37,],[25,42,]),'S':([26,27,34,35,36,39,44,],[32,-9,-10,40,-17,-8,-18,]),'CM':([26,27,34,35,36,39,44,],[33,-9,-10,41,-17,-8,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'prog_ok':([0,],[2,]),'mp3_list':([4,],[5,]),'mp3':([4,5,],[6,9,]),'NT1':([10,],[12,]),'data_time':([11,],[13,]),'user_list':([13,],[17,]),'NT0':([16,],[20,]),'user':([17,],[21,]),'ip':([17,],[22,]),'song_list':([20,],[26,]),'song':([20,33,],[27,39,]),'songs_list':([29,],[35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> prog_ok','prog',1,'p_prog','myParser.py',29),
  ('prog_ok -> START C mp3_list SERVER C data_time user_list','prog_ok',7,'p_prog_ok','myParser.py',36),
  ('mp3_list -> mp3','mp3_list',1,'p_mp3_list','myParser.py',41),
  ('mp3_list -> mp3_list mp3','mp3_list',2,'p_mp3_list','myParser.py',42),
  ('mp3 -> NUMBER KBS NT1 C NT0 song_list S','mp3',7,'p_mp3','myParser.py',47),
  ('NT1 -> <empty>','NT1',0,'p_NT1','myParser.py',52),
  ('NT0 -> <empty>','NT0',0,'p_NT0','myParser.py',59),
  ('song_list -> song_list CM song','song_list',3,'p_song_list','myParser.py',66),
  ('song_list -> song','song_list',1,'p_song_list','myParser.py',67),
  ('song -> SONG NUMBER','song',2,'p_song','myParser.py',72),
  ('data_time -> TIME C HOUR DATA C DATE','data_time',6,'p_data_time','myParser.py',84),
  ('data_time -> DATA C DATE TIME C HOUR','data_time',6,'p_data_time','myParser.py',85),
  ('user_list -> <empty>','user_list',0,'p_user_list','myParser.py',92),
  ('user_list -> user_list user','user_list',2,'p_user_list','myParser.py',93),
  ('user -> ip C songs_list S','user',4,'p_user','myParser.py',98),
  ('ip -> IP','ip',1,'p_ip','myParser.py',105),
  ('songs_list -> SONG','songs_list',1,'p_songs_list','myParser.py',112),
  ('songs_list -> songs_list CM SONG','songs_list',3,'p_songs_list','myParser.py',113),
]
