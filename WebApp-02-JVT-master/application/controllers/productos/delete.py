import web
import config as config

class Delete:
	def __init__(self):
		pass

	def GET(self,nombre_p):
		productos = config.model_productos.select_nombre(nombre_p)
		return config.render.delete(productos)

	def POST(self,nombre_prod):
		formulario = web.input()
		nombre_prod = formulario['nombre_p']
		tipo = formulario ['categoria']
		descripcion = formulario ['descripcion']
		marca = formulario ['marca']
		origen = formulario ['cantidad']
		config.model_productos.delete_producto(nombre_p)
		raise web seeother('/')