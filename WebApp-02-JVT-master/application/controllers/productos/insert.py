import web 
import config as config 

class Insert:
	def __init__(self):
		pass

	def GET(self):
		return config.render.insert()

	def POST(self):
		formulario = web.input()
		nombre_p= formulario['nombre_p']
		tipo = formulario['categoria']
		descripcion = formulario['descripcion']
		marca = formulario['marca']
		cantidad = formulario['cantidad']
		config.model_productos.insert_producto(nombre_p,cantidad,descripcion,marca,cantidad)
		raise web.seeother('/')