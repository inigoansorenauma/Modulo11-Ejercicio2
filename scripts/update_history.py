import json
import os
import datetime

HISTORY_FILE = "history.json"
PAGES_DIR = "public"

def main():
    # 1. Leer las nuevas métricas
    with open("latest_metrics.json", "r") as f:
        latest_metrics = json.load(f)
        
    run_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_metrics["date"] = run_date
    
    # 2. Cargar histórico anterior (si existe)
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
            
    # 3. Añadir nueva ejecución y guardar
    history.insert(0, latest_metrics) # Añadir al principio
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)
        
    # 4. Generar HTML simple (Requisito: simple y pequeño)
    os.makedirs(PAGES_DIR, exist_ok=True)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Model Validation Status</title>
        <style>body {{ font-family: sans-serif; padding: 2rem; }} table {{ border-collapse: collapse; width: 100%; }} th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }} th {{ background-color: #f4f4f4; }}</style>
    </head>
    <body>
        <h1>Model Validation Status</h1>
        <h2>Latest Run: {run_date}</h2>
        <p><strong>Accuracy:</strong> {latest_metrics['accuracy']:.2%} | <strong>Precision:</strong> {latest_metrics['precision']:.2%} | <strong>Recall:</strong> {latest_metrics['recall']:.2%}</p>
        
        <hr>
        
        <h2>Execution History</h2>
        <table>
            <tr><th>Date</th><th>Accuracy</th><th>Precision</th><th>Recall</th></tr>
    """
    
    for run in history:
        html_content += f"<tr><td>{run['date']}</td><td>{run['accuracy']:.2%}</td><td>{run['precision']:.2%}</td><td>{run['recall']:.2%}</td></tr>"
        
    html_content += """
        </table>
    </body>
    </html>
    """
    
    with open(os.path.join(PAGES_DIR, "index.html"), "w") as f:
        f.write(html_content)
        
    print("✅ Histórico actualizado y HTML generado correctamente en public/index.html")

if __name__ == "__main__":
    main()