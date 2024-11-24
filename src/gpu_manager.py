import torch

def check_gpu():
    """
    Verifica si una GPU está disponible en el sistema para PyTorch.
    """
    if torch.cuda.is_available():
        print(f"GPU disponible: {torch.cuda.get_device_name(0)}")
        return True
    else:
        print("No se detectó una GPU. El programa usará la CPU.")
        return False
