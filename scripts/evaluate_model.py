import json
import sys
# import tu_modelo y tus_datos_de_validacion aquí

def main():
    # AQUÍ IRÍA LA LÓGICA REAL DE TU EQUIPO DE DATA SCIENCE:
    # y_true, y_pred = model.predict(validation_data)
    # accuracy = accuracy_score(y_true, y_pred)
    # precision = precision_score(y_true, y_pred)
    # recall = recall_score(y_true, y_pred)
    
    # Valores simulados para el ejemplo (asumiendo que mejoraron el ~75% inicial)
    accuracy = 0.82
    precision = 0.85
    recall = 0.81
    
    print(f"Métricas obtenidas: Accuracy={accuracy:.2f}, Precision={precision:.2f}, Recall={recall:.2f}")
    
    # Validar que todos superen el 80% (0.80)
    if accuracy < 0.80 or precision < 0.80 or recall < 0.80:
        print("❌ ERROR: Una o más métricas cayeron por debajo del 80%. El modelo es inválido.")
        sys.exit(1) # Esto hace que la pipeline falle inmediatamente
        
    print("✅ Todas las métricas superan el 80%. El modelo es válido.")
    
    # Guardar métricas para la generación del HTML
    metrics = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall
    }
    
    with open("latest_metrics.json", "w") as f:
        json.dump(metrics, f)

if __name__ == "__main__":
    main()