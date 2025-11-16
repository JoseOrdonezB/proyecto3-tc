# main.py
from config_loader import load_yaml_config
from turing_machine import TuringMachine

print(" Elige que configuración cargar:")
print(" 1. reconocedora")
print(" 2. alternadora")
choice = int(input("Ingresa tu elección:"))

if choice == 1:
    path = "reconocedora.yaml"
elif choice == 2:
    path = "alternadora.yaml"

config = load_yaml_config(path)

mt_config = config["mt"]
inputs = config.get("inputs", [])

tm = TuringMachine(mt_config)
for w in inputs:
    print("\n" + "=" * 60)
    print(f"Simulando entrada: {repr(w)}")
    print("=" * 60)

    result = tm.run(w)

    print("\nDescripciones instantáneas (IDs):")
    for i, id_str in enumerate(result["ids"]):
        print(f"Paso {i:02d}: {id_str}")

    print("\nResultado final:")
    print(f"  Cinta final : {result['final_tape']!r}")
    print(f"  Estado final: {result['final_state']}")
    print(f"  ¿Aceptada?  : {'SÍ' if result['accepted'] else 'NO'}")