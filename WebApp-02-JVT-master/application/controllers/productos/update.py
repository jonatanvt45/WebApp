import web
import config as config 

class Update:
	def __init__(self):
		pass

	def GET(self,nombre_p):
		cliente = config.model_productos.select_nombre_p(nombre_p)
		return config.render.update(producto)

	def POST(self,categoria,descripcion,marca,cantidad):
		formulario = web.input()
		nombre_p = formulario['nombre_p']
		categoria = formulario ['categoria']
		descripcion = formulario ['descripcion']
		marca = formulario ['marca']
		cantidad = formulario ['cantidad']
		config.model_productos.update_producto(nombre_p,categoria,descripcion,marca,cantidad)
		raise web.seeother('/')