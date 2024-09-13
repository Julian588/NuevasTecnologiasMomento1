from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

#Usuario
class Usuario(Base):
    __tablename__='usuario'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(100))
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))

#Gastos
class Gasto(Base):
    __tablename__='gastos'
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Integer(50))
    fecha=Column(Date)
    descripcion=Column(String(50))
    nombre=Column(String(50))


#Categoria
class Categoria(Base):
    __tablename__='categoria'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(20))
    descripcion=Column(String(50))
    fotoicono=Column(String(50))

#Metodos de Pago
class MetodoPago(Base):
    __tablename__='pagos'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    descripcion=Column(String(50))

#Prestamo
class Prestamo(Base):
    __tablename__='prestamo'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(100))
    ciudad=Column(String(50))
    salario=Column(float)
    fechaRegistro=Column(Date)

#Deuda
class Deuda(Base):
    __tablename__='deuda'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(50))
    telefono=Column(String(12))
    correo=Column(String(100))
    ciudad=Column(String(50))
    deuda=Column(float)
    fechaRegistro=Column(Date)
    pago=Column(float)

#Ingreso Mensual
class IngresoMensual(Base):
    __tablename__='ingresomensual'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(50))
    fechaRegistro=Column(Date)
    valor=Column(float)