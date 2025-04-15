import flet as ft

from i18n import get_texts
from mock import mock
from strava import scrape_website

domain = 'https://www.strava.com/athletes/faustocps'

def main(page: ft.Page):
    lang_code = "pt"
    current_lang = get_texts(lang_code)

    def change_language(e):
        nonlocal current_lang
        current_lang = get_texts(e.control.value)
        page.title = current_lang["title"]
        page.appbar.title.value = current_lang["title"]
        txtDistance.value = current_lang["distance"]
        txtElevation.value = current_lang["elevation"]
        txtTime.value = current_lang["time"]
        txtViewMore.text = current_lang["view_more_strava"].format(name=name)
        page.update()

     
    # Dropdown de idiomas
    lang_selector = ft.Dropdown(
        color="#fafafa",
        bgcolor="#fafafa",# fundo da caixa
        border_color="#fafafa",   
        focused_border_color="#fafafa",
        value=lang_code,
        options=[
                ft.dropdown.Option("pt", "Português"),
                ft.dropdown.Option("en", "English"),
                ft.dropdown.Option("es", "Español")
        ],
        on_change=change_language,
        width=140
    )

    page.title = current_lang["title"]
    page.bgcolor = "#fafafa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.appbar = ft.AppBar(
        title=ft.Text(current_lang["title"], color="#fafafa"),
        center_title=False,
        bgcolor="#e7520b",
        actions=[lang_selector],
    )

    
    # Coletar conteúdo
    conteudo =  scrape_website(domain)
    # conteudo =  mock()#scrape_website(dominio)

    # Processar o texto: remover espaços e linhas vazias
    linhas_processadas = [linha.strip() for linha in conteudo.splitlines() if linha.strip()]

    # Extrair linhas específicas (índices começam em 0)
    fullname = linhas_processadas[0] if len(linhas_processadas) > 0 else None
    name = linhas_processadas[1] if len(linhas_processadas) > 1 else None
    country = linhas_processadas[2] if len(linhas_processadas) > 2 else None  
    date = linhas_processadas[8] if len(linhas_processadas) > 8 else None  
    description = linhas_processadas[9] if len(linhas_processadas) > 9 else None  
    type = linhas_processadas[10] if len(linhas_processadas) > 10 else None  
    distance = linhas_processadas[12] if len(linhas_processadas) > 12 else None  
    elevation = linhas_processadas[14] if len(linhas_processadas) > 14 else None  
    time = linhas_processadas[16] if len(linhas_processadas) > 16 else None  

    print("name:", name)

    txtDistance = ft.Text(current_lang["distance"], size=12, color=ft.colors.GREY_600)
    txtElevation = ft.Text(current_lang["elevation"], size=12, color=ft.colors.GREY_600)
    txtTime = ft.Text(current_lang["time"], size=12, color=ft.colors.GREY_600)
    txtViewMore = ft.TextButton(
        current_lang["view_more_strava"].format(name=name),
        on_click=lambda e: e.page.launch_url(f"{domain}")
    )

    page.add(
        ft.Text(f"{fullname}", size=24, color="#e7520b")
    )

    page.add(
        ft.Text(f"{country}", theme_style=ft.TextThemeStyle.BODY_SMALL)
    )

    page.add(
        ft.Container(
            content=ft.Text(f"{description}", size=30, color="#231c12"),
            padding=ft.padding.only(top=50)  
        )
    )

    page.add(
        ft.Text(f"{date}", size=14)
    )

    # Icons.DIRECTIONS_RUN

    page.add(ft.Column(
            [
               ft.Container(
                    content=ft.Row([
                        ft.Text(f"{type}", color="#e7520b", size=24),
                        # ft.Icon(name=fts.icons.PEDAL_BIKE, color="#e7520b", size=30),
                        # ft.Icon(name="fa-regular fa-bicycle", color=ft.colors.ORANGE)  
                    ], 
                    alignment=ft.MainAxisAlignment.CENTER),
                    padding=ft.padding.only(top=50)
                ),
            ])
    )

    linha = ft.Row(
        controls=[
            # Coluna 1 - Distância
            ft.Container(
                content=ft.Column([
                    ft.Text(f"{distance}", size=28, weight=ft.FontWeight.BOLD),
                    txtDistance,
                ], alignment=ft.MainAxisAlignment.CENTER),
                width=110,
                height=100,
            ),
            
            # Coluna 2 - Elevação
            ft.Container(
                content=ft.Column([
                    ft.Text(f"{elevation}", size=28, weight=ft.FontWeight.BOLD),
                    txtElevation,
                ], alignment=ft.MainAxisAlignment.CENTER),
                width=110,
                height=100,
            ),
            
           
            # Coluna 3 - Tempo
            ft.Container(
                content=ft.Column([
                    ft.Text(f"{time}", size=28, weight=ft.FontWeight.BOLD),
                    txtTime,
                ], alignment=ft.MainAxisAlignment.CENTER),
                width=110,
                height=100,
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    linha_horizontal = ft.Divider(height=2, color=ft.colors.GREY_300)

    page.add(
        ft.Column([linha, linha_horizontal]),
    )

    link = txtViewMore

    page.add(link)
   
    # if conteudo:
    #     # Criar nome de arquivo
    #     # nome_arquivo = dominio.split('//')[-1].replace('/', '_') + '.txt'
    #     # save_content(conteudo, nome_arquivo)
    #     print(conteudo)

ft.app(target=main, view=ft.WEB_BROWSER)