class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def validar_stock(self, cantidad):
        """Verifica si hay suficiente stock y si la cantidad es positiva."""
        return 0 < cantidad <= self.stock

    def reducir_stock(self, cantidad):
        """Disminuye el stock disponible."""
        if self.validar_stock(cantidad):
            self.stock -= cantidad
            return True
        return False

    def calcular_total(self, cantidad):
        """Método base para el cálculo (será sobreescrito por las hijas)."""
        return self.precio * cantidad

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - ${self.precio} (Stock: {self.stock})"


class ProductoFisico(Producto):
    def __init__(self, codigo, nombre, precio, stock, peso, categoria_envio):
        super().__init__(codigo, nombre, precio, stock)
        self.peso = peso
        # Categorías: 'liviano', 'estandar', 'pesado'
        self.categoria_envio = categoria_envio.lower()

    def calcular_costo_envio(self):
        """Define el costo de envío según la categoría."""
        tarifas = {
            "liviano": 2000,
            "estandar": 5000,
            "pesado": 10000
        }
        return tarifas.get(self.categoria_envio, 5000) # 5000 por defecto

    def calcular_total(self, cantidad):
        """Precio base * cantidad + costo de envío único por el paquete."""
        subtotal = super().calcular_total(cantidad)
        envio = self.calcular_costo_envio()
        return subtotal + envio


class ProductoDigital(Producto):
    def __init__(self, codigo, nombre, precio, stock, tamano_archivo, tipo_licencia):
        super().__init__(codigo, nombre, precio, stock)
        self.tamano_archivo = tamano_archivo
        # Licencias: 'personal', 'comercial'
        self.tipo_licencia = tipo_licencia.lower()

    def calcular_recargo_licencia(self):
        """Si es licencia comercial, aplica un recargo."""
        if self.tipo_licencia == "comercial":
            return 0.20 * self.precio # 20% de recargo sobre el precio base
        return 0

    def calcular_total(self, cantidad):
        """Precio con recargo de licencia * cantidad."""
        recargo = self.calcular_recargo_licencia()
        precio_final_unitario = self.precio + recargo
        return precio_final_unitario * cantidad