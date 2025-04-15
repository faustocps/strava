import flet as ft

from mock import mock
from strava import scrape_website
import time as sleep

def main(page: ft.Page):
    page.title = "last physical activity"
    page.bgcolor = "#fafafa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # loading = ft.Container(
    #     content=ft.Column(
    #         [ft.ProgressRing()],
    #         alignment=ft.MainAxisAlignment.CENTER
    #     ),
    #     expand=True
    # )
    # page.add(loading)
    # page.update()

    # # Simula um carregamento
    # sleep.sleep(2)

    # page.clean()

    domain = 'https://www.strava.com/athletes/47411883'
    
    # Coletar conteúdo
    conteudo =  scrape_website(domain)
    #conteudo =  mock()#scrape_website(dominio)

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
                        # ft.Icon(name=ft.Icons.PEDAL_BIKE, color="#e7520b", size=30),
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
                    ft.Text(f"{distance}", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("Distância", size=12, color=ft.colors.GREY_600),
                ], alignment=ft.MainAxisAlignment.CENTER),
                width=150,
                height=100,
            ),
            
            # Coluna 2 - Elevação
            ft.Container(
                content=ft.Column([
                    ft.Text(f"{elevation}", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("Elevação", size=12, color=ft.colors.GREY_600),
                ], alignment=ft.MainAxisAlignment.CENTER),
                width=150,
                height=100,
            ),
            
           
            # Coluna 3 - Tempo
            ft.Container(
                content=ft.Column([
                    ft.Text(f"{time}", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("Tempo de movimentação", size=12, color=ft.colors.GREY_600),
                ], alignment=ft.MainAxisAlignment.CENTER),
                width=150,
                height=100,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    linha_horizontal = ft.Divider(height=2, color=ft.colors.GREY_300)

    page.add(
        ft.Column([linha, linha_horizontal]),
    )

    link = ft.GestureDetector(
        content=ft.Text(
            spans=[
                ft.TextSpan(
                    f"Ver mais de {name} (Strava)",
                    on_click=lambda e: e.page.launch_url(f"{domain}"),
                    style=ft.TextStyle(
                        color=ft.colors.BLUE,
                        decoration=ft.TextDecoration.UNDERLINE,
                    )
                )
            ]
        ),
        mouse_cursor=ft.MouseCursor.CLICK  # Adicione aqui!
    )

    page.add(link)

   
    if conteudo:
        # Criar nome de arquivo
        # nome_arquivo = dominio.split('//')[-1].replace('/', '_') + '.txt'
        # save_content(conteudo, nome_arquivo)
        print(conteudo)

ft.app(target=main)