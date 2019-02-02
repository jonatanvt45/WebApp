import config as config 

db = config.db

def select_productos():
	try:
		return db.select('productos')
	except Exception as e:
		print "Model select_productos Error{}",format(e.args)
		print "Model select_productos Message{}",format(e.message)
		return None

def select_nombre_prod(nombre_p):
	try:
		return db.select('productos',
		where='nombre_prod=$nombre_prod',
		vars=locals())[0]
	except Exception as e:
		print "Model select_nombre_prod Error{}",format(e.args)
		print "Model select_nombre_prod Message{}",format(e.message)
		return None

def insert_producto(nombre_p,categoria,descripcion,marca,cantidad):
	try:
		return db.insert('productos',
		nombre_p=nombre_p,
		categoria=categoria,
		descripcion=descripcion,
		marca=marca,
		cantidad=cantidad)
	except Exception as e:
		print "Model insert_producto Error{}",format(e.args)
		print "Model insert_producto Message{}",format(e.message)
		return None

def delete_producto(nombre_p):
	try:
		return db.delete('productos',
		where='nombre_p=$nombre_p',
		vars=locals())
	except Exception as e:
		print "Model delete_producto Error{}",format(e.args)
		print "Model delete_producto Message{}",format(e.message)
		return None

def update_producto(nombre_p,categoria,descripcion,marca,cantidad):
	try:
		return db.update('productos',
		categoria=categoria,
		descripcion=descripcion,
		marca=marca,
		cantidad=cantidad,
		where='nombre_p=$nombre_p',
		vars=locals())
	except Exception as e:
		print "Model update_producto Error{}",format(e.args)
		print "Model update_producto Message{}",format(e.message)
		return None		