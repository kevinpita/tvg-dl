import requests


class TvgDl:
    def __init__(self, url_programa):
        self.__HEADERS = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "en-US,en;q=0.5",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://www.crtvg.es",
                "DNT": "1",
                "Connection": "keep-alive",
                "Referer": url_programa
        }
        self.__programas = {}
        self.__separador_guardado = " || "
        self.__url_programa = url_programa
        self.__id_programa = 0
        self.__numero_pagina = 0
        self.__id_seccion = 0
        self.__respuesta_url_programa = self.__codificar_respuesta(url_programa)
        self.__definir_ids_programa()

    def __definir_ids_programa(self):
        self.__id_seccion = self.__respuesta_url_programa.split("AlaCartaBuscador(")[1].split(", ")[0]
        self.__id_seccion = self.__respuesta_url_programa.split("AlaCartaBuscador(")[1].split(", ")[2].split(")")[0]

    @staticmethod
    def __codificar_respuesta(url) -> str:
        respuesta = requests.get(url)
        respuesta.encoding = "UTF-8"
        return respuesta.text

    def guardar_programas(self, nombre="tvg-dl.txt") -> None:
        r"""Guardar los links de los progrmas y sus títulos

        :param nombre: Nombre del archivo donde se persisten los datos
            si no se inserta extensión se añadirá .txt
        """
        if "." not in nombre:
            nombre = nombre + ".txt"

        with open(nombre, "w") as f:
            for programa in self.__programas:
                f.write(
                    f"{self.__programas[programa][0]}"
                    f"{self.__separador_guardado}"
                    f"{programa} "
                    f"[{self.__programas[programa][1]}]\n"
                )

    def cargar_programas(self, nombre="tvg-dl.txt") -> None:
        with open(nombre, "r") as f:
            lineas = f.read().split("\n")
        for linea in lineas:
            self.__programas[linea.split(self.__separador_guardado)[0]] = linea.split(self.__separador_guardado)[1]







