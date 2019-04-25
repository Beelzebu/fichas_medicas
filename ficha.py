# -*- coding: utf-8 -*-
from medicine import MedicamentoRecetado
from people import (Acompaniante, Paciente, Personal, Medico)


class Ficha:

    def __init__(self, paciente: Paciente, acompaniante: Acompaniante, nivel_de_urgencia: str,
                 personal_ingreso: Personal, fecha: str, hora: str):
        self.id: int = -1
        if not isinstance(paciente, Paciente):
            raise ValueError("paciente is not an instance of Persona")
        self.paciente: Paciente = paciente
        if not isinstance(personal_ingreso, Personal):
            raise ValueError("personal_ingreso is not an instance of Persona")
        if not isinstance(acompaniante, Acompaniante) and acompaniante is not None:
            raise ValueError("acompaniante is not an instance of Acompaniante")
        self.acompaniante: Acompaniante = acompaniante
        self.nivel_de_urgencia: str = nivel_de_urgencia
        self.personal_ingreso: Personal = personal_ingreso
        self.fecha: str = fecha
        self.hora: str = hora
        self.medico: Medico = None
        self.sintomas: str = ""
        self.diagnostico: str = ""
        self.reposo: bool = False
        self.reposo_dias: int = 0
        self.tiempo_atencion: int = 0
        self.medicamento: MedicamentoRecetado = None

    def __str__(self):
        return "-----------------------\nFICHA DE INGRESO N° {}:\n-----------------------\n\n" \
               "Fecha de atención: {}\n" \
               "Hora de atención: {}\n" \
               "Personal que ingresa ficha: {}\n" \
               "Identificación de paciente:\n" \
               "  Nombre: {}\n" \
               "  Apellido: {}\n" \
               "  Rut: {}\n" \
               "  Estado civil: {}\n" \
               "  Domicilio: {}\n" \
               "  Fono: {}\n" \
               "  Asiste acompañado: {}\n" \
               "  Nivel de urgencia: {}\n" \
               "  Sexo: {}\n" \
               "  Edad: {}\n" \
               "  Grupo sanguíneo: {}\n" \
               "\nIdentificación de acompañante:\n" \
               "  Nombre: {}\n" \
               "  Apellido: {}\n" \
               "  Rut: {}\n" \
               "  Grado de parentesco: {}\n" \
               "  Fono: {}\n" \
               "\nInformación de atención:\n" \
               "  Nombre médico: {}\n" \
               "  Especialidad: {}\n" \
               "  Síntomas detectados: {}\n" \
               "  Diagnóstico: {}\n" \
               "  Reposo: {}\n" \
               "  Cantidad de días: {}\n" \
               "\nInformación de medicamento:\n" \
               "  Médico asigna medicamento: {}\n" \
               "  Nombre de medicamento: {}\n" \
               "  Dósis: {}\n" \
               "  Cantidad de días: {}".format(self.id,
                                               self.fecha,
                                               self.hora,
                                               self.personal_ingreso.nombre + " " + self.personal_ingreso.apellido,
                                               self.paciente.nombre,
                                               self.paciente.apellido,
                                               self.paciente.run,
                                               self.paciente.estado_civil,
                                               self.paciente.direccion,
                                               self.paciente.telefono,
                                               "Si" if self.acompaniante is not None else "No",
                                               self.nivel_de_urgencia,
                                               self.paciente.sexo,
                                               self.paciente.edad,
                                               self.paciente.grupo_sanguineo,
                                               self.acompaniante.nombre if self.acompaniante is not None else "",
                                               self.acompaniante.apellido if self.acompaniante is not None else "",
                                               self.acompaniante.run if self.acompaniante is not None else "",
                                               self.acompaniante.parentesco if self.acompaniante is not None else "",
                                               self.acompaniante.telefono if self.acompaniante is not None else "",
                                               self.medico.nombre + " " + self.medico.apellido if self.medico is not None else "",
                                               self.medico.especialidad if self.medico is not None else "",
                                               self.sintomas if self.medico is not None else "",
                                               self.diagnostico if self.medico is not None else "",
                                               self.reposo if self.medico is not None else "",
                                               self.reposo_dias if self.medico is not None else "",
                                               "Si" if self.medicamento is not None else "No",
                                               self.medicamento.medicamento.nombre if self.medicamento is not None else "",
                                               self.medicamento.dosis if self.medicamento is not None else "",
                                               self.medicamento.dias if self.medicamento is not None else "")
