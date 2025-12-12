class Carrito:
    def __init__(self):
        self.items = [] # Lista de diccionarios: {'producto': obj, 'cantidad': int}

    def agregar_producto(self, producto, cantidad):
        if producto.validar_stock(cantidad):
            producto.reducir_stock(cantidad)
            self.items.append({
                "producto": producto,
                "cantidad": cantidad
            })
            print(f" Agregado: {producto.nombre} (x{cantidad})")
        else:
            print(f" Error: No hay stock suficiente de '{producto.nombre}' para agregar {cantidad} unidades.")

    def eliminar_producto(self, codigo):
        # Filtramos la lista para excluir el producto con ese código
        # Nota: En un sistema real, deberíamos devolver el stock al producto.
        items_iniciales = len(self.items)
        self.items = [item for item in self.items if item["producto"].codigo != codigo]
        
        if len(self.items) < items_iniciales:
            print(f"Producto {codigo} eliminado del carrito.")
        else:
            print(f"Producto con código {codigo} no encontrado en el carrito.")

    def mostrar_detalle(self):
        print("\n--- DETALLE DEL CARRITO ---")
        if not self.items:
            print("El carrito está vacío.")
            return

        for item in self.items:
            prod = item["producto"]
            cant = item["cantidad"]
            total_item = prod.calcular_total(cant)
            
            # Determinamos el tipo para mostrar en el print
            tipo = "Físico" if hasattr(prod, 'peso') else "Digital"
            
            print(f"- {prod.nombre} ({tipo}) | Cant: {cant} | Total: ${total_item:.0f}")

    def obtener_total_general(self):
        total = 0
        for item in self.items:
            total += item["producto"].calcular_total(item["cantidad"])
        return total