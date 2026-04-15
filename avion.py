flota = {
    "N123AA": {
        "modelo": "Boeing 787-9",
        "año": 2018,
        "horas_vuelo": 12500,
        "ciclos": 1350,
        "estado": "En servicio",
        "base": "DFW",
        "proxima_revision": "2023-07-15"
    },
    "N456AA": {
        "modelo": "Boeing 777-300ER",
        "año": 2014,
        "horas_vuelo": 26800,
        "ciclos": 2940,
        "estado": "En mantenimiento",
        "base": "MIA",
        "proxima_revision": "2023-03-30"
    }
}

placa = input("Ingrese la placa:")
mod = input("Ingrese  el modelo:")
year = input("Ingrese el año de producción:")
H = input("Ingrese las horas de vuelo de la aeronave:")
cic = input("Ingrese el numero de ciclos:")
est = input("Ingrese el estado de la aeronave")
bas = input("Ingrese la base")
rev = input("cuando se la la proxima revisión de la eronave")

temp = {}
temp["modelo"] = mod
temp["año"] = year
temp["Horas de vuelo"] = H
temp["ciclos"] = cic
temp["estado"] = est
temp["base"] = bas
temp["revisión"] = rev


flota[placa] = temp


