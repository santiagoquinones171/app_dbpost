from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from modelos import modelo_producto

router = APIRouter()


@router.get("/")
async def consultar():
    return "API CBA Agro"


@router.get("/prod_all")
def get_productos(db: Session = Depends(get_db)):
    productos = db.query(modelo_producto.Producto).all()
    return productos


@router.get("/{id_producto}")
def get_producto(id_producto: int, db: Session = Depends(get_db)):
    producto = db.query(modelo_producto.Producto).filter(
        modelo_producto.Producto.id_producto == id_producto).first()
    if producto:
        return producto
    raise HTTPException(status_code=404, detail=f"Producto con id {id_producto} no encontrado")


@router.get("/categorias")
def get_categorias(db: Session = Depends(get_db)):
    categorias = db.query(modelo_producto.Categoria).all()
    return categorias


@router.get("/usuarios")
def get_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(modelo_producto.Usuario).all()
    return usuarios


@router.get("/pedidos")
def get_pedidos(db: Session = Depends(get_db)):
    pedidos = db.query(modelo_producto.Pedido).all()
    return pedidos


@router.delete("/borrar/{id_producto}")
def borrar_producto(id_producto: int, db: Session = Depends(get_db)):
    producto = db.query(modelo_producto.Producto).filter(
        modelo_producto.Producto.id_producto == id_producto).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return f"Producto {id_producto} eliminado"