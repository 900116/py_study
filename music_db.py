#encoding=utf-8
import sqlite3
import xlrd
db_name = raw_input('请输入数据库文件名:')
conn = sqlite3.connect(db_name)
print "打开数据库文件成功"
tb_name = raw_input('请输入表名:')
createTabSql = 'CREATE TABLE %s (' % tb_name
propls = []
colName = raw_input('请输入字段名称(例如：ID INT PRIMARY KEY NOT NULL)(按回车退出):')
propls.append(colName.split(' ')[0])
while colName!='':
	createTabSql += colName + ','
	colName = raw_input('请输入字段名称(例如：ID INT PRIMARY KEY NOT NULL)(按回车退出):')
	if colName!='':
		propls.append(colName.split(' ')[0])
createTabSql = createTabSql[:-1]+')'
conn.execute(createTabSql)
xls_name = raw_input('请输入Excel文件名:')
workbook = xlrd.open_workbook(r'%s.xls'%xls_name)
sheet = workbook.sheet_by_index(0)
cols = sheet.ncols
rows = sheet.nrows
tag = bool(raw_input('Excel是否包含表头(1包含，0不包含):'))

beginSql = 'INSERT INTO ' + tb_name + '(' + ','.join(propls) + ') VALUES ('

for i in range(tag,rows):
	sql = beginSql
	cls = sheet.row_values(i)
	for j in cls:
		if isinstance(j,float):
			j = str(int(j))
		else:
			j = "'%s'" % j
		sql = sql + j + ","
	sql = sql[:-1] + ")"
	conn.execute(sql)

conn.commit()
conn.close()