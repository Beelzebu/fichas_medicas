# -*- coding: utf-8 -*-

import os
import platform
import re
import sys
import time

from ficha import Ficha
from medicine import (Lidocaina, Omeprazol, Paracetamol, Penicilina, Salbutamol, MedicamentoRecetado)
from people import (Acompaniante, Medico, Paciente, Personal)

this = sys.modules[__name__]
this.ficha_actual: int = -1
this.fichas = []


def run():
    clear()
    options_str = """Bienvenido al programa, optiones disponibles:

    1) Ingresar ficha del paciente
    2) Actualizar ficha por el médico
    3) Asignación de medicamentos
    4) Obtención de estadísticas
    5) Imprimir una ficha en base a su id
    6) Salir
    """
    print(options_str)
    option = input("Seleccione una opción: ")
    if not isint(option):
        input("No ha ingresado una opción válida, presione enter para reintentar...")
        run()
    else:
        option = int(option)

    if option == 1:
        print("Ha seleccionado ingresar los datos del paciente, a continuación se le solicitarán los datos para "
              "rellenar la ficha de forma automática.")
        paciente = Paciente(input("Nombre: "), input("Apellido: "), int(re.sub(r"\D", "", input("RUN: "))), int(input("Teléfono: ")),
                            input("Dirección: "), input("Estado civil: "), input("Sexo: ").upper(),
                            int(input("Edad: ")), input("Grupo sanguíneo: "))
        while paciente.sexo != "M" and paciente.sexo != "F":
            paciente.sexo = input(
                "Ha ingresado un sexo inválido, ingrese nuevamente (opciones posibles: M, F): ").upper()
        while 0 < paciente.edad > 120:
            paciente.edad = int(input("Ha ingresado una edad inválida, ingrese nuevamente: "))
        acompaniante = None
        if input("¿El paciente viene acompañado?: ").lower() == "si":
            print("Por favor ingrese los datos del acompañante: ")
            acompaniante = Acompaniante(input("Nombre: "), input("Apellido: "), int(re.sub(r"\D", "", input("RUN: "))),
                                        input("Parentesco con el paciente: "), int(input("Teléfono: ")))
        print("Por favor ingrese los datos del personal que realizó el ingreso de datos:")
        personal = Personal(input("Nombre: "), input("Apellido: "), int(re.sub(r"\D", "", input("RUN: "))),
                            input("Título: "), input("Institución de egreso: "), input("Fecha de titulación: "),
                            int(input("Teléfono: ")), input("Dirección: "))
        print("Por favor ingrese la fecha y hora: ")
        ficha = Ficha(paciente, acompaniante, input("Nivel de urgencia: "), personal, input("Fecha: "), input("Hora: "))
        ficha.id = len(this.fichas) + 1
        this.fichas.append(ficha)
        this.ficha_actual = ficha.id - 1
        print("Se han ingresado los siguientes datos de atención correctamente: ")
        print(str(ficha))
        print("Id de ficha: " + str(ficha.id))
        input("Presione enter para continuar.")

    elif option == 2:
        if this.ficha_actual == -1:
            print("Aún no se ha ingresado ninguna ficha, por favor ingrese los datos del paciente.")
            time.sleep(5)
        else:
            print("Ingrese los datos del médico: \n")
            get_ficha().medico = Medico(input("Nombre: "), input("Apellido: "), int(re.sub(r"\D", "", input("RUN: "))),
                                        input("Titulo: "), input("Institución egreso: "),
                                        input("Fecha de titulación: "), int(input("Teléfono: ")), input("Dirección: "),
                                        input("Especialidad: "))
            get_ficha().sintomas = input("Síntomas: ")
            get_ficha().diagnostico = input("Diagnóstico: ")
            get_ficha().reposo = input("Reposo: ").lower() == "si"
            if get_ficha().reposo:
                get_ficha().reposo_dias = int(input("Días de reposo: "))
            get_ficha().tiempo_atencion = int(input("Tiempo de atención en minutos: "))
            print(get_ficha())
            input("Presione enter para continuar.")
    elif option == 3:
        if this.ficha_actual == -1:
            print("Aún no se ha ingresado ninguna ficha, por favor ingrese los datos del paciente.")
            time.sleep(5)
        else:
            medicamentos_str = """Seleccione el tipo de medicamento:
            1) Parcetamol
            2) Lidocaína
            3) Omeprazol
            4) Penicilina
            5) Salbutamol
            """
            medicamento_opt = input(medicamentos_str)
            while not is_in_range(medicamento_opt, 1, 5):
                medicamento_opt = input(medicamentos_str)
                if not isint(option):
                    input("No ha ingresado una opción válida, reintente...")
                    continue
            medicamento_opt = int(medicamento_opt)
            medicamento = None
            if medicamento_opt == 1:
                medicamento = Paracetamol()
            elif medicamento_opt == 2:
                medicamento = Lidocaina()
            elif medicamento_opt == 3:
                medicamento = Omeprazol()
            elif medicamento_opt == 4:
                medicamento = Penicilina()
            elif medicamento_opt == 5:
                medicamento = Salbutamol()
            else:
                # DEBUG, nunca debería pasar
                print("No se ha encontrado un medicamento válido para: " + str(medicamento_opt))
                time.sleep(5)
                run()
            get_ficha().medicamento = MedicamentoRecetado(medicamento, int(input("Ingrese la dósis: ")),
                                                                             int(input("Ingrese el número de días: ")))
            print(this.ficha_actual)
            input("Presione enter para continuar.")
    elif option == 4:
        atendidos_hombres = 0
        atendidos_mujeres = 0
        reposo = 0
        tiempo_atencion = 0
        medicamentos_total = 0
        medicamentos_solicitados = {}
        for x in this.fichas:
            x: Ficha = x
            if x.paciente.sexo == "M":
                atendidos_hombres += 1
            elif x.paciente.sexo == "F":
                atendidos_mujeres += 1
            if x.reposo:
                reposo += 1
            tiempo_atencion += x.tiempo_atencion
            if x.medicamento is not None:
                medicamentos_total += 1
                dosis: int = 0 if medicamentos_solicitados[x.medicamento.medicamento.nombre] is None else int(
                    medicamentos_solicitados[x.medicamento.medicamento.nombre])
                dosis += x.medicamento.dosis
                medicamentos_solicitados[x.medicamento] = dosis

        stats = "Estadísticas de atención:\n" \
                "  Pacientes atendidos en total: {}\n" \
                "  Hombres atendidos: {}\n" \
                "  Mujeres atendidas: {}\n" \
                "  Pacientes con reposo: {}\n" \
                "  Tiempo total de atención: {} minutos\n" \
                "  Tiempo promedio de atención: {} minutos\n" \
                "  Cantidad de medicamentos solicitados en total: {}\n" \
                "  Medicamentos solicitados por tipo: {}".format(len(this.fichas),
                                                                 atendidos_hombres,
                                                                 atendidos_mujeres,
                                                                 reposo,
                                                                 tiempo_atencion,
                                                                 tiempo_atencion / len(this.fichas),
                                                                 medicamentos_total,
                                                                 medicamentos_solicitados)
        print(stats)
        input("Presione enter para continuar.")
    elif option == 5:
        index = toint(input("Ingrese el id de ficha para obtener: "))
        while not isint(index):
            index = toint(input("No se ha ingresado un valor válido, reintente: "))
        if 0 <= index <= len(this.fichas):
            ficha: Ficha = this.fichas[index - 1]
            print(ficha)
            input("Presione enter para continuar.")
        else:
            print("No se ha encontrado una ficha con el id entregado.")
            time.sleep(5)
    elif option == 6:
        print("Saliendo del programa...")
        time.sleep(5)
        exit(0)
    else:
        print("Opción inválida, reintente.")


def isint(x) -> bool:
    try:
        int(x)
        return True
    except ValueError:
        return False


def toint(x):
    return int(x) if isint(x) else x


def is_in_range(x: any, rmin: int, rmax: int) -> bool:
    if isint(x):
        x = int(x)
        return rmin - 1 < x < rmax + 1
    else:
        return False


def get_ficha() -> Ficha:
    return this.fichas[this.ficha_actual]


def clear():
    name = re.sub(r"[^\w]+", "", platform.system()).lower()
    if "windows" in name:
        os.system("cls")
    else:
        os.system("clear")


if __name__ == '__main__':
    while True:
        try:
            run()
        except KeyboardInterrupt:
            exit(0)
