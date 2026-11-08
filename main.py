import os
from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
)
import yt_dlp

console = Console()


def baixar_musicas():
    if not os.path.exists('link.txt'):
        console.print("[bold red]Erro:[/bold red] Arquivo 'link.txt' não encontrado.")
        return

    with open('link.txt', 'r', encoding='utf-8') as f:
        urls = [linha.strip() for linha in f if linha.strip()]

    if not urls:
        console.print("[bold yellow]Aviso:[/bold yellow] Nenhuma URL encontrada em 'link.txt'.")
        return

    console.print(f"[bold cyan]🎵 Iniciando o download de {len(urls)} música(s)...[/bold cyan]\n")

    # Configuração dos componentes visuais da barra de progresso
    with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=40),
            "[progress.percentage]{task.percentage:>3.0f}%",
            "•",
            DownloadColumn(),
            "•",
            TransferSpeedColumn(),
            "•",
            TimeRemainingColumn(),
            console=console,
    ) as progress:

        task_id = None

        def progress_hook(d):
            nonlocal task_id
            if d['status'] == 'downloading':
                filename = os.path.basename(d.get('filename', 'Música'))

                # Trunca nomes longos para não quebrar o layout do terminal
                if len(filename) > 30:
                    filename = filename[:27] + "..."

                total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate') or 0
                downloaded_bytes = d.get('downloaded_bytes', 0)

                if task_id is None:
                    task_id = progress.add_task(f"Baixando: {filename}", total=total_bytes)
                else:
                    progress.update(
                        task_id,
                        completed=downloaded_bytes,
                        total=total_bytes,
                        description=f"Baixando: [green]{filename}[/green]"
                    )

            elif d['status'] == 'finished':
                if task_id is not None:
                    progress.update(task_id, description="[bold green]✔ Finalizado![/bold green]")
                    task_id = None

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
            'progress_hooks': [progress_hook],
            'quiet': True,  # Desativa as mensagens padrão do yt-dlp
            'noprogress': True,  # Desativa a barra nativa do yt-dlp
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)

    console.print("\n[bold green]✨ Todos os downloads foram concluídos com sucesso![/bold green]")


if __name__ == '__main__':
    baixar_musicas()