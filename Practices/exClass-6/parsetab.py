
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARROW C CB D DD DIV EQ ID MINUS NUMBER OB PLUS SC STAR WORD\n        prog : definitions D descriptions\n        \n        definitions : definitions definition\n                        | definition\n        \n        definition :  OB attrib_list CB ARROW ident\n        \n        attrib_list :  attrib_list C attrib\n                        | attrib\n        \n        attrib : ident DD NUMBER\n        \n        descriptions : descriptions description\n                        | \n        \n        description : ident DD scores EQ sentence SC \n        \n        scores : scores NT0 C valutation\n                    | valutation\n        \n        NT0 : \n        \n        valutation : point ident\n        \n        point : STAR\n                | PLUS\n                | DIV\n                | MINUS\n        \n        sentence : sentence sentence_elem\n                    | sentence_elem\n        \n        sentence_elem : WORD\n                        | NUMBER\n        \n        ident : ID\n                | WORD\n        '
    
_lr_action_items = {'OB':([0,2,3,6,10,11,22,],[4,4,-3,-2,-23,-24,-4,]),'$end':([1,5,12,16,38,],[0,-9,-1,-8,-10,]),'D':([2,3,6,10,11,22,],[5,-3,-2,-23,-24,-4,]),'ID':([4,5,12,14,16,18,25,26,27,28,29,38,],[10,-9,10,10,-8,10,10,-15,-16,-17,-18,-10,]),'WORD':([4,5,12,14,16,18,25,26,27,28,29,30,33,34,35,36,38,39,],[11,-9,11,11,-8,11,11,-15,-16,-17,-18,35,35,-20,-21,-22,-10,-19,]),'CB':([7,9,19,20,],[13,-6,-5,-7,]),'C':([7,9,10,11,19,20,23,24,31,32,40,],[14,-6,-23,-24,-5,-7,-13,-12,37,-14,-11,]),'DD':([8,10,11,17,],[15,-23,-24,21,]),'EQ':([10,11,23,24,32,40,],[-23,-24,30,-12,-14,-11,]),'ARROW':([13,],[18,]),'NUMBER':([15,30,33,34,35,36,39,],[20,36,36,-20,-21,-22,-19,]),'STAR':([21,37,],[26,26,]),'PLUS':([21,37,],[27,27,]),'DIV':([21,37,],[28,28,]),'MINUS':([21,37,],[29,29,]),'SC':([33,34,35,36,39,],[38,-20,-21,-22,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'definitions':([0,],[2,]),'definition':([0,2,],[3,6,]),'attrib_list':([4,],[7,]),'ident':([4,12,14,18,25,],[8,17,8,22,32,]),'attrib':([4,14,],[9,19,]),'descriptions':([5,],[12,]),'description':([12,],[16,]),'scores':([21,],[23,]),'valutation':([21,37,],[24,40,]),'point':([21,37,],[25,25,]),'NT0':([23,],[31,]),'sentence':([30,],[33,]),'sentence_elem':([30,33,],[34,39,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> definitions D descriptions','prog',3,'p_prog','myParser.py',28),
  ('definitions -> definitions definition','definitions',2,'p_definitions','myParser.py',35),
  ('definitions -> definition','definitions',1,'p_definitions','myParser.py',36),
  ('definition -> OB attrib_list CB ARROW ident','definition',5,'p_definition','myParser.py',41),
  ('attrib_list -> attrib_list C attrib','attrib_list',3,'p_attrib_list','myParser.py',55),
  ('attrib_list -> attrib','attrib_list',1,'p_attrib_list','myParser.py',56),
  ('attrib -> ident DD NUMBER','attrib',3,'p_attrib','myParser.py',86),
  ('descriptions -> descriptions description','descriptions',2,'p_descriptions','myParser.py',99),
  ('descriptions -> <empty>','descriptions',0,'p_descriptions','myParser.py',100),
  ('description -> ident DD scores EQ sentence SC','description',6,'p_description','myParser.py',105),
  ('scores -> scores NT0 C valutation','scores',4,'p_scores','myParser.py',113),
  ('scores -> valutation','scores',1,'p_scores','myParser.py',114),
  ('NT0 -> <empty>','NT0',0,'p_NT0','myParser.py',128),
  ('valutation -> point ident','valutation',2,'p_valutation','myParser.py',135),
  ('point -> STAR','point',1,'p_point','myParser.py',153),
  ('point -> PLUS','point',1,'p_point','myParser.py',154),
  ('point -> DIV','point',1,'p_point','myParser.py',155),
  ('point -> MINUS','point',1,'p_point','myParser.py',156),
  ('sentence -> sentence sentence_elem','sentence',2,'p_sentence','myParser.py',175),
  ('sentence -> sentence_elem','sentence',1,'p_sentence','myParser.py',176),
  ('sentence_elem -> WORD','sentence_elem',1,'p_sentence_elem','myParser.py',187),
  ('sentence_elem -> NUMBER','sentence_elem',1,'p_sentence_elem','myParser.py',188),
  ('ident -> ID','ident',1,'p_ident','myParser.py',195),
  ('ident -> WORD','ident',1,'p_ident','myParser.py',196),
]