
class StringHelpers:

    @staticmethod
    def clear_excel_caracters(value):
        return value.replace('R$', '').replace('.', "").replace(",", ".").replace('- ', "-").strip()

    @staticmethod
    def get_value_before_slash(value):
        if "/" in value:
            value_before_slash = value.split("/")[0]
        else:
            value_before_slash = value

        return value_before_slash
