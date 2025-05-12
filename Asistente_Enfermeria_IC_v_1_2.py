import tkinter as tk
from tkinter import ttk, messagebox
import os
from datetime import datetime

# Lista de dependencias para documentación:
# - Python 3.6 o superior
# - tkinter (incluido en la mayoría de instalaciones de Python)
# - No es necesario tkcalendar ya que se eliminaron los selectores de fecha

class AplicacionInsuficienciaCardiaca:
    def __init__(self, root):
        self.root = root
        self.root.title("Seguimiento de Insuficiencia Cardíaca")
        self.root.geometry("1000x750")
        self.root.resizable(True, True)
        
        # Configuración de estilo
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        self.style.configure("TButton", font=("Arial", 10, "bold"))
        self.style.configure("Heading.TLabel", font=("Arial", 12, "bold"), background="#f0f0f0")
        self.style.configure("Section.TLabel", font=("Arial", 11, "bold"), background="#e0e0e0")
        self.style.configure("Footer.TLabel", font=("Arial", 8), foreground="#888888", background="#f0f0f0")
        
        # Variables para los campos de datos
        self.crear_variables()
        
        # Crear el contenedor principal con barra de desplazamiento
        self.main_canvas = tk.Canvas(self.root, background="#f0f0f0")
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.main_canvas.yview)
        self.scrollable_frame = ttk.Frame(self.main_canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.main_canvas.configure(
                scrollregion=self.main_canvas.bbox("all")
            )
        )
        
        self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.main_canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Bind para permitir el desplazamiento con la rueda del ratón
        self.root.bind_all("<MouseWheel>", self._on_mousewheel)  # Para Windows
        self.root.bind_all("<Button-4>", self._on_mousewheel)    # Para Unix (subir)
        self.root.bind_all("<Button-5>", self._on_mousewheel)    # Para Unix (bajar)
        
        # Creación de la interfaz
        self.crear_interfaz()
    
    def _on_mousewheel(self, event):
        """Función para manejar el evento de la rueda del ratón"""
        # Diferentes sistemas tienen diferentes eventos para la rueda del ratón
        if event.num == 5 or event.delta < 0:  # Movimiento hacia abajo
            self.main_canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta > 0:  # Movimiento hacia arriba
            self.main_canvas.yview_scroll(-1, "units")
    
    def crear_variables(self):
        # Datos básicos
        self.estado_general_var = tk.StringVar()
        self.clase_nyha_var = tk.StringVar()
        self.peso_var = tk.StringVar()
        self.aumento_peso_kg_var = tk.StringVar()
        self.aumento_peso_dias_var = tk.StringVar()
        
        # Autocuidados (variables para Sí/No/NS)
        self.se_pesa_var = tk.StringVar(value="NS")
        self.liquido_dia_var = tk.StringVar()
        self.sal_comida_var = tk.StringVar(value="NS")
        self.toma_medicacion_var = tk.StringVar(value="NS")
        self.controla_ta_fc_var = tk.StringVar(value="NS")
        self.ejercicio_fisico_var = tk.StringVar(value="NS")
        self.dieta_baja_sal_var = tk.StringVar(value="NS")
        
        # Constantes
        self.ta_var = tk.StringVar()
        self.fc_var = tk.StringVar()
        
        # Signos de alarma (variables para Sí/No/NS)
        self.aumento_peso_var = tk.StringVar(value="NS")
        self.edemas_var = tk.StringVar(value="NS")
        self.distension_abdominal_var = tk.StringVar(value="NS")
        self.disminucion_diuresis_var = tk.StringVar(value="NS")
        self.dificultad_respirar_var = tk.StringVar(value="NS")
        self.ortopnea_var = tk.StringVar(value="NS")
        self.dpn_var = tk.StringVar(value="NS")
        self.tos_decubito_var = tk.StringVar(value="NS")
        self.mas_pastillas_orinar_var = tk.StringVar(value="NS")
        self.mareo_var = tk.StringVar(value="NS")
        self.astenia_var = tk.StringVar(value="NS")
        self.obnubilacion_var = tk.StringVar(value="NS")
        
        # Tratamiento
        self.tto_diuretico_var = tk.StringVar()
        
        # Evaluación y observaciones
        self.causa_desencadenante_var = tk.StringVar()
        self.precisa_consulta_var = tk.StringVar(value="NS")
        self.observaciones_var = tk.StringVar()
    
    def crear_interfaz(self):
        # Título principal
        ttk.Label(self.scrollable_frame, text="CONSULTA TELEFÓNICA DE ENFERMERÍA - INSUFICIENCIA CARDÍACA", 
                style="Heading.TLabel").grid(row=0, column=0, columnspan=6, pady=10, padx=10, sticky="w")
        
        # Marco para situación actual
        situacion_frame = ttk.LabelFrame(self.scrollable_frame, text="Situación Actual")
        situacion_frame.grid(row=1, column=0, columnspan=6, padx=10, pady=5, sticky="ew")
        
        # Primera fila de situación actual
        ttk.Label(situacion_frame, text="Estado General:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        estados = ["Estable", "Regular", "Malo"]
        ttk.Combobox(situacion_frame, textvariable=self.estado_general_var, values=estados, width=10).grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(situacion_frame, text="CF NYHA:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        nyha_classes = ["I", "II", "III", "IV"]
        ttk.Combobox(situacion_frame, textvariable=self.clase_nyha_var, values=nyha_classes, width=5).grid(row=0, column=3, padx=5, pady=5, sticky="w")
        
        ttk.Label(situacion_frame, text="TA:").grid(row=0, column=4, padx=5, pady=5, sticky="w")
        ttk.Entry(situacion_frame, textvariable=self.ta_var, width=10).grid(row=0, column=5, padx=5, pady=5, sticky="w")
        
        ttk.Label(situacion_frame, text="FC:").grid(row=0, column=6, padx=5, pady=5, sticky="w")
        ttk.Entry(situacion_frame, textvariable=self.fc_var, width=8).grid(row=0, column=7, padx=5, pady=5, sticky="w")
        
        # Segunda fila en situación actual
        ttk.Label(situacion_frame, text="Peso (kg):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(situacion_frame, textvariable=self.peso_var, width=8).grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(situacion_frame, text="Aumento de peso:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        aumento_frame = ttk.Frame(situacion_frame)
        aumento_frame.grid(row=1, column=3, columnspan=5, padx=5, pady=5, sticky="w")
        ttk.Entry(aumento_frame, textvariable=self.aumento_peso_kg_var, width=5).pack(side="left")
        ttk.Label(aumento_frame, text="Kg en").pack(side="left", padx=5)
        ttk.Entry(aumento_frame, textvariable=self.aumento_peso_dias_var, width=5).pack(side="left")
        ttk.Label(aumento_frame, text="días").pack(side="left", padx=5)
        
        # Marco para Autocuidados
        autocuidados_frame = ttk.LabelFrame(self.scrollable_frame, text="Autocuidados")
        autocuidados_frame.grid(row=2, column=0, columnspan=6, padx=10, pady=5, sticky="ew")
        
        # Sección de autocuidados en dos columnas
        col1_frame = ttk.Frame(autocuidados_frame)
        col1_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nw")
        
        col2_frame = ttk.Frame(autocuidados_frame)
        col2_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nw")
        
        # Primera columna de autocuidados
        row = 0
        ttk.Label(col1_frame, text="¿Se pesa todos los días?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_frame, text="Sí", variable=self.se_pesa_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_frame, text="No", variable=self.se_pesa_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_frame, text="NS", variable=self.se_pesa_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col1_frame, text="¿Cuánto líquido toma al día? (ml)").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(col1_frame, textvariable=self.liquido_dia_var, width=8).grid(row=row, column=1, columnspan=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col1_frame, text="¿Añade sal a su comida?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_frame, text="Sí", variable=self.sal_comida_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_frame, text="No", variable=self.sal_comida_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_frame, text="NS", variable=self.sal_comida_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col1_frame, text="¿Sigue dieta baja en sal?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_frame, text="Sí", variable=self.dieta_baja_sal_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_frame, text="No", variable=self.dieta_baja_sal_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_frame, text="NS", variable=self.dieta_baja_sal_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        # Segunda columna de autocuidados
        row = 0
        ttk.Label(col2_frame, text="¿Toma toda su medicación como pone el último informe?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_frame, text="Sí", variable=self.toma_medicacion_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_frame, text="No", variable=self.toma_medicacion_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_frame, text="NS", variable=self.toma_medicacion_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col2_frame, text="¿Se controla la TA y la FC?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_frame, text="Sí", variable=self.controla_ta_fc_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_frame, text="No", variable=self.controla_ta_fc_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_frame, text="NS", variable=self.controla_ta_fc_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col2_frame, text="¿Camina o realiza otro tipo de ejercicio físico?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_frame, text="Sí", variable=self.ejercicio_fisico_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_frame, text="No", variable=self.ejercicio_fisico_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_frame, text="NS", variable=self.ejercicio_fisico_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        # Marco para Signos de Alarma
        alarma_frame = ttk.LabelFrame(self.scrollable_frame, text="Signos de Alarma")
        alarma_frame.grid(row=3, column=0, columnspan=6, padx=10, pady=5, sticky="ew")
        
        # Sección de signos de alarma en dos columnas (igual que Autocuidados)
        col1_alarma = ttk.Frame(alarma_frame)
        col1_alarma.grid(row=0, column=0, padx=10, pady=5, sticky="nw")
        
        col2_alarma = ttk.Frame(alarma_frame)
        col2_alarma.grid(row=0, column=1, padx=10, pady=5, sticky="nw")
        
        # Primera columna de signos de alarma
        row = 0
        ttk.Label(col1_alarma, text="¿Ha aumentado de peso en los últimos días?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="Sí", variable=self.aumento_peso_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="No", variable=self.aumento_peso_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="NS", variable=self.aumento_peso_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col1_alarma, text="¿Nota los pies, las piernas o la tripa más hinchada?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="Sí", variable=self.edemas_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="No", variable=self.edemas_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="NS", variable=self.edemas_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col1_alarma, text="¿Distensión abdominal?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="Sí", variable=self.distension_abdominal_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="No", variable=self.distension_abdominal_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="NS", variable=self.distension_abdominal_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col1_alarma, text="¿Está orinando menos que habitualmente?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="Sí", variable=self.disminucion_diuresis_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="No", variable=self.disminucion_diuresis_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="NS", variable=self.disminucion_diuresis_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col1_alarma, text="¿Tiene más dificultad para respirar?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="Sí", variable=self.dificultad_respirar_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="No", variable=self.dificultad_respirar_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="NS", variable=self.dificultad_respirar_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col1_alarma, text="¿Presenta ortopnea?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="Sí", variable=self.ortopnea_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="No", variable=self.ortopnea_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col1_alarma, text="NS", variable=self.ortopnea_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        # Segunda columna de signos de alarma
        row = 0
        ttk.Label(col2_alarma, text="¿Por las noches siente más ahogo (DPN)?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="Sí", variable=self.dpn_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="No", variable=self.dpn_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="NS", variable=self.dpn_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col2_alarma, text="¿Tos en decúbito?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="Sí", variable=self.tos_decubito_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="No", variable=self.tos_decubito_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="NS", variable=self.tos_decubito_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col2_alarma, text="¿Ha necesitado tomar más pastillas para orinar?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="Sí", variable=self.mas_pastillas_orinar_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="No", variable=self.mas_pastillas_orinar_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="NS", variable=self.mas_pastillas_orinar_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col2_alarma, text="¿Mareo?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="Sí", variable=self.mareo_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="No", variable=self.mareo_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="NS", variable=self.mareo_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col2_alarma, text="¿Astenia?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="Sí", variable=self.astenia_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="No", variable=self.astenia_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="NS", variable=self.astenia_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(col2_alarma, text="¿Obnubilación?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="Sí", variable=self.obnubilacion_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="No", variable=self.obnubilacion_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(col2_alarma, text="NS", variable=self.obnubilacion_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        # Marco para Tratamiento y Observaciones
        tto_frame = ttk.LabelFrame(self.scrollable_frame, text="Tratamiento y Observaciones")
        tto_frame.grid(row=4, column=0, columnspan=6, padx=10, pady=5, sticky="ew")
        
        row = 0
        ttk.Label(tto_frame, text="Tratamiento diurético:").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(tto_frame, textvariable=self.tto_diuretico_var, width=60).grid(row=row, column=1, columnspan=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(tto_frame, text="Posible causa desencadenante:").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(tto_frame, textvariable=self.causa_desencadenante_var, width=60).grid(row=row, column=1, columnspan=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(tto_frame, text="¿Precisa consulta/valoración conjunta con el médico?").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(tto_frame, text="Sí", variable=self.precisa_consulta_var, value="Sí").grid(row=row, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(tto_frame, text="No", variable=self.precisa_consulta_var, value="No").grid(row=row, column=2, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(tto_frame, text="NS", variable=self.precisa_consulta_var, value="NS").grid(row=row, column=3, padx=5, pady=5, sticky="w")
        
        row += 1
        ttk.Label(tto_frame, text="Observaciones:").grid(row=row, column=0, padx=5, pady=5, sticky="w")
        
        row += 1
        observaciones_text = tk.Text(tto_frame, width=80, height=4)
        observaciones_text.grid(row=row, column=0, columnspan=4, padx=5, pady=5, sticky="w")
        
        # Asociar el Text widget a la variable de control
        def observaciones_callback(*args):
            self.observaciones_var.set(observaciones_text.get("1.0", "end-1c"))
        
        observaciones_text.bind("<KeyRelease>", observaciones_callback)
        
        # Botones para generar el informe y limpiar
        btn_frame = ttk.Frame(self.scrollable_frame)
        btn_frame.grid(row=5, column=0, columnspan=6, pady=15)
        
        ttk.Button(btn_frame, text="Crear Informe", command=self.generar_informe, style="TButton").pack(side="left", padx=10)
        ttk.Button(btn_frame, text="Limpiar Formulario", command=self.limpiar_formulario, style="TButton").pack(side="left", padx=10)
        
        # Firma discreta al final
        firma_frame = ttk.Frame(self.scrollable_frame)
        firma_frame.grid(row=6, column=0, columnspan=6, pady=5)
        ttk.Label(firma_frame, 
                 text="Creado por Alejandro Venegas Robles, si presenta incidencias o sugerencias, contactar con alejandro2196vr@gmail.com",
                 style="Footer.TLabel").pack(pady=10)
    
    def limpiar_formulario(self):
        """Limpia todos los campos del formulario"""
        for var in self.__dict__.values():
            if isinstance(var, tk.StringVar):
                if var in [self.se_pesa_var, self.sal_comida_var, self.toma_medicacion_var, 
                          self.controla_ta_fc_var, self.ejercicio_fisico_var, self.aumento_peso_var,
                          self.edemas_var, self.disminucion_diuresis_var, self.dificultad_respirar_var,
                          self.ortopnea_var, self.dpn_var, self.tos_decubito_var, self.mareo_var,
                          self.astenia_var, self.obnubilacion_var, self.distension_abdominal_var,
                          self.dieta_baja_sal_var, self.precisa_consulta_var, self.mas_pastillas_orinar_var]:
                    var.set("NS")
                else:
                    var.set("")
        
    def generar_informe(self):
        """Genera un informe estructurado basado en los datos ingresados"""
        try:
            # Crear informe sin verificar campos obligatorios
            informe = self.crear_texto_informe()
            
            # Mostrar informe en una ventana nueva
            self.mostrar_informe(informe)
            
        except Exception as e:
            messagebox.showerror("Error al generar informe", str(e))
    
    def crear_texto_informe(self):
        """Crea el texto del informe basado en los datos ingresados"""
        # Inicio del informe
        informe = f"CONSULTA TELEFÓNICA DE ENFERMERÍA - INSUFICIENCIA CARDÍACA\n\n"
        
        # Situación actual (en una línea)
        situacion_items = []
        
        if self.estado_general_var.get():
            situacion_items.append(f"Estado general: {self.estado_general_var.get()}")
        
        if self.clase_nyha_var.get():
            situacion_items.append(f"CF NYHA: {self.clase_nyha_var.get()}")
        
        if self.ta_var.get() or self.fc_var.get():
            constantes = []
            if self.ta_var.get():
                constantes.append(f"TA: {self.ta_var.get()} mmHg")
            if self.fc_var.get():
                constantes.append(f"FC: {self.fc_var.get()} lpm")
            
            if constantes:
                situacion_items.append(", ".join(constantes))
        
        if self.peso_var.get():
            situacion_items.append(f"Peso: {self.peso_var.get()} kg")
        
        if self.aumento_peso_kg_var.get() and self.aumento_peso_dias_var.get():
            situacion_items.append(f"Aumento de peso: {self.aumento_peso_kg_var.get()} kg en {self.aumento_peso_dias_var.get()} días")
        
        if situacion_items:
            informe += "SITUACIÓN ACTUAL: " + "; ".join(situacion_items) + ".\n\n"
        
        # Autocuidados - MODIFICADO
        autocuidados_positivos = []
        autocuidados_negativos = []
        
        # Procesar cada variable de autocuidados
        if self.se_pesa_var.get() == "Sí":
            autocuidados_positivos.append("Control diario de peso")
        elif self.se_pesa_var.get() == "No":
            autocuidados_negativos.append("Control diario de peso")
        
        if self.liquido_dia_var.get():
            autocuidados_positivos.append(f"Ingesta de líquidos: {self.liquido_dia_var.get()} ml/día")
        
        if self.sal_comida_var.get() == "Sí":
            autocuidados_negativos.append("Evita añadir sal a las comidas")
        elif self.sal_comida_var.get() == "No":
            autocuidados_positivos.append("Evita añadir sal a las comidas")
        
        if self.dieta_baja_sal_var.get() == "Sí":
            autocuidados_positivos.append("Sigue dieta baja en sal")
        elif self.dieta_baja_sal_var.get() == "No":
            autocuidados_negativos.append("Seguir dieta baja en sal")
        
        if self.toma_medicacion_var.get() == "Sí":
            autocuidados_positivos.append("Adherencia a la medicación")
        elif self.toma_medicacion_var.get() == "No":
            autocuidados_negativos.append("Adherencia a la medicación")
        
        if self.controla_ta_fc_var.get() == "Sí":
            autocuidados_positivos.append("Autocontrol de TA/FC")
        elif self.controla_ta_fc_var.get() == "No":
            autocuidados_negativos.append("Autocontrol de TA/FC")
        
        if self.ejercicio_fisico_var.get() == "Sí":
            autocuidados_positivos.append("Realiza ejercicio físico")
        elif self.ejercicio_fisico_var.get() == "No":
            autocuidados_negativos.append("Realizar ejercicio físico")
        
        # Añadir sección de autocuidados al informe
        informe += "AUTOCUIDADOS:\n"
        if autocuidados_positivos:
            informe += "El paciente refiere:\n- " + "\n- ".join(autocuidados_positivos) + "\n"
        
        if autocuidados_negativos:
            informe += "El paciente no realiza:\n- " + "\n- ".join(autocuidados_negativos) + "\n"
        
        if not autocuidados_positivos and not autocuidados_negativos:
            informe += "No se ha podido valorar autocuidados.\n"
        
        informe += "\n"
        
        # Signos y síntomas - MODIFICADO
        signos_presentes = []
        signos_negados = []
        
        # Verificar cada signo y añadirlo a la lista correspondiente
        if self.aumento_peso_var.get() == "Sí":
            signos_presentes.append("Aumento de peso")
        elif self.aumento_peso_var.get() == "No":
            signos_negados.append("Aumento de peso")
            
        if self.edemas_var.get() == "Sí":
            signos_presentes.append("Edemas")
        elif self.edemas_var.get() == "No":
            signos_negados.append("Edemas")
            
        if self.distension_abdominal_var.get() == "Sí":
            signos_presentes.append("Distensión abdominal")
        elif self.distension_abdominal_var.get() == "No":
            signos_negados.append("Distensión abdominal")
            
        if self.disminucion_diuresis_var.get() == "Sí":
            signos_presentes.append("Disminución de la diuresis")
        elif self.disminucion_diuresis_var.get() == "No":
            signos_negados.append("Disminución de la diuresis")
            
        if self.dificultad_respirar_var.get() == "Sí":
            signos_presentes.append("Disnea")
        elif self.dificultad_respirar_var.get() == "No":
            signos_negados.append("Disnea")
            
        if self.ortopnea_var.get() == "Sí":
            signos_presentes.append("Ortopnea")
        elif self.ortopnea_var.get() == "No":
            signos_negados.append("Ortopnea")
            
        if self.dpn_var.get() == "Sí":
            signos_presentes.append("Disnea paroxística nocturna")
        elif self.dpn_var.get() == "No":
            signos_negados.append("Disnea paroxística nocturna")
            
        if self.tos_decubito_var.get() == "Sí":
            signos_presentes.append("Tos en decúbito")
        elif self.tos_decubito_var.get() == "No":
            signos_negados.append("Tos en decúbito")
            
        if self.mas_pastillas_orinar_var.get() == "Sí":
            signos_presentes.append("Ha necesitado aumentar dosis de diuréticos")
        elif self.mas_pastillas_orinar_var.get() == "No":
            signos_negados.append("Aumento de dosis de diuréticos")
            
        if self.mareo_var.get() == "Sí":
            signos_presentes.append("Mareo")
        elif self.mareo_var.get() == "No":
            signos_negados.append("Mareo")
            
        if self.astenia_var.get() == "Sí":
            signos_presentes.append("Astenia")
        elif self.astenia_var.get() == "No":
            signos_negados.append("Astenia")
            
        if self.obnubilacion_var.get() == "Sí":
            signos_presentes.append("Obnubilación")
        elif self.obnubilacion_var.get() == "No":
            signos_negados.append("Obnubilación")
        
        # Añadir sección de signos y síntomas al informe
        informe += "SIGNOS Y SÍNTOMAS ACTUALES:\n"
        
        if signos_presentes:
            informe += "El paciente presenta: " + ", ".join(signos_presentes) + ".\n"
        
        if signos_negados:
            informe += "El paciente niega: " + ", ".join(signos_negados) + ".\n"
        
        if not signos_presentes and not signos_negados:
            informe += "No se han podido valorar signos o síntomas de descompensación.\n"
        
        informe += "\n"
        
        # Tratamiento
        if self.tto_diuretico_var.get():
            informe += f"TRATAMIENTO DIURÉTICO ACTUAL:\n{self.tto_diuretico_var.get()}\n\n"
        
        # Posible causa
        if self.causa_desencadenante_var.get():
            informe += f"POSIBLE CAUSA DESENCADENANTE:\n{self.causa_desencadenante_var.get()}\n\n"
        
        # Valoración
        if self.precisa_consulta_var.get() != "NS":
            informe += f"VALORACIÓN:\n"
            if self.precisa_consulta_var.get() == "Sí":
                informe += "El paciente requiere valoración médica.\n\n"
            else:
                informe += "No se considera necesaria valoración médica en este momento.\n\n"
        
        # Observaciones
        if self.observaciones_var.get():
            informe += f"OBSERVACIONES:\n{self.observaciones_var.get()}\n"
        
        return informe
    
    def mostrar_informe(self, informe):
        """Muestra el informe en una ventana nueva con opciones para guardar o copiar"""
        # Crear ventana modal
        informe_window = tk.Toplevel(self.root)
        informe_window.title("Informe de Consulta Telefónica")
        informe_window.geometry("700x500")
        informe_window.transient(self.root)
        informe_window.grab_set()
        
        # Marco con barra de desplazamiento
        frame = ttk.Frame(informe_window)
        frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Área de texto con barra de desplazamiento
        scroll = ttk.Scrollbar(frame)
        texto = tk.Text(frame, wrap="word", width=80, height=20)
        scroll.pack(side="right", fill="y")
        texto.pack(side="left", fill="both", expand=True)
        scroll.config(command=texto.yview)
        texto.config(yscrollcommand=scroll.set)
        
        # Insertar el informe
        texto.insert("1.0", informe)
        texto.config(state="disabled")  # Hacer el texto de solo lectura
        
        # Marco para botones
        btn_frame = ttk.Frame(informe_window)
        btn_frame.pack(pady=10)
        
        # Botón para copiar al portapapeles
        def copiar_portapapeles():
            informe_window.clipboard_clear()
            informe_window.clipboard_append(informe)
            messagebox.showinfo("Información", "Informe copiado al portapapeles")
        
        # Botón para guardar como archivo
        def guardar_archivo():
            try:
                # Obtener la ruta del escritorio
                desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') \
                          if os.name == 'nt' else os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
                
                # Crear nombre de archivo con fecha y hora
                fecha_hora = datetime.now().strftime("%Y%m%d_%H%M")
                nombre_archivo = f"Consulta_IC_{fecha_hora}.txt"
                ruta_completa = os.path.join(desktop, nombre_archivo)
                
                # Guardar archivo
                with open(ruta_completa, 'w', encoding='utf-8') as f:
                    f.write(informe)
                
                messagebox.showinfo("Información", f"Informe guardado como:\n{ruta_completa}")
            except Exception as e:
                messagebox.showerror("Error al guardar", str(e))
        
        ttk.Button(btn_frame, text="Copiar al portapapeles", command=copiar_portapapeles).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Guardar como archivo", command=guardar_archivo).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Cerrar", command=informe_window.destroy).pack(side="left", padx=5)

# Función principal para iniciar la aplicación
def main():
    root = tk.Tk()
    app = AplicacionInsuficienciaCardiaca(root)
    root.mainloop()

if __name__ == "__main__":
    main()