全班學生 = set(['John', 'Mary', 'Tina', 'Fiona', 'Claire', 'Eva', 'Ben', 'Bill', 'Bert'])
英文及格 = set(['John', 'Mary', 'Fiona', 'Claire', 'Ben', 'Bill'])
數學及格 = set(['Mary', 'Fiona', 'Claire', 'Eva', 'Ben'])
print('英文與數學都及格', 英文及格&數學及格)
print('數學不及格', 全班學生-數學及格)
print('英文及格與數學不及格', 英文及格&(全班學生-數學及格))