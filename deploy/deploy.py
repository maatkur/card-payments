# deploy.py

import os
import PyInstaller.__main__


def main():
    # Caminho para o arquivo de configuração
    config_file = "cards_login_view.spec"

    # Executa o PyInstaller com base no arquivo de configuração
    PyInstaller.__main__.run([
        config_file
    ])


if __name__ == "__main__":
    main()
