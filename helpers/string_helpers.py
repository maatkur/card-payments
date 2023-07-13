
class StringHelpers:

    @staticmethod
    def clear_excel_caracters(value):
        return value.replace('R$', '').replace('.', "").replace(",", ".").replace('- ', "-").strip()
