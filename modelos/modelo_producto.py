from sqlalchemy import Column, Integer, String, Text, DECIMAL, Date, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Rol(Base):
    __tablename__ = "roles"

    id_rol = Column(Integer, primary_key=True)
    nombre_rol = Column(String(50))

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    correo = Column(String(100))
    password = Column(String(255))
    telefono = Column(String(20))
    fecha_registro = Column(DateTime, default=func.now())
    id_rol = Column(Integer, ForeignKey("roles.id_rol"))

class Categoria(Base):
    __tablename__ = "categorias"

    id_categoria = Column(Integer, primary_key=True)
    nombre_categoria = Column(String(100))
    descripcion = Column(Text)

class Producto(Base):
    __tablename__ = "productos"

    id_producto = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(Text)
    precio = Column(DECIMAL(10, 2))
    stock = Column(Integer)
    fecha_cosecha = Column(Date)
    fecha_vencimiento = Column(Date)
    imagen = Column(String(255))
    id_categoria = Column(Integer, ForeignKey("categorias.id_categoria"))

class Carrito(Base):
    __tablename__ = "carrito"

    id_carrito = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    fecha_creacion = Column(DateTime, default=func.now())

class DetalleCarrito(Base):
    __tablename__ = "detalle_carrito"

    id_detalle_carrito = Column(Integer, primary_key=True)
    id_carrito = Column(Integer, ForeignKey("carrito.id_carrito"))
    id_producto = Column(Integer, ForeignKey("productos.id_producto"))
    cantidad = Column(Integer)

class PuntoEntrega(Base):
    __tablename__ = "puntos_entrega"

    id_punto = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    direccion = Column(String(150))
    ciudad = Column(String(100))

class Pedido(Base):
    __tablename__ = "pedidos"

    id_pedido = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    fecha_pedido = Column(DateTime, default=func.now())
    estado = Column(String(50))
    total = Column(DECIMAL(10, 2))
    id_punto_entrega = Column(Integer, ForeignKey("puntos_entrega.id_punto"))

class DetallePedido(Base):
    __tablename__ = "detalle_pedido"

    id_detalle_pedido = Column(Integer, primary_key=True)
    id_pedido = Column(Integer, ForeignKey("pedidos.id_pedido"))
    id_producto = Column(Integer, ForeignKey("productos.id_producto"))
    cantidad = Column(Integer)
    precio_unitario = Column(DECIMAL(10, 2))