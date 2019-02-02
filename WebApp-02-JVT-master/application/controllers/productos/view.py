import web 
import config as config

class View:
	def __init__(self):
		pass

	def GET(self,nombre_p):
		cliente = config.model_productos.select_nombre_prod(nombre_p)
		return config.render.view(producto)