class Carro:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        Carro=self.session.get('carro')
        if not Carro:
            Carro=self.session['carro']={}
        #else:
        self.Carro=Carro

    def agregar(self,producto):
        if(str(producto.id)not in self.Carro.keys()):
            self.Carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,
            }
        else:
            for key,value in self.Carro.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad'] +1
                    value['precio'] = float(value['precio']) +producto.precio 
                    break
        
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session['carro']=self.Carro
        self.session.modified=True

    def eliminar(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.Carro:
            del self.Carro[producto.id]
            self.guardar_carro()

    def restar_producto(self,producto):
        for key,value in self.Carro.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad'] -1
                    value['precio'] = float(value['precio']) -producto.precio
                    if value['cantidad'] < 1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session['carro']={}
        self.session.modified=True


        




        
    

    