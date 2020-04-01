import ibis

table = ibis.table([('foo', 'double'), ('bar', 'double')], name='sample')
df = table.execute()
print(table)
print(df)
