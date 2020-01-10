class CustomRequest():

    @staticmethod
    def verificarParametros(data, fields):
        # COPIAR OBJETO SIN REFERENCIA
        aux_data = dict(data)
        for key in data:
            if not isinstance(data[key], dict) or not isinstance(data[key], list) or not isinstance(data[key], tuple):
                if key not in fields or key == 'id':
                    aux_data.pop(key)
        return aux_data