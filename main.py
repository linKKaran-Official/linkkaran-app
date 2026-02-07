# linKKaran Protocol: Main Orchestrator
# Rooted in Stability | Growing in Service

from core.logic import LinKKaranEngine

def start_protocol():
    print("--- linKKaran Protocol Initializing ---")
    
    # Memanggil Sang Penggerak
    app = LinKKaranEngine()
    
    # Simulasi Otoritas Penggunaan Tunggal
    # Ganti 'Kinanah' dengan input yang aman nantinya
    auth = app.validate_authority("Kinanah")
    print(f"Status: {auth}")
    
    if "Granted" in auth:
        print("\n[Green Interface Mode: Active]")
        print("Vibe: Natural, Elegant, and Wise.")
        print("Action: Monitoring digital equilibrium...")
        
        # Menjalankan Sapu Jagad untuk menjaga kebersihan data
        cleanup = app.execute_sapu_jagad()
        print(f"Final Action: {cleanup}")

if __name__ == "__main__":
    start_protocol()
